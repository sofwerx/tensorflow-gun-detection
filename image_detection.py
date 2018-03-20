# Current progress
# Counts the no.of bounding boxes

import csv, os

import cv2
import tensorflow as tf
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

from utils import label_map_util

# Frozen inference graph path + checkpoint path
MODEL_PATHS = ['./outputs/ssd_mobile/ssd_mobile/ssd_mobile_graph_output', \
    './outputs/faster_rcnn/faster_rcnn_inception_v2_graph_output']

MODEL_TRAINING_PATHS = ['./outputs/ssd_mobile/ssd_mobile/training', \
    './outputs/faster_rcnn/training'
    ]

for model_path, model_tr_path in zip(MODEL_PATHS, MODEL_TRAINING_PATHS):
    MODEL_NAME = model_path
    PATH_TO_CKPT = MODEL_NAME + '/frozen_inference_graph.pb'
    PATH_TO_LABELS = os.path.join(model_tr_path, 'object-detection.pbtxt')

    output_path = "./outputs/" + model_tr_path.split("/")[2] + "_bounding_boxes_count.csv"

    NUM_CLASSES = 1
    MIN_SCORE_THRESHOLD =  0.5
    # Load the frozen inference graph

    detection_graph = tf.Graph()
    with detection_graph.as_default():
        graphDef = tf.GraphDef()

        # load the graph from disk
        with tf.gfile.GFile(PATH_TO_CKPT, "rb") as f:
            serializedGraph = f.read()
            graphDef.ParseFromString(serializedGraph)
            tf.import_graph_def(graphDef, name="")


    # Load class labels - label map
    label_map = label_map_util.load_labelmap(PATH_TO_LABELS)
    categories = label_map_util.convert_label_map_to_categories(label_map, max_num_classes=NUM_CLASSES, use_display_name=True)
    category_index = label_map_util.create_category_index(categories)

    # Helper code
    def load_image_into_numpy_array(image):
        (im_width, im_height) = image.size
        return np.array(image.getdata()).reshape(
              (im_height, im_width, 3)).astype(np.uint8)

    # Input images path
    PATH_TO_VAL_IMAGES_DIR = './images/validation/'
    #VALIDATION_IMAGES_PATH = [ os.path.join(PATH_TO_VAL_IMAGES_DIR, 'image{}.jpg'.format(i)) for i in range(1, 300) ]

    bounding_box_count = csv.writer(open(output_path,"w"))
    bounding_box_count.writerow(["img_name","bnd_bx_count"])
    val_images = []

    for (dirpath, dirnames, image_names) in os.walk(PATH_TO_VAL_IMAGES_DIR):
        for img in image_names:
            if any([ext in img for ext in (".bmp", ".jpg", ".jpeg", ".png",
                ".tif", ".tiff")]):
                val_images.append(os.path.join(PATH_TO_VAL_IMAGES_DIR, img))

    val_images = sorted(val_images)

    # Size, in inches, of the output images.
    IMAGE_SIZE = (12, 8)

    with detection_graph.as_default():
        with tf.Session(graph=detection_graph) as sess:
            # get the references of the input image tensor + boxes tensor
            image_tensor = detection_graph.get_tensor_by_name("image_tensor:0")
            detection_boxes = detection_graph.get_tensor_by_name("detection_boxes:0")

            # for each bounding box, find the socre, class and image label
            detection_scores = detection_graph.get_tensor_by_name("detection_scores:0")
            detection_classes = detection_graph.get_tensor_by_name("detection_classes:0")
            num_detections = detection_graph.get_tensor_by_name("num_detections:0")

            for img_path in val_images:
                try:
                    image = Image.open(img_path)
                    image_np = load_image_into_numpy_array(image)
                    image_np_expanded = np.expand_dims(image_np, axis=0)  # Expand dimensions since the model expects images to have shape: [1, None, None, 3]
                    # Detection Parth
                    (boxes, scores, classes, num) = sess.run(
                        [detection_boxes, detection_scores, detection_classes, num_detections],
                         feed_dict={image_tensor: image_np_expanded})

                    boxes = np.squeeze(boxes)
                    scores = np.squeeze(scores)
                    classes = np.squeeze(classes)

                    count = 0
                    for i in range(100):
                        # mAP > 0.5? - 0.5 is considered the minimal good score
                        if scores is None or scores[i] > MIN_SCORE_THRESHOLD:
                            count = count + 1
                    bounding_box_count.writerow([img_path.split("/")[-1], count])
                except FileNotFoundError:
                    print("cant find image")
