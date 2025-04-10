import cv2
import os



# img = cv2.imread("assets/amina.jpg", cv2.IMREAD_COLOR)

# # make image smaller
# height, width = img.shape[:2]
# img = cv2.resize(img, (640, 360))
# root = os.getcwd()


# BORDER

# img = cv2.copyMakeBorder(img, 20, 20, 20, 20,
#                          borderType=cv2.BORDER_CONSTANT,
#                          value=(200, 0, 0))


# LINE

# double click drawing
def drawCircle(event, x, y, flags, param):
    img = param
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img, (x, y), 10, (0, 0, 255), -1)
    
    
    
def doubleClickDrawing():
    root = os.getcwd() # gets the current working directory path
    imgPath = os.path.join(root, 'assets\\amina.jpg') # get the path of the image
    img = cv2.imread(imgPath) # reads the image
    windowName = 'drawing app'
    cv2.namedWindow(windowName) #set name of window
    cv2.setMouseCallback(windowName, drawCircle, img) 
    
    while True:
        cv2.imshow(windowName, img)
        if cv2.waitKey(1) == ord('q'):
            break

class DrawingApp:
    def __init__(self, imagePath):
        self.imagePath = imagePath
        self.startX, self.startY = 0, 0
        self.isDrawing = False

    def drawLine(self, event, x, y, flags, param):
        img = param
        if event == cv2.EVENT_LBUTTONDOWN:
            self.isDrawing = True
            print("drawing start")
            self.startX, self.startY = x, y
        elif event == cv2.EVENT_MOUSEMOVE and self.isDrawing:
            cv2.line(img(self.startX, self.startY), (x, y), (255, 255, 255), 3)
            print("drawing continue")
        elif event == cv2.EVENT_LBUTTONUP:
            self.isDrawing = False
            cv2.line(img(self.startX, self.startY), (x, y), (255, 255, 255), 3)
            print("drawing stopped")
    
    def run(self):
        img = cv2.imread(self.imagePath)
        windowName = 'drawing app'
        cv2.namedWindow(windowName) #set name of window
        cv2.setMouseCallback(windowName, self.drawLine, img) 
    
        while True:
            cv2.imshow(windowName, img)
            if cv2.waitKey(1) == ord('q'):
                break
        
def holdAndDragDrawing():
    root = os.getcwd() # gets the current working directory path
    imgPath = os.path.join(root, 'assets\\amina.jpg') # get the path of the image
    app = DrawingApp(imgPath)
    app.run()
    
if __name__ == '__main__':
    # doubleClickDrawing()
    holdAndDragDrawing()
    
    
# ARROW

# CIRCLE

# ELLIPSE

# RECTANGLE

# TEXT

# cv2.imshow("amina", img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()