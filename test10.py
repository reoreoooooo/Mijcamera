import cv2
import os
import sys
import time
import logging

def save_frame_camera_key(device_num, dir_path, basename, ext='png', delay=10, window_name='frame'):
    ##sys.stdout = open("log.txt","w")
    # フォーマットを定義
    formatter = '%(levelname)s : %(asctime)s : %(message)s'
    # ログレベルを DEBUG に変更
    logging.basicConfig(filename='logfile/logger.log',level=logging.DEBUG, format=formatter)
    ##logging.info('info %s %s', 'test', 'test')
    cap = cv2.VideoCapture(device_num)
    cap.set(4, 480)
    cap.set(3, 640)


    '''for c,x in enumerate(range(37)):
        print("%4d:%s"%(c,cap.get(x)))'''

    if not cap.isOpened():
        return

    '''os.makedirs(dir_path, exist_ok=True)
    base_path = os.path.join(dir_path, basename)'''
    n = 0
    for _ in range(3):
        try:
            ret, frame = cap.read()
            cv2.imshow(window_name, frame)
            ##key = cv2.waitKey(delay) & 0xFF
            '''if key == ord('c'):
                print("camera change")
                cap.set(4, 3156)
                cap.set(3, 4224)
                print("gasitu change up")
                ret, frame = cap.read()
                cv2.imshow(window_name, frame)
                cv2.imwrite('picture/{}.{}'.format(n, ext), frame)
                print("camera change")
                cap.set(4, 480)
                cap.set(3, 640)
                print("gasitu chamge down")
                n += 1'''
            for i in range(10):
                try:
                    cap.set(4,720)
                    cap.set(3, 1280)
                    print("capture try:" + str(i+1))
                    logging.info('info %s %s', 'test', "capture try:" + str(i+1))
                    ret, frame = cap.read()
                    cv2.imshow(window_name, frame)
                    if os.path.exists("picture"):
                        cv2.imwrite('picture/{}.{}'.format(i+1, ext), frame)
                        cap.set(4, 480)
                        cap.set(3, 640)
                        print("pictured:" + str(i+1))
                        logging.info('info %s %s', 'test', "pictured:" + str(i+1))
                        print("well done:" + str(i+1))
                        logging.info('info %s %s', 'test', "well done:" + str(i+1))
                    else:
                        logging.critical('critical %s %s', 'test', 'directory does not exists' )
                except:
                    print("----------------------------------------------------")
                    logging.error('info %s %s', 'test', "----------------------------------------------------")
                    print("error occurred:" + str(i+1))
                    logging.error('info %s %s', 'test', "error occurred:" + str(i+1))
                    cap.release()
                    cap = cv2.VideoCapture(device_num)
                    cap.set(4, 480)
                    cap.set(3, 640)
                    print("rebooted:" + str(i+1))
                    logging.error('info %s %s', 'test', "rebooted:" + str(i+1))
                    
            print("10kai seikou")
            logging.info('info %s %s', 'test', "10kai seikou") 
        except:
            cap.release()
            cap = cv2.VideoCapture(device_num)
            cap.set(4, 480)
            cap.set(3, 640)
            pass
        else:
            print("break")
            logging.info('info %s %s', 'test', "break")
            break
    else:
        ##sys.stdout.close()
        cv2.destroyWindow(window_name)



for j in range(1):
    save_frame_camera_key(0, 'data/temp', 'camera_capture')