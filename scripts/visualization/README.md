# Visualization scripts for the ADVIO data

Python scripts that parse and visualize the pose data from the dataset.

## Prerequisites

- Python 3
- [Numpy](http://www.numpy.org/)
- [Numpy quaternion](https://pypi.org/project/numpy-quaternion/)
- [pandas](https://pandas.pydata.org/) (0.23)
- [Matplotlib](https://matplotlib.org/)
- [Opencv](https://pypi.org/project/opencv-python/) for python (3.3)

The examples asume that the data has been downloaded and unzipped in the ADVIO/data folder

## Video frames

The video frames are packed into a video file. The script view_frame.py shows one frame and its associated ground truth pose.

```
# Usage
python view_frame $path$ $dataset number$ $time$ $camera scale$
# Example to produce the image below
python view_frame ../../data 1 aligned 50 0.5
```

![pose](https://github.com/AaltoVision/ADVIO/blob/master/scripts/visualization/example-frame.png)

## Pose tracks

The pose tracks are shown in their raw form (optional alignment to the fixpoints). The script show_dataset.py show them orthographically projected to top, front and left views.
```
# Usage
python show_dataset $path$ $dataset number$ $alignment$ $sample$ $camera scale$
# Example to produce the images below
python show_dataset ../../data 1 aligned 50 0.5
```

![pose](https://github.com/AaltoVision/ADVIO/blob/master/scripts/visualization/example.png)
