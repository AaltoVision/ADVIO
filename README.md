![DOI 10.5281/zenodo.1320824](https://zenodo.org/badge/DOI/10.5281/zenodo.1320824.svg)

# ADVIO: An Authentic Dataset for Visual-Inertial Odometry

[Santiago Cortés](https://research.aalto.fi/portal/santiago.cortesreina.html) · [Arno Solin](http://arno.solin.fi) · [Esa Rahtu](http://esa.rahtu.fi) · [Juho Kannala](https://users.aalto.fi/~kannalj1/) 

The lack of realistic and open benchmarking datasets for pedestrian visual-inertial odometry has made it hard to pinpoint differences in published methods. Existing datasets either lack a full six degree-of-freedom ground-truth or are limited to small spaces with optical tracking systems. We take advantage of advances in pure inertial navigation, and develop a set of versatile and challenging real-world computer vision benchmark sets for visual-inertial odometry. For this purpose, we have built a test rig equipped with an iPhone, a Google Pixel Android phone, and a Google Tango device. We provide a wide range of raw sensor data that is accessible on almost any modern-day smartphone together with a high-quality ground-truth track. We also compare resulting visual-inertial tracks from Google Tango, ARCore, and Apple ARKit with two recent methods published in academic forums. The data sets cover both indoor and outdoor cases, with stairs, escalators, elevators, office environments, a shopping mall, and metro station.

## Example video

This video shows the ground-truth track for data set \#16 (captured in one of the two office buildings). The visualized track is the ground-truth track calculated from the entire IMU data sequence. The fix points used for track calculation are visualized by dots. The track on the current floor shows in red. The video has been sped-up.

[![ADVIO Dataset 16](https://img.youtube.com/vi/AU_PXxvxBHM/0.jpg)](http://www.youtube.com/watch?v=AU_PXxvxBHM)

## Attribution

If you use this data, please cite the original paper presenting it:

* Santiago Cortés, Arno Solin, Esa Rahtu, and Juho Kannala (2018). *ADVIO: An authentic dataset for visual-inertial odometry.* Accepted for publication in European Conference on Computer Vision (ECCV). Munich, Germany.


# Downloading the data

The data files are available for download on Zenodo: [https://zenodo.org/record/1320824](https://zenodo.org/record/1320824) and can be downloaded on a per dataset basis from there. You can also use `wget` with the following bash snippet to fetch all the data:

```bash
# Download all 23 data ZIPs from Zenodo
for i in $(seq -f "%02g" 1 23);
do
  wget -O advio-$i.zip https://zenodo.org/record/1321157/files/advio-$i.zip
done
```

The size of one set ranges from 71 Mb to 255 Mb (packed). Uncompressed total size around 5.1 Gb.

# Details on collected data

![Setup](https://github.com/AaltoVision/ADVIO/blob/master/setup.png)

## Ground-truth

* __Ground-truth poses:__ Camera pose (translation and orientation) calculated based on the raw IMU data and a set of known fixation points. The ground-truth track is sampled at 100 Hz.

* __Fix points:__ A set of ground-truth points marked with a visual editor. The points are based on the three videos stored by the system (primarily the iPhone and the second iPhone that filmed a reference track showing the capturer) and floor plan layouts.

## iPhone

* __Camera frames:__ Camera frames are captured at 60 fps (resolution of 1280 by 720, portrait). The exact frame acquisition times reported by the platform are stored. The frames are packed into an H.264/MPEG-4 video file.

* __Platform location:__ Data collected through CoreLocation. The update rate depends on the device and its capabilities. Locations are requested with the desired accuracy of kCLLocationAccuracyBest. The timestamps are converted to follow the same clock as the other sensors (time interval since device boot). The stored values are

  * Coordinate.latitude
  * Coordinate.longitude
  * HorizontalAccuracy
  * Altitude
  * VerticalAccuracy
  * Speed

* __Accelerometer:__ Data collected through CoreMotion/CMMotionManager. Acquired at 100 Hz, which is the maximum rate. CoreMotion reports the accelerations in 'g's (at standstill you expect to have 1g in the vertical direction).

* __Gyroscope:__ Data collected through CoreMotion/CMMotionManager. Acquired at 100 Hz, which is the maximum rate. Note that the readings are in the Apple device coordinate frame (not altered in any way here).

* __Magnetometer:__ Data collected through CoreMotion/CMMotionManager. Acquired at 100 Hz, which is the maximum rate. Values are the three-axis magnetometer readings in uT. All values are uncalibrated.

* __Barometric altimeter:__ Data collected through CoreMotion/CMAltimeter. Acquired at an uneven sampling rate (roughly 1 Hz). Samples are stored as they arrive from the delegare callback. The actual barometric pressure is in val0 and the inferred relative altutude (calculated by Apple magic) is stored in val1.

* __ARKit poses:__ The Apple ARKit poses (translation and orientation) are captured at 60 Hz.

## Tango

* __Tango poses (raw):__ The Google Tango raw poses (translation and orientation) are captured at 60 Hz.

* __Tango poses (area learning):__ The Google Tango area learning poses (translation and orientation) are captured at 60 Hz.

* __Camera frames:__ Video from the wide-angle (fisheye) camera on the Tango. Captured at ~5 fps with  640 by 480 resolution. The frames are packed into an MPEG-4 video file.

* __Tango point clouds:__ Tango point cloud data acquired by the Tango device and aligned to the current pose of the device. Sampling rate is not uniform. Timestamps are stored in `point-cloud.csv`. The actual point clouds are stored in the corresponding `point-cloud-$index.csv`.

## Pixel

* __ARCore poses:__ The Google ARCore poses (translation and orientation) are captured at 30 Hz.


# List of data sets

The following table summarizes the features of the 23 data sets:

|Id|Venue|Dataset|In/Out|Stairs|Escalator|Elevator|People|Vehicles|
|:---------:|:---------:|:---------:|:---------:|:---------:|:---------:|:---------:|:---------:|:---------:|
|1  | Mall  | 01  | Indoor  |  | ✔ |  | Moderate  |
|2  | Mall  | 02  | Indoor  |  |  |  | Moderate  |
|3  | Mall  | 03  | Indoor  |  |  |  | Moderate  |
|4  | Mall  | 04  | Indoor  |  | ✔ |  | Moderate  |
|5  | Mall  | 05  | Indoor  | ✔ |  |  | Moderate  |
|6  | Mall  | 06  | Indoor  |  |  |  | High  |
|7  | Mall  | 07  | Indoor  |  |  | ✔ | Low  |
|8  | Mall  | 08  | Indoor  |  | ✔ |  | Low  |
|9  | Mall  | 09  | Indoor  |  | ✔ |  | Low  |
|10  | Mall  | 10  | Indoor  |  |  |  | Low  |
|11  | Metro  | 01  | Indoor  |  |  |  | High  | ✔
|12  | Metro  | 02  | Indoor  |  |  |  | High  | ✔
|13  | Office  | 01  | Indoor  | ✔ |  |  | Low  |
|14  | Office  | 02  | Indoor  | ✔ |  | ✔ | Low  |
|15  | Office  | 03  | Indoor  |  |  |  | None  |
|16  | Office  | 04  | Indoor  | ✔ |  |  | None  |
|17  | Office  | 05  | Indoor  | ✔ |  |  | None  |
|18  | Office  | 06  | Indoor  | ✔ |  | ✔ | None  |
|19  | Office  | 07  | Indoor  | ✔ |  |  | None  |
|20  | Outdoor | 01  | Outdoor  |  |  |  | Low  | ✔
|21  | Outdoor | 02  | Outdoor  |  |  |  | Low  | ✔
|22  | Outdoor (urban)  | 01  | Outdoor  |  |  |  | High  | ✔
|23  | Outdoor (urban)  | 02  | Outdoor  |  |  |  | High  | ✔


# Data structure

To maximize compatibility, all data is published in open and simple file formats. The comma separated value (CSV) files hold a timestamp in the first column and the respective data in the columns that follow. All time stamps are synchronized between sensor types and devices. Camera frames are stored as H.264/MPEG video and the associated frame time stamps are available in separate CSV files.

The folder structure for one data set looks like the following:

```
data
└───advio-01
│   └───ground-truth
│   │     poses.csv
│   │     fixpoints.csv
│   └───iphone
│   │     frames.mov
│   │     frames.csv
│   │     platform-location.csv
│   │     accelerometer.csv
│   │     gyroscope.csv
│   │     magnetometer.csv
│   │     barometer.csv
│   │     arkit.csv
│   └───tango
│   │     frames.mov
│   │     frames.csv
│   │     raw.csv
│   │     area-learning.csv
│   │     point-cloud.csv
│   │     point-cloud-001.csv
│   │     point-cloud-002.csv
│   │     ...
│   └───pixel
│         arcore.csv
│     
└───advio-02
      ...
```

# Privacy

This data is collected in public places in Finland, and the collection of the data agrees with the local legislation. We, however, take your privacy seriously. If you find yourself in the data and wish to be removed, please contact us through the contact information provided at the top of this page.

# Licence

The ADVIO data is published under the [Creative Commons Attribution-NonCommercial 4.0 (CC BY-NC 4.0) Licence](https://creativecommons.org/licenses/by-nc/4.0/). This means that you must attribute the work in the manner specified by the authors and you may not use this work for commercial purposes.
