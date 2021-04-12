#!/usr/bin/python3

import cv2
import time

path_file = './source_file/'
cap = cv2.VideoCapture('rtsp://admin:1234568899@10.10.150.119:554/h264/ch2/main/av_stream')
flag = 0

def main ():
    while (cap.isOpened()):
        cap.set(cv2.CAP_PROP_POS_FRAMES,flag) #设置帧数标记
        ret,im = cap.read()#get photo
        #cv2.waitKey(2000)#延时
        cv2.imwrite(path_file+'{}.jpg'.format(flag),im)#save photo
        flag+=1#set photo number
        time.sleep( 3 )
        if not ret:
            break
            
if __name__ == '__main__':
    main()
