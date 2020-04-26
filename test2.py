import cv2
import os
import time
import logging

def save_frame_camera_key(device_num, dir_path, basename, ext='png', delay=10, window_name='frame'):
    cap = cv2.VideoCapture(device_num)
    cap.set(4, 480)
    cap.set(3, 640)
    cap.set(cv2.CAP_PROP_AUTO_WB,0)
    cap.set(cv2.CAP_PROP_AUTO_EXPOSURE,0)
    cap.set(cv2.CAP_PROP_WB_TEMPERATURE,5500)
    cap.set(cv2.CAP_PROP_EXPOSURE,200)



    for c,x in enumerate(range(37)):
        print("%4d:%s"%(c,cap.get(x)))

    if not cap.isOpened():
        return

    '''os.makedirs(dir_path, exist_ok=True)
    base_path = os.path.join(dir_path, basename)'''
    n = 0
    for _ in range(3):
        while True:
            try:
                ret, frame = cap.read()
                cv2.imshow(window_name, frame)
                key = cv2.waitKey(delay) & 0xFF
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
                if key == ord('c'):    
                    for i in range(10):
                        try:
                            cap.set(4,720)
                            cap.set(3, 1280)
                            print("capture try" + str(i+1))
                            ##time.sleep(1)
                            ret, frame = cap.read()
                            cv2.imshow(window_name, frame)
                            cv2.imwrite('picture/{}.{}'.format(i+1, ext), frame)
                            cap.set(4, 480)
                            cap.set(3, 640)
                            print("pictured:" + str(i+1))
                        except:
                            print("----------------------------------------------------")
                            print("error occurred" + str(i+1))
                            cap.release()
                            cap = cv2.VideoCapture(device_num)
                            cap.set(4, 480)
                            cap.set(3, 640)
                            print("rebooted" + str(i+1))
                            pass
                        else:
                            print("well done" + str(i+1))   
                        
                elif key == ord('q'):
                    break
            except:
                cap.release()
                cap = cv2.VideoCapture(device_num)
                cap.set(4, 480)
                cap.set(3, 640)
                pass
    cv2.destroyWindow(window_name)


save_frame_camera_key(0, 'data/temp', 'camera_capture')