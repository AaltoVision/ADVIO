# Calibration data

The ADVIO data was collected in four batches, and the calibrations were done for each batch separately. The rows correspond to the different batches (the sequence numbers refer to the data sets). This same information is also available in machine-readable form.

# iPhone camera

| Sequences  |f<sub>x |f<sub>y |c<sub>x |c<sub>y |r<sub>1 |r<sub>2 |k<sub>1 |k<sub>2 |
| ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- |
| 1-12 |1077.2| 1079.3|362.14| 636.39|0.0478| 0.0339| -0.0003|-0.0009|
| 13-17|1082.4| 1084.4|364.68| 643.31|0.0366| 0.0803| 0.0007|-0.0002|
| 18-19|1076.9| 1078.5|360.96| 639.31|0.0510| -0.0354| -0.0054|0.0473|
| 20-23|1081.1|1082.1|359.59|640.79|0.0556|-0.0454|0.0009|-0.0018|
  
## iPhone IMU (approximate) additive biases

| Sequences  |acc<sub>x |acc<sub>y |acc<sub>x |gyr<sub>x |gyr<sub>y |gyr<sub>z |
| ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- |
| 1-12 |0.0407| -0.0623|0.1017| -0.0067|0.0070| -0.0065|
| 13-17|0.0415| -0.0617|0.1008| -0.0065|0.0055| -0.0064|
| 18-19|0.0393| -0.0635|0.1024| -0.0069|0.0062| -0.0067|
| 20-23|0.0405| -0.0620|0.1012| -0.0066|0.0065| -0.0063|

## iPhone camera to IMU transformation

Calibration performed with the [Kalibr](https://github.com/ethz-asl/kalibr) toolbox. Very stable, assumed the same for all sequences.

|  |  |  |  |
| ------------- | ------------- | ------------- | ------------- |
|0.9999763379093255|-0.004079205042965442|-0.005539287650170447|-0.008977668364731128|
|-0.004066386342107199|-0.9999890330121858|0.0023234365646622014|0.07557012320238939|
|-0.00554870467502187|-0.0023008567036498766|-0.9999819588046867|-0.005545773942541918|
|0.0|0.0|0.0|1.0|


