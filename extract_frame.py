#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  2 19:05:23 2022

@author: qahoang
"""

import cv2
import glob
from os import listdir
from os.path import isfile, join

video_dir = "Python_Data/test_videos"
image_dir = "Python_Data/test_dataset"

videoFiles = [f for f in listdir(video_dir) 
              if f.endswith('.mp4')]
labelFiles = [l for l in listdir(video_dir) 
              if l.endswith('.txt')]

videoIdx = []
labelIdx = []

for videoFilename in videoFiles:
    tokVideoFilename = videoFilename.split('.')
    labelFilename = tokVideoFilename[0] + "_LABELS.txt"
    
    # videoIdx.append(videoFiles.index(videoFilename))
    # labelIdx.append(labelFiles.index(labelFilename))

    video_capt = cv2.VideoCapture(join(video_dir, videoFilename))
    label_file = open(join(video_dir, labelFilename), "r")
    
    if (video_capt.isOpened() == False):
        print("Error opening video stream or file")

    # Frame index starts from 1        
    frameID = 1
    
    while(video_capt.isOpened()):
        ret, frame = video_capt.read()
        label = label_file.readline()

        if ret == True:
            imageFilename = tokVideoFilename[0] + "_{:04}.jpg".format(frameID)
            bboxFilename = tokVideoFilename[0] + "_{:04}.txt".format(frameID)
            frameID += 1

            bboxFilestream = open(join(image_dir, bboxFilename), "w")
            cv2.imwrite(join(image_dir, imageFilename), frame)
            bboxFilestream.write(label)
            bboxFilestream.close()
            
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break
            
        else:
            break

    video_capt.release()
    cv2.destroyAllWindows()

# print(videoIdx)
# print(labelIdx)