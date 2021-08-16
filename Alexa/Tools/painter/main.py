import cv2
import numpy as np
import os
import HandTrackingModule as hTM

#######################
brushThickness = 25
eraserThickness = 100
########################

headerPath = 'Header'


def paint():
    folderPath = headerPath
    myList = os.listdir(folderPath)
    overlayList = []
    for imPath in myList:
        image = cv2.imread(f'{folderPath}/{imPath}')
        overlayList.append(image)
    header = overlayList[0]
    drawColor = (255, 0, 255)

    cap = cv2.VideoCapture(0)
    cap.set(3, 1280)
    cap.set(4, 720)

    detector = hTM.handDetector(detectionCon=0.65, maxHands=1)
    xp, yp = 0, 0
    imgCanvas = np.zeros((720, 1280, 3), np.uint8)
    while True:

        # 1. Import image
        success, img = cap.read()
        img = cv2.flip(img, 1)

        # 2. Find Hand Landmarks
        img = detector.findHands(img)
        lmList = detector.findPosition(img, draw=False)

        if len(lmList) != 0:

            # tip of index and middle fingers
            x1, y1 = lmList[8][1:]
            x2, y2 = lmList[12][1:]

            # 3. Check which fingers are up
            fingers = detector.fingersUp()

            # 4. If Selection Mode - Two finger are up
            if fingers[1] and fingers[2]:
                cv2.putText(img, 'Selection Mode', (10, 300), cv2.FONT_HERSHEY_COMPLEX_SMALL, 3, (0, 0, 0), 3)
                # Checking for the click
                if y1 < 125:
                    if 250 < x1 < 450:
                        header = overlayList[0]
                        drawColor = (255, 0, 255)
                    elif 550 < x1 < 750:
                        header = overlayList[1]
                        drawColor = (255, 76, 0)
                    elif 800 < x1 < 950:
                        header = overlayList[2]
                        drawColor = (0, 255, 0)
                    elif 1050 < x1 < 1200:
                        header = overlayList[3]
                        drawColor = (0, 0, 0)
                cv2.rectangle(img, (x1, y1 - 25), (x2, y2 + 25), drawColor, cv2.FILLED)

            # 5. If Drawing Mode - Index finger is up
            if fingers[1] and fingers[2] == False:
                cv2.putText(img, 'Drawing Mode', (10, 300), cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 255), 3)
                cv2.circle(img, (x1, y1), 15, drawColor, cv2.FILLED)
                if xp == 0 and yp == 0:
                    xp, yp = x1, y1

                cv2.line(img, (xp, yp), (x1, y1), drawColor, brushThickness)

                if drawColor == (0, 0, 0):
                    cv2.line(img, (xp, yp), (x1, y1), drawColor, eraserThickness)
                    cv2.line(imgCanvas, (xp, yp), (x1, y1), drawColor, eraserThickness)

                else:
                    cv2.line(img, (xp, yp), (x1, y1), drawColor, brushThickness)
                    cv2.line(imgCanvas, (xp, yp), (x1, y1), drawColor, brushThickness)

                xp, yp = x1, y1

        imgGray = cv2.cvtColor(imgCanvas, cv2.COLOR_BGR2GRAY)
        _, imgInv = cv2.threshold(imgGray, 50, 255, cv2.THRESH_BINARY_INV)
        imgInv = cv2.cvtColor(imgInv, cv2.COLOR_GRAY2BGR)
        img = cv2.bitwise_and(img, imgInv)
        img = cv2.bitwise_or(img, imgCanvas)

        # Setting the header image
        img[0:125, 0:1280] = header
        if cv2.waitKey(10) == ord('q'):
            break
        cv2.imshow("lol.exe", img)
        cv2.waitKey(1)


paint()
