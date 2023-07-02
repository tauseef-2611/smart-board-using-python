from PIL.Image import linear_gradient
import cv2
import numpy as np
import time
import pyautogui as pg
import HandTracking as ht
import autopy   # Install using "pip install autopy"
from pynput.mouse import Button, Controller

### Variables Declaration
pTime = 0               # Used to calculate frame rate
width = 960            # Width of Camera
height = 480            # Height of Camera
frameR = 100            # Frame Rate
smoothening = 8         # Smoothening Factor
prev_x,prev_x1,prev_y1,prev_y = 0,0,0,0   # Previous coordinates
curr_x,curr_x1, curr_y,curr_y1 = 0,0,0, 0   # Current coordinates
mouse=Controller()

cap = cv2.VideoCapture(0)   # Getting video feed from the webcam
cap.set(3, width)           # Adjusting size
cap.set(4, height)

detector = ht.handDetector(maxHands=1)                  # Detecting one hand at max
screen_width, screen_height = autopy.screen.size()      # Getting the screen size
while True:
    success, img = cap.read()
    img = detector.findHands(img)                       # Finding the hand
    lmlist, bbox = detector.findPosition(img)           # Getting position of hand
   
    if len(lmlist)!=0:
        x1, y1 = lmlist[8][1:]
        x2, y2 = lmlist[12][1:]
        fingers = detector.fingersUp()      # Checking if fingers are upwards
        x3 = np.interp(x1, (frameR,width-frameR), (0,screen_width))
        y3 = np.interp(y1, (frameR, height-frameR), (0, screen_height))
        curr_x = prev_x + (x3 - prev_x)/smoothening
        curr_y = prev_y + (y3 - prev_y) / smoothening
        cv2.rectangle(img, (frameR, frameR), (width - frameR, height - frameR), (255, 0, 255), 2)   # Creating boundary box
        if fingers[1] == 1 and fingers[2] == 0:     # If fore finger is up and middle finger is down
            autopy.mouse.move(screen_width - curr_x, curr_y)    # Moving the cursor
            cv2.circle(img, (x1, y1), 7, (255, 0, 255), cv2.FILLED)
            prev_x, prev_y = curr_x, curr_y



        if fingers[1] == 1 and fingers[2] == 1:     # If fore finger & middle finger both are up
            length, img, lineInfo = detector.findDistance(8, 12, img)

            if length < 40:     # If both fingers are really close to each other
                cv2.circle(img, (lineInfo[4], lineInfo[5]), 15, (0, 255, 0), cv2.FILLED)
                #print(curr_x1,curr_y1)
                #autopy.mouse.clik()
                mouse.press(Button.left)
                autopy.mouse.move(screen_width - curr_x, curr_y) 
        
        if fingers[1] == 1 and fingers[0]==1:     # If fore finger & thumb both are up
            length, img, lineInfo = detector.findDistance(4, 8, img)

            if length < 40:     # If both fingers are really close to each other
                cv2.circle(img, (lineInfo[4], lineInfo[5]), 15, (0, 255, 0), cv2.FILLED)
                #print(curr_x1,curr_y1)
                #autopy.mouse.clik()
                mouse.click(Button.right)

                '''
                while True:
                    
                    x4 = np.interp(x1, (frameR,width-frameR), (0,screen_width))
                    y4 = np.interp(y1, (frameR, height-frameR), (0, screen_height))
                    curr_x1 = prev_x1 + (x4 - prev_x1)/smoothening
                    curr_y1 = prev_y1 + (y4 - prev_y1) / smoothening
                    pg.dragTo(screen_width - curr_x1, curr_y1)
                x4 = np.interp(x1, (frameR,width-frameR), (0,screen_width))
                y4 = np.interp(y1, (frameR, height-frameR), (0, screen_height))
                curr_x1 = prev_x1 + (x4 - prev_x1)/smoothening
                curr_y1 = prev_y1 + (y4 - prev_y1) / smoothening
                while length<40:
                    autopy.mouse.click()
                autopy.mouse.move(screen_width-x4,y4)
                       



                        if fingers[0]==1 and fingers[1]==1:
            length, img, lineInfo = detector.findDistance(4, 8, img)
            if length<40:
                cv2.circle(img, (lineInfo[4], lineInfo[5]), 15, (0, 255, 0), cv2.FILLED)
                mouse.press(Button.left)
                autopy.mouse.move(screen_width - curr_x, curr_y) 



                startposition=(screen_width - curr_x, curr_y)
                for i in range (height*width):
                    currentposition=(screen_width - curr_x, curr_y)
                    pg.leftClick()
                    pg.dragTo(currentposition)
                    if length>40:
                        break
                autopy.mouse.click()  #click
                print(curr_x,curr_y)
                autopy.mouse.move(screen_width-curr_x,curr_y)'''

    mouse.release(Button.left)
    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime
    cv2.putText(img, str(int(fps)), (20, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)
    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break