# Overview

This repository contains source code for cars' plates detection and recognition, which can be applied for both video and image data.
Here is an example:



On the first stage we have detect() function working to put bounding box of the plate and crop the result:

<img src='images/9.jpeg' width=320 height=480>  <img src='images/crop_11.png' width=320 height=480>

On the next stage we use adjust_perspective() to bring plate back to straight look:

<img src='images/adjusted.png' width=375 height=94>

# Technical details:

* YOLO v4 is used as a detector pretrained on Car plates dataset (ypu can find it if /data folder.
* We use trained Net to segment number in order to find the nodes.
* 3rd stage includes OpenCV algo to adjust perspective. 
* Last stage consits of using any library (like pytesseract) to convert straight plate image into string.

* As postprocessing of YOLO output takes a long time (~30-40 seconds for one image on local machine) for all 500 classes I selected only food-related classes (59 classes) information from entire output tensor and sent it to postprocessing block. This procedure decreases processing time to 5-6 seconds per image.
* YOLO detector is not very accurate, so replacing it with another one (for example, from R-CNN family) or training on larger and more diverst dataset could improve its performance. But excellent performance was not my goal in this pet-project.

# Usage
0. Download this repo in your working directory. 
1. Type in command line _pip install -r requirements.txt_ from calorie_counter directory. 
1. Download pretrained weights for YOLO v3 from this [link](https://github.com/radekosmulski/yolo_open_images).
2. Convert Darknet model to Keras using this [link](https://github.com/qqwweee/keras-yolo3).
3. Put converted model with _.h5_ extention in calorie_counter/bot/model folder.
4. From command line or IDE run _main.py_ file.
5. Done! Your bot is working!

## Other resources
https://github.com/experiencor/keras-yolo3
