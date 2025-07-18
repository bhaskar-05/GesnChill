import cv2 as cv
import time
import HandTrackingModule as htm
import pyautogui as pag

cap = cv.VideoCapture(0)
detector = htm.handDetector(maxHands=1)

pTime = 0
current_action = None

while True:
    success, img = cap.read()
    img = cv.flip(img, 1)   # flip webcam for mirror view

    img = detector.findHands(img)
    lmlist, bbox = detector.findPosition(img)

    action = None
    key = None

    if len(lmlist) != 0:
        fingers = detector.fingersUp()
        print(f"Fingers: {fingers}")  # debug print

        # Example gestures:
        if fingers == [1, 1, 0, 0, 0]:
            action = 'forward'; key = 'w'
            cv.putText(img, "FORWARD", (50,100), cv.FONT_HERSHEY_SIMPLEX, 2, (0,0,255), 3)

        elif fingers == [0, 0, 0, 0, 0]:
            action = 'left'; key = 'a'
            cv.putText(img, "LEFT", (50,100), cv.FONT_HERSHEY_SIMPLEX, 2, (255,0,0), 3)

        elif fingers == [1, 0, 0, 0, 1]:
            action = 'right'; key = 'd'
            cv.putText(img, "RIGHT", (50,100), cv.FONT_HERSHEY_SIMPLEX, 2, (0,255,0), 3)

        elif fingers == [1, 0, 0, 0, 0]:
            action = 'brake'; key = 's'
            cv.putText(img, "BRAKE", (50,100), cv.FONT_HERSHEY_SIMPLEX, 2, (0,255,255), 3)

    # If gesture changed → release old key & press new key
    if action != current_action:
        for k in ['w','a','s','d']:
            pag.keyUp(k)

        if key:
            pag.keyDown(key)

        current_action = action

    # show FPS
    cTime = time.time()
    fps = 1 / (cTime - pTime) if cTime != pTime else 0
    pTime = cTime
    cv.putText(img, f"FPS: {int(fps)}", (20,50), cv.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)

    cv.imshow("Image", img)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

# release keys & cleanup
for k in ['w','a','s','d']:
    pag.keyUp(k)

cap.release()
cv.destroyAllWindows()
saa