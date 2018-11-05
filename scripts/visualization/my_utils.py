# Utils for visualization 
#
# Description:
#   Various functions for geometric manipulation and visualization of data in the ADVIO dataset.
#
# Copyright (C) 2018 Santiago Cortes
#
# This software is distributed under the GNU General Public 
# Licence (version 2 or later); please refer to the file 
# Licence.txt, included with the software, for details.

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

def draw_camera_top(pos,ori,sc,side,ax='NULL'):
    # Draw the camera in the given position and orientation.
    # Input
    # pos: the position of the camera.
    # ori: the orientation of the camera.
    # sc: the scale of the camera to be drawn(in the same units as pos).
    # side: the side to be orthographically projected onto.
    # ax: axes of the figure to be drawn.
    # Output
    # none
    
    # create camera model (z axis going into the camera)
    cam=np.ndarray(shape=(3,15),dtype=float)
    x=np.array([ 0, 1,-1,-1,-1, 0, 1,-1,-1, 0, 1, 1, 1,-1, 0])
    y=np.array([ 0, 1, 1,-1,-1, 0,-1,-1, 1, 0, 1,-1, 1, 1,-1])
    z=np.array([ 0,-1,-1,-1,-1, 0,-1,-1,-1, 0,-1,-1,-1,-1,-1])
    cam[0,:]=x
    cam[1,:]=y
    cam[2,:]=z*5
    cam=cam*sc
    
    # Transform camera object inot given space.
    pos= np.array(pos)[np.newaxis]
    cam=ori@cam+pos.T
    
    # Draw camera body and points for  orientation clarity.
    if ax=='NULL':
        ax=plt.gca()
    ax.plot(cam[side[0],-2],cam[side[1],-2],'r.',linewidth=2.0)   
    ax.plot(cam[side[0],-3],cam[side[1],-3],'c.',linewidth=2.0)
    #ax.plot(cam[side[0],-1],cam[side[1],-1],'g.',linewidth=2.0)
    ax.plot(cam[side[0],:-3],cam[side[1],:-3],'k',linewidth=0.2)
    
def plot_side(M,sample,scale,side,n=-1,ax='NULL'):
    # Plot a whole sequence orthographically projected onto one side.
    name=['x','y','z']
    if ax=='NULL':
        ax=plt.gca()
        
    # plot entire track
    ax.plot(M[:,side[0]+1],M[:,side[1]+1]) 
    ax.axis('equal')    
    ax.set_xlabel(name[side[0]])
    ax.set_ylabel(name[side[1]])
    
    # If sample is zero, just draw the pose inticated by n.
    # If sample is not zero, sample that many poses linearly distributed and darw them.
    if sample==0:
        quat=np.quaternion(M[n,4],M[n,5],M[n,6],M[n,7])
        draw_camera_top(M[n,1:4],quaternion.as_rotation_matrix(quat),scale,side,ax)
    else:
        for i in range(0,np.shape(M)[0],int(np.shape(M)[0]/sample)):
            quat=np.quaternion(M[i,4],M[i,5],M[i,6],M[i,7])
            draw_camera_top(M[i,1:4],quaternion.as_rotation_matrix(quat),scale,side,ax)

def plot_path(M,sample,scale):  
    # Plot an entire path from three sides
    sides=[[0,1],[2,0],[2,1]]
    axe=[]
    for index,side in enumerate(sides):
        axe.append(plt.subplot(1,3,index+1))    
        plot_side(M,sample,scale,side,ax=axe[index])
    return axe

def read_pose(path):
    # read the given pose file into a numpy array
    data=pd.read_csv(path,names=list('tabcdefg'))
    v=[]
    for c in 'tabcdefg':
        v.append(np.array(list(map(float,data[list(c)].values))))
    M=np.column_stack((v[0],v[1],v[2],v[3],v[4],v[5],v[6],v[7]))
    #M=M[np.sum(M[:,4:8]**2,1)>0.01,:]
    return M

def read_frames(path):
    # read the given frame times into a numpy array
    data=pd.read_csv(path,names=list('ta'))    
    v=[]
    for c in 'ta':
        v.append(np.array(list(map(float,data[list(c)].values))))
    M=np.column_stack((v[0],v[1]))
    return M

def read_fix(path):
    # read fixpoint file into numpy array
    data=pd.read_csv(path,names=list('tabcdef'))
    v=[]
    for c in 'tabcdef':
        v.append(np.array(list(map(float,data[list(c)].values))))
    M=np.column_stack((v[0],v[1],v[3],v[2],v[4],v[5],v[6]))
    return M

def my_procrustes(m1,m2):
    #procrustes algorithm with no scaling and no reflection.    

    mu1=np.mean(m1,0)
    mu2=np.mean(m2,0)
    
    m10=m1-mu1
    m20=m2-mu2
    
    ssq1=np.sum(m10**2,0)
    ssq2=np.sum(m20**2,0)
    
    ssq1=np.sum(ssq1)
    ssq2=np.sum(ssq2)
    
    n1=np.sqrt(ssq1)
    n2=np.sqrt(ssq2)
 
    m10=m10/n1
    m20=m20/n2
    
    A=m10.T@m20
    L,d,M=np.linalg.svd(A)
    M=M.T
    T=M@L.T
 
    if np.linalg.det(T)<0:
        M[:,-1]=-M[:,-1]
        d[-1]=d[-1]
        T=M@L.T
    
    trac=sum(d)
    
    scale=1
    d=1 + ssq2/ssq1 - 2*trac*n2/n1
    
    trans=mu1-scale*mu2@T
    return T,trans
    
def align_to_fixpoints(M_path,M_fix):
    # align pose track to fixpoints.
    samp_index=[]
    for i in range(0,np.shape(M_fix)[0]):
        samp_index.append(int(np.argmin((M_path[:,0]-M_fix[i,0])**2)))
    R,trans=my_procrustes(M_fix[:,1:4],M_path[samp_index,1:4])
    trans= np.array(trans)[np.newaxis]
    M_path2=M_path
    M_path2[:,1:4]=(M_path[:,1:4]@R+trans)
    for i in range(0,np.shape(M_path)[0]):
        quat=np.quaternion(M_path[i,4],M_path[i,5],M_path[i,6],M_path[i,7])
        R_q=quaternion.as_rotation_matrix(quat)
        n_quat=quaternion.from_rotation_matrix(R.T@R_q)
        M_path2[i,4:8]=quaternion.as_float_array(n_quat)   
    return(M_path2)

def plot_path_frame(M_p,M_fr,video_name,t,pscale,axis='NULL'):
    # plot a frame and the path at the sime time.
    ind_frame=int(np.argmin((M_fr[:,0]-t)**2))
    ind_pose=int(np.argmin((M_p[:,0]-t)**2))
    frame=get_frame(video_name,ind_frame)    
    if axis=='NULL':
        ax1=plt.subplot(1,2,1)
        ax2=plt.subplot(1,2,2)
    else:
        ax1=axis[0]
        ax2=axis[1]
       
    ax1.imshow(frame,cmap='Greys_r')
    ax1.axis('off')
    
    plot_side(M_p,sample=0,scale=pscale,n=ind_pose,side=[2,0],ax=ax2)
    return ax1,ax2
    
def get_frame(video_name,N):
    # get a frame from ADVIO video stream at a given time.
    cap = cv2.VideoCapture(video_name)
    totalFrames = cap.get(cv2.CAP_PROP_FRAME_COUNT)
    if N>totalFrames:
        print('Not a valid frame index')
        return False
    cap.set(cv2.CAP_PROP_POS_FRAMES,N)
    ret, frame = cap.read()
    frame=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    if np.shape(frame)[0]==720:
        frame=frame.swapaxes(1,0)
        frame=np.flip(frame,1)
    cap.release()
    return frame