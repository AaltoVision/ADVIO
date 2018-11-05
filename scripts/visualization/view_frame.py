# Show path and pose beside th frame in the ADVIO dataset
#
# Description:
# Show a frame and the associated path and pose
#
# Parameters:
# - Path to data folder
# - Dataset number 
# - Time in the video
# - Size of camera model
#
# Copyright (C) 2018 Santiago Cortes
#
# This software is distributed under the GNU General Public 
# Licence (version 2 or later); please refer to the file 
# Licence.txt, included with the software, for details.


import sys
# Using pandas to read the dataset files.
import pandas as pd

# Using numpy quaternions for rotation manipulation.
import numpy as np
import quaternion

# Using matplolib for visualization.
import matplotlib.pyplot as plt
import matplotlib as mpl

# Using opencv to parse the video file.
import cv2

#import functions
import my_utils as myt

#parse arguments
folder=sys.argv[1]
i=sys.argv[2]
time=float(sys.argv[3])
scale=float(sys.argv[4])

#get data locations
path= folder+'/advio-'+str(i).zfill(2)+'/iphone/frames.csv'
M_fr=myt.read_frames(path)
path= folder+'/advio-'+str(i).zfill(2)+'/ground-truth/pose.csv'
M_gt=myt.read_pose(path)
path=folder+'/advio-'+str(i).zfill(2)+'/ground-truth/fixpoints.csv'
M_fix=myt.read_fix(path)
video_name = folder+'/advio-'+str(i).zfill(2)+'/iphone/frames.mov'


#plot the frame and top view of ground truth.
fig=plt.figure(figsize=[15,5])
ax1=plt.subplot(121)
ax2=plt.subplot(122)
myt.plot_path_frame(myt.align_to_fixpoints(M_gt,M_fix),M_fr,video_name,time,scale,[ax1,ax2])
ax1.set_title('Video Frame at '+str(time)+' seconds')
ax2.set_title('Ground truth Pose at '+str(time)+' seconds')
plt.show()