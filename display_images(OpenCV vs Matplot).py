import cv2
import matplotlib.pyplot as plt

road_img=cv2.imread("C:/Users/aumpa/OneDrive/Desktop/OpenCV/images/road.jpg")
coke_img=cv2.imread("C:/Users/aumpa/OneDrive/Desktop/OpenCV/images/c1.png")

# Use matplotlib imshow()
plt.imshow(road_img)
plt.title("Road Image")
plt.show()

# Use OpenCV imshow(),display for 8sec
window1=cv2.namedWindow("w1")
cv2.imshow(window1,road_img)
cv2.wait(8000)
cv2.destroyWindow(window1)

window2=cv2.namedWindow("w2")
cv2.imshow(coke_img)
cv2.wait(8000)
cv2.destroyWindow(window2)

# Use OpenCV imshow(), display until any key is pressed 
window3=cv2.namedWindow("w3")
cv2.imshow(window3,road_img)
cv2.wait(0)
cv2.destroyWindow(window3)

window4=cv2.namedWindow("w4")

Alive=True
while Alive:
    # Use OpenCV imshow(), display until 'q' key is pressed
    cv2.imshow(window4,road_img)
    keypress=cv2.wait(1)
    if keypress==ord('q'):
        Alive=False
cv2.destroyWindow(window4)
cv2.destroyAllWindows()
stop=1
