# Show paths and poses in the ADVIO dataset
#
# Description:
# Show all pose tracks for a given dataset
#
# Parameters:
# - Path to data folder
# - Dataset number 
# - Raw or aligned
# - Number of cameras to draw
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
align = 'raw'!= sys.argv[3]
sample=float(sys.argv[4])
scale=float(sys.argv[5])


#import files
path= folder+'/advio-'+str(i).zfill(2)+'/ground-truth/pose.csv'
M_gt=myt.read_pose(path)
path= folder+'/advio-'+str(i).zfill(2)+'/ground-truth/fixpoints.csv'
M_fix=myt.read_fix(path)
path= folder+'/advio-'+str(i).zfill(2)+'/iphone/arkit.csv'
M_kt=myt.read_pose(path)
path= folder+'/advio-'+str(i).zfill(2)+'/pixel/arcore.csv'
M_px=myt.read_pose(path)
path= folder+'/advio-'+str(i).zfill(2)+'/tango/raw.csv'
M_tr=myt.read_pose(path)
path= folder+'/advio-'+str(i).zfill(2)+'/tango/area-learning.csv'
M_ta=myt.read_pose(path)

#Fix title
titl=' aligned to Fixpoints' if align else ''


# for each pose track either draw raw or align to fixpoints and draw.
if align:
    M_gt=myt.align_to_fixpoints(M_gt,M_fix)
plt.figure(figsize=(15,4))
axe=myt.plot_path(M_gt,sample,scale)
axe[1].set_title('Ground Truth'+titl)


if align:
    M_kt=myt.align_to_fixpoints(M_kt,M_fix)
plt.figure(figsize=(15,4))
myt.plot_path(M_kt,sample,scale)
plt.title('ARKit'+titl)


if align:
    M_px=myt.align_to_fixpoints(M_px,M_fix)
plt.figure(figsize=(15,4))
axe=myt.plot_path(M_px,sample,scale)
axe[1].set_title('ARCore'+titl)


if align:
    M_tr=myt.align_to_fixpoints(M_tr,M_fix)
plt.figure(figsize=(15,4))
axe=myt.plot_path(M_tr,sample,scale)
axe[1].set_title('Tango Raw'+titl)


if align:
    M_ta=myt.align_to_fixpoints(M_ta,M_fix)
plt.figure(figsize=(15,4))
axe=myt.plot_path(M_ta,sample,scale)
axe[1].set_title('Tango Area Learning'+titl)


plt.show()

