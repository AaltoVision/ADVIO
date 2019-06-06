# Convert ADVIO files into a ROSBAG

## Summary

Demonstration script to convert the advio files into a rosbag with /cam0/image_raw and /imu0 topics.

## Dependencies

Ubuntu 16.04 and python 3 were used in all the tests.

* [ROS](http://wiki.ros.org/kinetic) (Kinetic kame)
* [OpenCV](http://wiki.ros.org/kinetic) (3.4.5)

Note that the ROS cv-bridge has to be built with python 3. (see [this](https://stackoverflow.com/questions/49221565/unable-to-use-cv-bridge-with-ros-kinetic-and-python3))

## Instructions

### Create IMU measurements by resampling.
files are created for all sequences in data/advio-xx/iphone/imu-gyro.csv

```bash
python sync-data.py <data folder>
```

### Create ROSBAG for one sequence
bag is created for the sequence in data/advio-xx/iphone/iphone.bag
```bash
python advio_to_rosbag.py <data folder> <sequence number>
```
## Example

Build the rosbag for sequence 15 in (...)/ADVIO/data

```bash
python sync-data.py (...)/ADVIO/data
python advio_to_rosbag.py (...)/ADVIO/data 15
```
