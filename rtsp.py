
import vlc
import cv2
import socket
import re
import time
from datetime import datetime
#import bitstring
# #
# # player=vlc.MediaPlayer('rtsp://admin:888888@192.168.0.164:10554/udp/av0_0')
# # player.play()
#
# path = '/home/david/Desktop/motion-images/'
# vcap = cv2.VideoCapture('rtsp://admin:888888@192.168.0.164:10554/tcp/av0_0')
# #time.sleep(2)
#
# count = 1
# while True:
#         time.sleep(.2)
#         ret, frame = cv2.VideoCapture('rtsp://admin:888888@192.168.0.164:10554/tcp/av0_0').read()
#
#         if frame is None:
#             continue
#
#
#         #cv2.imwrite(path + datetime.now().strftime('%Y%m%d_%Hh%Mm%Ss%f') + '.jpg', frame)
#         #cv2.imshow('VIDEO', frame)
#         count = count + 1
#         print(count)
#         cv2.waitKey(1)
#         vcap.release()

# import cv2 ;print(cv2.getBuildInformation())


# import time
# import cv2
#
# from datetime import datetime
# count = 1
#
# path = '/home/david/Desktop/motion-images/test/'
#
#
# while True:
#
#         count = count + 1
#         print(count)
#
#         img = cv2.imread('/home/david/Desktop/motion-images/img.jpg', 0)
#         if img is not None:
#
#
#                 cv2.imshow('image', img)
#                 print("print" + str(count))
#         #cv2.imwrite(path + datetime.now().strftime('%Y%m%d_%Hh%Mm%Ss%f') + '.jpg', img)
#         cv2.destroyAllWindows()
#         time.sleep(.2) #wa
#         #cv2.waitKey(0)
#         #cv2.destroyAllWindows()
#

import time
import cv2
print(cv2.__version__)

url = 'rtsp://admin:888888@192.168.0.164:10554/tcp/av0_0'
vidcap = cv2.VideoCapture(url)
#rt,image = vidcap.read()
path = '/home/david/Desktop/motion-images/test/'
count = 0
#success = True
while(vidcap.isOpened()):
  #time.sleep(.1)
  #cv2.imwrite("frame%d.jpg" % count, image)     # save frame as JPEG file
  ret,image = vidcap.read()
  if image is not None and ret is True:

    #cv2.imwrite(path + datetime.now().strftime('%Y%m%d_%Hh%Mm%Ss%f') + '.jpg', image)
    cv2.imshow('frame', image)
    print('Read a new frame: ', str(count))
    count += 1
    if cv2.waitKey(1) & 0xFF == ord('q'):
      break
  else:
    print("Print Missing")



vidcap.release()
  #out.release()
cv2.destroyAllWindows()