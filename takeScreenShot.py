import cv2


def takeScreenShot():
    videoCaptureObject = cv2.VideoCapture(0,cv2.CAP_DSHOW)
    result = True

    while (result):
        ret, frame = videoCaptureObject.read()
        print(frame)

        cv2.imwrite("Image1.jpg", frame)
        
        normal = 2

        if normal < 1 :
            result = False
        

    videoCaptureObject.release()

    cv2.destroyAllWindows()

takeScreenShot()
