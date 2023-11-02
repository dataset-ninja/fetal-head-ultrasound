**Fetal Head UltraSound** is a dataset for the measurement of fetal head circumference (HC) - an ultrasound imaging used to measure fetal biometrics during pregnancy. The dataset is a part of [HC18 challenge](https://hc18.grand-challenge.org/) and contains a total of 1334 two-dimensional (2D) ultrasound images of the standard plane that can be used to measure the HC. 

All two-dimensional (2D) ultrasound images of the HC were collected from the database of the Department of Obstetrics of the Radboud University Medical Center, Nijmegen, the Netherlands. The ultrasound images were acquired from 551 pregnant women who received a routine ultrasound screening exam between May 2014 and May 2015. Only fetuses that did not exhibit any growth abnormalities were included in this study. Images were acquired by experienced sonographers using either the Voluson E8 or the Voluson 730 ultrasound device (General Electric, Austria). The local ethics committee (CMO Arnhem-Nijmegen) approved the collection and use of this data for this study. Due to the retrospective data collection, informed consent was waived. All data was anonymized according to the tenets of the Declaration of Helsinki.

The size of each 2D ultrasound image was 800 by 540 pixels with a pixel size ranging from 0.052 to 0.326 mm. This large variation in pixel size is a result of adjustments in the ultrasound settings by the sonographer (depth settings and amount of zoom are routinely varied during the examination) to account for the different sizes of the fetuses. The size of each 2D ultrasound image was 800 by 540 pixels with a pixel size ranging from 0.052 to 0.326 mm. This large variation in pixel size is a result of adjustments in the ultrasound settings by the sonographer (depth settings and amount of zoom are routinely varied during the examination) to account for the different sizes of the fetuses. Fig. 1 shows example ultrasound images from each trimester. The distribution of the GA in this study is shown in Fig 2. Most data were acquired after 12 and 20 weeks of pregnancy since these are standard time points of routine ultrasound screening for pregnant women in the Netherlands. During each exam, the sonographer manually annotated the HC. This was done by drawing an ellipse that best fits the circumference of the head. Fig. 2 also shows the comparison between the distribution of the HC and the growth curve of [Verburg et al.](https://obgyn.onlinelibrary.wiley.com/doi/full/10.1002/uog.5225). The reference GA was determined with a CRL measurement between 20 mm (8+4 weeks) and 68 mm (12+6 weeks). All the HCs that fell outside the 3-97 percent confidence interval of the curve of [Verburg et al.](https://obgyn.onlinelibrary.wiley.com/doi/full/10.1002/uog.5225) were individually checked to ensure no mistakes were made during data collection.

![Fig 1](https://journals.plos.org/plosone/article/figure/image?size=large&id=10.1371/journal.pone.0200412.g001)

<span style="font-size: smaller; font-style: italic;">Fig. 1. Example ultrasound images.</span>

![Fig 2](https://i.ibb.co/0CVRsMk/pone-0200412-g002.png)

<span style="font-size: smaller; font-style: italic;">Fig. 2. Distribution of HC and GA for the study data.</span>

The data was randomly divided into a *train* set and a *test* set of 75 percent (999 images) and 25 percent (335 images), respectively. The GAs were proportionally balanced between the data sets as shown in Table 1. All images that were made during one echographic examination were assigned to either the training or the test set. An independent data set of HC annotations of the images in the test set was created by TLAvdH, a medical researcher who has a technical background in ultrasound imaging and received training from an experienced sonographer in measuring the HC.

|Trimester|Training Set|Testing Set|
|---------|------------|-------------|
|First|165|55|
|Second|693|233|
|Third|141|47|
|Total|999|335|

<span style="font-size: smaller; font-style: italic;">Table 1. Number of images in the training and the test set.</span>


As a result of HC18 challenge, the following fetal head circumference parameters are calculated:

``` apa
filename, center_x_mm, center_y_mm, semi_axes_a_mm, semi_axes_b_mm, angle_rad
```

![Result](https://i.ibb.co/5WXS0V3/Grand-Challange-Values-90xw-KFs.png)
