import cv2
import numpy as np

camera = cv2.VideoCapture(0) # get camera

print("Getting Camera....")

while True:
    _ , video = camera.read()
    cv2.imshow("camera",video) # show the camera

    #find center
    width  = round(camera.get(cv2.CAP_PROP_FRAME_WIDTH))   # int `width`
    height = round(camera.get(cv2.CAP_PROP_FRAME_HEIGHT))  # int `height
    center = width // 2 , height // 2
    
    #hsv frame
    hsvFrame = cv2.cvtColor(video, cv2.COLOR_BGR2HSV)
    cv2.imshow("hsv",hsvFrame) # show the filtered frame

    #red mask
    red_lower = np.array([136, 87, 111], np.uint8)
    red_upper = np.array([180, 255, 255], np.uint8)
    red_mask = cv2.inRange(hsvFrame, red_lower, red_upper)
    
    # find the red places 
    contours, _ = cv2.findContours(red_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    #draw vertical and horizontal lines
    video = cv2.line(video, (0, height//2), (width, height//2), (0,0,0), thickness=5) # draw horizontal line
    video = cv2.line(video, (width // 2, 0), (width // 2, height), (0,0,0), thickness=5) # draw verical line

    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if(area > 500): # just look for larger parts
            x, y, w, h = cv2.boundingRect(contour)
            centerOfContour = x + w // 2, y + h //2

            # check for position
            writeCommand = ""
            if(center[0] * 0.5 > centerOfContour[0]):
                writeCommand = "go right"
            elif(center[0] > centerOfContour[0]):
                writeCommand = "go faster right"
            elif(center[0] * 1.5 < centerOfContour[0]):
                writeCommand = "go left"
            else:
                writeCommand = "go faster left"
            
            #draw
            video = cv2.rectangle(video, (x, y), (x + w, y + h), (0, 0, 255), 2) #draw a rectangel for found obsitcle
            cv2.putText(video, "RED", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 255)) # write it is red
            cv2.putText(video, writeCommand, (width - len(writeCommand) * 20, height - 10), cv2.FONT_HERSHEY_TRIPLEX, 1.0, (0, 0, 255)) # write the command

    #last frame
    cv2.imshow("filtered",video) # last frame, find the red, write command, draw the axiis
    cv2.waitKey(1)

# After the loop release the cap object
camera.release()
# Destroy all the windows
cv2.destroyAllWindows()