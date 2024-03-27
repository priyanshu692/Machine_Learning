import time

import cv2

import mediapipe as mp

mpPose = mp.solutions.pose
pose = mpPose.Pose()

mpDraw = mp.solutions.drawing_utils
cap = cv2.VideoCapture("video1")
pTime = 0
while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = pose.process(imgRGB)
    # print(results.pose_landmarks)
    if results.pose_landmarks:
        mpDraw.draw_landmarks(img, results.pose_landmarks, mpPose.POSE_CONNECTIONS, )
        for id, lm in enumerate(results.pose_landmarks.landmark):
            print(id, lm)
            h, w, c = img.shape
            cx, cy = int(lm.x * w), int(lm.y * h)
            print(id, cx, cy)
            cv2.circle(img, (cx, cy), 3, (0, 255, 255), cv2.FILLED)
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img, str(int(fps)), (70, 50), cv2.FONT_HERSHEY_PLAIN, 3, (5, 0, 100), 3)

    cv2.imshow("image", img)
    cv2.waitKey(2)
