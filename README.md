# ADVIO

The lack of realistic and open benchmarking datasets for pedestrian visual-inertial odometry has made it hard to pinpoint differences in published methods. Existing datasets either lack a full six degree-of-freedom ground-truth or are limited to small spaces with optical tracking systems. We take advantage of advances in pure inertial navigation, and develop a set of versatile and challenging real-world computer vision benchmark sets for visual-inertial odometry. For this purpose, we have built a test rig equipped with an iPhone, a Google Pixel Android phone, and a Google Tango device. We provide a wide range of raw sensor data that is accessible on almost any modern-day smartphone together with a high-quality ground-truth track. We also compare resulting visual-inertial tracks from Google Tango, ARCore, and Apple ARKit with two recent methods published in academic forums. The data sets cover both indoor and outdoor cases, with stairs, escalators, elevators, office environments, a shopping mall, and metro station.


The attached supplementary video shows the ground-truth track for data set \#16 (captured in one of the two office buildings). The visualized track is the ground-truth track calculated from the entire IMU data sequence. The fix points used for track calculation are visualized by dots. The track on the current floor shows in red. The video has been sped-up.



# Details on collected data

## Ground-truth


* Ground-truth poses: Camera pose (translation and orientation) calculated based on the raw IMU data and a set of known fixation points. The ground-truth track is sampled at 100~Hz.

* Fix points: A set of ground-truth points marked with a visual editor. The points are based on the three videos stored by the system (primarily the iPhone and the second iPhone that filmed a reference track showing the capturer) and floor plan layouts.

## iPhone

* UNIX time: Time stamps aligning the internal device clock to UNIX time. Time stamp acquired through the network at beginning of each data capture.

* Camera frames: Camera frames are captured at 60~fps (1280 $\times$ 720, portrait). The exact frame acquisition times reported by the platform are stored.

* Platform location: Data collected through CoreLocation. The update rate depends on the device and its capabilities. Locations are requested with the desired accuracy of kCLLocationAccuracyBest. The timestamps are converted to follow the same clock as the other sensors (time interval since device boot). The stored values are

  * Coordinate.latitude
  * Coordinate.longitude
  * HorizontalAccuracy
  * Altitude
  * VerticalAccuracy
  * Speed


* Accelerometer: Data collected through CoreMotion/CMMotionManager. Acquired at 100 Hz, which is the maximum rate. CoreMotion reports the accelerations in 'g's (at standstill you expect to have 1~g in the vertical direction).

* Gyroscope: Data collected through CoreMotion/CMMotionManager. Acquired at 100 Hz, which is the maximum rate. Note that the readings are in the Apple device coordinate frame (not altered in any way here).

* Magnetometer: Data collected through CoreMotion/CMMotionManager. Acquired at 100 Hz, which is the maximum rate. Values are the three-axis magnetometer readings in uT. All values are uncalibrated.

* Barometric altimeter: Data collected through CoreMotion/CMAltimeter. Acquired at an uneven sampling rate ($\sim$1~Hz). Samples are stored as they arrive from the delegare callback. The actual barometric pressure is in val0 and the inferred relative altutude (calculated by Apple magic) is stored in val1.

* ARKit poses : The Apple ARKit poses (translation and orientation) are captured at 60~Hz. The camera parameters reported by ARKit on the iPhone are stored as well.

## Tango

* UNIX time: Time stamps aligning the internal device clock to UNIX time.

* Tango poses (raw): The Google Tango raw poses (translation and orientation) are captured at 60~Hz.

* Tango poses (area learning): The Google Tango area learning poses (translation and orientation) are captured at 60~Hz.

* Camera frames: Video from the wide-angle (fisheye) camera on the Tango. Captured at 30~fps / 640$\times$480.

## Pixel

* UNIX time: Time stamps aligning the internal device clock to UNIX time.

* ARCore poses: The Google ARCore poses (translation and orientation) are captured at 30~Hz.

# Dataset structure

To maximize compatibility, all data is published in open and simple file formats. The comma separated value (CSV) files hold a timestamp in the first column and the respective data in the columns that follow. All time stamps are synchronized between sensor types and devices. Camera frames are stored as H.264/MPEG video and the associated frame time stamps are available in separate CSV files. 

The folder structure for one data set looks like the following:

```
data
└───dataset01
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
└───dataset02
      ...
```




|Id|Venue|Dataset|In/Out|Stairs|Escalator|Elevator|People|Vehicles|
|---------|---------|---------|---------|---------|---------|---------|---------|---------|
|1  | Mall  | 01  | Indoor  |  | :heavy_check_mark: |  | Moderate  |
|2  | Mall  | 02  | Indoor  |  |  |  | Moderate  |
|3  | Mall  | 03  | Indoor  |  |  |  | Moderate  |
|4  | Mall  | 04  | Indoor  |  | :heavy_check_mark: |  | Moderate  |
|5  | Mall  | 05  | Indoor  | :heavy_check_mark: |  |  | Moderate  |
|6  | Mall  | 06  | Indoor  |  |  |  | High  |
|7  | Mall  | 07  | Indoor  |  |  | :heavy_check_mark: | Low  |
|8  | Mall  | 08  | Indoor  |  | :heavy_check_mark: |  | Low  |
|9  | Mall  | 09  | Indoor  |  | :heavy_check_mark: |  | Low  |
|10  | Mall  | 10  | Indoor  |  |  |  | Low  |
|11  | Metro  | 01  | Indoor  |  |  |  | High  |:heavy_check_mark:
|12  | Metro  | 02  | Indoor  |  |  |  | High  |:heavy_check_mark:
|13  | Office  | 01  | Indoor  | :heavy_check_mark: |  |  | Low  |
|14  | Office  | 02  | Indoor  | :heavy_check_mark: |  | :heavy_check_mark: | Low  |
|15  | Office  | 03  | Indoor  |  |  |  | None  |
|16  | Office  | 04  | Indoor  | :heavy_check_mark: |  |  | None  |
|17  | Office  | 05  | Indoor  | :heavy_check_mark: |  |  | None  |
|18  | Office  | 06  | Indoor  | :heavy_check_mark: |  | :heavy_check_mark: | None  |
|19  | Office  | 07  | Indoor  | :heavy_check_mark: |  |  | None  |
|20  | Outdoor | 01  | Outdoor  |  |  |  | Low  |:heavy_check_mark:
|21  | Outdoor | 02  | Outdoor  |  |  |  | Low  |:heavy_check_mark:
|22  | Outdoor (urban)  | 01  | Outdoor  |  |  |  | High  |:heavy_check_mark:
|23  | Outdoor (urban)  | 02  | Outdoor  |  |  |  | High  |:heavy_check_mark:


