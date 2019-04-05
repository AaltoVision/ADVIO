# Create ROSBAG with the IMU and uncompressed video data 
#
# Description:
#   Create data structure containing IMU and ARKit data.
#
# Arguments:
#   - Data folder.
#   - sequences to bag
#
# Copyright (C) 2018 Santiago Cortes
#
# This software is distributed under the GNU General Public 
# Licence (version 2 or later); please refer to the file 
# Licence.txt, included with the software, for details.

# Import system libraries 
import sys, os
import csv
import numpy as np
# Import ros libraries.
from ros import rosbag
from cv_bridge import CvBridge, CvBridgeError
import roslib
roslib.load_manifest('sensor_msgs')
from sensor_msgs.msg import Image
from sensor_msgs.msg import Imu
#Deal with ros and opencv path error.
if '/opt/ros/kinetic/lib/python2.7/dist-packages'in sys.path:
    sys.path.remove('/opt/ros/kinetic/lib/python2.7/dist-packages')
import rospy
# Import opencv
import cv2

# Read arguments
# Folder
folder= sys.argv[1]
# If number argument is added, just build that rosbag. Else, build all.
try:
    sys.argv[2]
except:
    tst = range(1,24)
else:
    tst = [int(sys.argv[2])]

print('Creating rosbags for sequences in '+ str(tst))
    
# Delete first frames
start=0.5

# Loop trough all sequences.
for i in iter(tst):
    # Find folder
    dir =folder+'/advio-'+str(i).zfill(2)+'/iphone'
    print(dir)
    
    # Initialize bag, data and video reader.
    bag =rosbag.Bag(dir+'/'+'iphone.bag', 'w')
    index=0
    csvfile=open(dir+'/'+'imu-gyro.csv')
    datareader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    
    # Initialize bridge.
    bridge=CvBridge()
    
    # Read video and check for number of frames.
    vidcap = cv2.VideoCapture(dir+'/'+'frames.mov')
    vlength = int(vidcap.get(cv2.CAP_PROP_FRAME_COUNT))
    
    # For each row in the data matrix
    for row in datareader:
        # Read data row
        sp=row[0].split(",")
        
        # If the row correspond to a frame
        if int(float(sp[1]))==7:
            # Read next frame and check.
            success,image = vidcap.read()
            if success and float(sp[0])>start:
                
                
                stamp=float(sp[0])
                Stamp = rospy.rostime.Time.from_sec(stamp)

                # Put image in corect orientation and convert into grayscale.
                gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                gray_image=cv2.transpose(gray_image)
                gray_image=cv2.flip(gray_image,+1)
                
                # Print progress.
                if index%500==0:
                    print(str(int(np.round(100*float(index)/float(vlength))))+'%')
                index=index+1
 
                # Create ros image and put frame in it.
                Img = Image()
                Img=bridge.cv2_to_imgmsg(gray_image,encoding='mono8')
                Img.header.stamp = Stamp
                
                # Put image in rosbag.
                bag.write('/cam0/image_raw', Img, Stamp)
  
        # If the row corresponds to an IMU measurement.
        elif int(float(sp[1]))==34 and float(sp[0])>start:
            
            # check time in row and make ros format.
            stamp=float(sp[0])
            Stamp = rospy.rostime.Time.from_sec(stamp)
            
            # Read acceleration and rotational rate.
            gyr=(sp[2:5:1])
            acc=(sp[5:8:1])
            
            # Create imu ros structure and put in the bias corrected values.
            imu=Imu()
            imu.header.stamp=Stamp
            imu.angular_velocity.x=float(gyr[0])+0.0067
            imu.angular_velocity.y=float(gyr[1])-0.0070
            imu.angular_velocity.z=float(gyr[2])+0.0065

            imu.linear_acceleration.x=(float(acc[0])-0.0407)
            imu.linear_acceleration.y=(float(acc[1])+0.0623)
            imu.linear_acceleration.z=(float(acc[2])-0.1017)
            
            # Put Imu measurement in rosbag.
            bag.write('/imu0',imu,Stamp)
    # Finish rosbag
    bag.close() 
print('Process complete')
