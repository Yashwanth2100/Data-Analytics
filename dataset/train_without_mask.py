# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 13:34:20 2021

@author: Bobby
"""

import cv2
import os.path
# Opens the inbuilt camera of laptop to capture video.
cap = cv2.VideoCapture(0)
i = 0
path='dataset/without_mask'
while(cap.isOpened()):
    ret, frame = cap.read()
     
    # This condition prevents from infinite looping
    # incase video ends.
    if ret == False:
        break
     
    # Save Frame by Frame into disk using imwrite method
    cv2.imwrite(os.path.join(path,'No_mask'+str(i)+'.jpg'), frame)
    i += 1
 
cap.release()
cv2.destroyAllWindows()
