
import cv2



def diffImg(t0, t1, t2):


    d1 = cv2.absdiff(t2, t1)

    d2 = cv2.absdiff(t1, t0)

    return cv2.bitwise_and(d1, d2)


url = 'rtsp://admin:888888@192.168.0.164:10554/tcp/av0_0'
#vidcap = cv2.VideoCapture(url)
cam = cv2.VideoCapture(url)



winName = "Movement Indicator"

cv2.namedWindow(winName, cv2.WINDOW_AUTOSIZE)




t_minus = cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)

t = cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)

t_plus = cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)

fgbg=cv2.createBackgroundSubtractorMOG2()



while(cam.isOpened()):

    ret, frame = cam.read()
    if frame is not None and ret is True:
        cv2.imshow(winName, diffImg(t_minus, t, t_plus))
        #ret, frame = cv2.imread('/home/david/Desktop/motion-images/img.jpg')
        videoMasked = fgbg.apply(frame)
        cv2.imshow('fgmask' ,videoMasked )
        t_minus = t

        t = t_plus

        t_plus = cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY)

        key = cv2.waitKey(10)

        if cv2.waitKey(1) & 0xFF == ord('q'):

            cv2.destroyWindow(winName)
            print("Goodbye")

            break


