from darknet.darknet import *
from IPython.display import display, Javascript, Image
from base64 import b64decode, b64encode
import cv2
import numpy as np
import PIL
import io
import html
import time
import matplotlib.pyplot as plt
import imutils
import pytesseract



def img_to_text(img):
    text = pytesseract.image_to_string(img ,lang='eng', config='--psm 13 --oem 1 -c tessedit_char_whitelist=ABCDEFG0123456789')
    return text

# load in our YOLOv4 architecture network
def detect(path,crops_path):
    network, class_names, class_colors = load_network("cfg/yolov4_custom_test.cfg", "cfg/obj.data", "cfg/yolov4_custom_train_last.weights")
    width = network_width(network)*2
    height = network_height(network)*2

    img = cv2.imread(path)
    darknet_image = make_image(width, height, 3)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img_resized = cv2.resize(img_rgb, (width, height),
                              interpolation=cv2.INTER_LINEAR)
    # get image ratios to convert bounding boxes to proper size
    img_height, img_width, _ = img.shape
    width_ratio = img_width/width
    height_ratio = img_height/height

    copy_image_from_bytes(darknet_image, img_resized.tobytes())
    print('detecting')
    detections = detect_image(network,class_names,darknet_image)
    box = detections
    n = len(os.listdir(crops_path))
    for i,x in enumerate(box):
        print(x)
        x = int(box[i][2][0])
        y = int(box[i][2][1])
        w = int(box[i][2][2])
        h = int(box[i][2][3])
        p = 20
        crop = img_resized[int(y-h/2-p):int(y+h/2+p),int(x-w/2-p):int(x+w/2+p)]
        cv2.imwrite(os.path.join(crops_path , 'crop_{}.png'.format(n+i)),crop)
    return len(box)
   