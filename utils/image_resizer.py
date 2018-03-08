import argparse
import glob
import os

import cv2
from imutils import paths

parser = argparse.ArgumentParser(description="Pass inputs")
parser.add_argument("-input","--input_dir", required=True,
    help="path to the input directory containing images")
parser.add_argument("-output","--output_dir", required=True,
    help="path to the output directory to store images")
parser.add_argument("-height", "--height", required=True,
    help="required height to resize")
parser.add_argument("-width", "--width", required=True,
    help="required width to resize")
args = vars(parser.parse_args())

def get_value(dim):
    if args.get(dim) is not None:
        try:
            return int(args.get(dim))
        except TypeError:
            return None
        except ValueError:
            return None
    else:
        return None

required_height = get_value("height")
required_width = get_value("height")
input_path = args["input_dir"]
output_path = args["output_dir"]

if required_height is None or required_width is None:
    print("Please pass height and weight")
    sys.exit()


print(output_path)

# create output folder if it doesnot exist
if not os.path.exists(output_path):
    os.makedirs(output_path)

def resize_image(image, width=None, height=None, inter=cv2.INTER_AREA):
    """
    resize the image without distorting it,
    using the width, height cmds entered at command line.

    interpolation docs = https://docs.opencv.org/3.0-beta/modules/imgproc/doc/geometric_transformations.html?highlight=resize#cv2.resize
    """
    dimensions = None
    img_height, img_width, channels = image.shape

    if width is None and height is None:
        return image
    elif width is None:
        ratio = height / float(img_height)
        dimensions = (int(img_width * ratio), height)
    else:
        ratio = width / float(img_width)
        dimensions = (width, int(img_height * ratio))

    resized_img = cv2.resize(image, dimensions, interpolation=inter)
    return resized_img
    # return cv2.resize(image, (required_width, required_height))


for (dirpath, dirnames, image_names) in os.walk(input_path):
    # remove images with invalid extension
    image_names = sorted([img for img in image_names
            if any([ext in img for ext in (".bmp", ".jpg", ".jpeg", ".png",
                ".tif", ".tiff")]) ])

    # loop through each image, get the dimensions
    #      compare with the cmd height,width passed and resize.
    for img_path in image_names:
        imagepath = os.path.join(dirpath, img_path)

        image = cv2.imread(imagepath)
        try:
            height, width, channels = image.shape
            if height > required_height or width > required_width:
                image = resize_image(image, required_width, required_height)
            # Write the image to output directory
            img_out_path = os.path.join(output_path, img_path)

            cv2.imwrite(img_out_path, image)
        except AttributeError:
            print("Cannot process image: ", img_path)
