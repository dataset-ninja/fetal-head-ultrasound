During pregnancy, ultrasound imaging is used to measure fetal biometrics. One of these measurements is the fetal head circumference (HC). The HC can be used to estimate the gestational age and monitor growth of the fetus. The HC is measured in a specific cross section of the fetal head, which is called the standard plane.

*Fetal Head UltraSound* is dataset for [HC18 challenge](https://hc18.grand-challenge.org/) and it contains a total of 1334 two-dimensional (2D) ultrasound images of the standard plane that can be used to measure the HC.

The data is divided into a *train* set of 999 images and a *test* set of 335 images. The size of each 2D ultrasound image is 800 by 540 pixels with a pixel size ranging from 0.052 to 0.326 mm. The *train* set also includes an image with the manual annotation of the head circumference for each HC, which was made by a trained sonographer. 

As a result of HC18 challenge, the following fetal head circumference parameters are calculated:

``` apa
filename,center_x_mm,center_y_mm,semi_axes_a_mm,semi_axes_b_mm,angle_rad
```

![Result](https://i.ibb.co/5WXS0V3/Grand-Challange-Values-90xw-KFs.png)
