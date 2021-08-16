import cv2
import datetime
import winsound

cap = cv2.VideoCapture(0)

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
smile_cascade = cv2.CascadeClassifier('haarcascade_smile.xml')


def start():
    while True:
        _, frame = cap.read()
        original_frame = frame.copy()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        face = face_cascade.detectMultiScale(gray, 1.3, 5)
        for x, y, w, h in face:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 255), 2)
            face_roi = frame[y:y+h, x:x+w]
            gray_roi = gray[y:y+h, x:x+w]
            smile = smile_cascade.detectMultiScale(gray_roi, 1.3, 25)
            if cv2.waitKey(10) == ord('s'):
                time_stamp = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
                file_name = f'selfie-{time_stamp}.png'
                cv2.imwrite(file_name, original_frame)
                winsound.PlaySound('alert.wav', winsound.SND_ASYNC)
        cv2.imshow('Press "s" to take selfie', frame)
        if cv2.waitKey(10) == ord('q'):
            break
