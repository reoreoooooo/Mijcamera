import cv2
import os
import time

def save_frame_camera_key(device_num, dir_path, basename, ext='png', delay=1, window_name='frame'):
    cap = cv2.VideoCapture(device_num)
    cap.set(4, 3156)
    cap.set(3, 4224)


    '''for c,x in enumerate(range(37)):
        print("%4d:%s"%(c,cap.get(x)))'''

    if not cap.isOpened():
        return

    '''os.makedirs(dir_path, exist_ok=True)
    base_path = os.path.join(dir_path, basename)'''

    n = 0
    while True:
        ret, frame = cap.read()
        cv2.imshow(window_name, frame)
        key = cv2.waitKey(delay) & 0xFF
        if key == ord('c'):
            ret, frame = cap.read()
            cv2.imwrite('{}.{}'.format(n, ext), frame)
            n += 1
        elif key == ord('q'):
            break

    cv2.destroyWindow(window_name)


save_frame_camera_key(1, 'data/temp', 'camera_capture')