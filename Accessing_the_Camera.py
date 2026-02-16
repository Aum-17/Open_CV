import cv2
import sys

s=0
if len(sys.argv)>1:
    s=sys.argv[1]

source=cv2.VideoCapture(s)

win_name="Camera Preview"
cv2.namedWindow(win_name,cv2.WINDOW_NORMAL)

while cv2.waitKey(1)!=27: # Escape
    has_frame, frame=source.read()
    ''' Horizontal Flip: frame = cv2.flip(frame, 1),
        Vertical Flip: frame = cv2.flip(frame, 0),ṇ
        Both Flipped: frame=cv2.flip(frame,-1) '''   
    #frame=cv2.flip(frame,1)

    if not has_frame:
        break
    cv2.imshow(win_name,frame)  

source.release()
cv2.destroyWindow(win_name)