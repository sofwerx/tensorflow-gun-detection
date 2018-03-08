import argparse, glob, os
import cv2
from shutil import copyfile

parser = argparse.ArgumentParser(description="Pass inputs")
parser.add_argument("-input","--input_dir", required=True,
    help="path to the input directory containing images")
parser.add_argument("-output","--output_dir", required=True,
    help="path to the output directory to store images")
args = vars(parser.parse_args())


# create output folder if it doesnot exist
if not os.path.exists(args["output_dir"]):
    os.makedirs(args["output_dir"])

def get_image_paths(input_dir, output_path):
    annotations_folder = os.path.join(input_dir, "annotations")
    image_names_all = []
    for (dirpath, dirnames, image_names) in os.walk(input_dir):
        image_names = sorted([img for img in image_names
                if any([ext in img for ext in (".bmp", ".jpg", ".jpeg", ".png",
                    ".tif", ".tiff")]) ])
        image_names_all.extend(image_names[:])

    annotations_dir = os.path.join(input_dir, "annotations")
    xml_names = [xml_names
        for (dirpath, dirnames, xml_names) in os.walk(annotations_dir)][0]

    xml_names = [xml for xml in xml_names]

    in_s = []
    outs = []

    for img in image_names_all:
        if img.split(".")[0] in [xml.split(".")[0] for xml in xml_names]:
            in_s.append(img)

            imagepath = os.path.join(input_dir, img)
            xmlpath = os.path.join(input_dir, "annotations", imagepath.split("/")[-1].split(".")[0] +'.xml')

            print(imagepath)
            print(xmlpath)

            img_out_path = os.path.join(output_path, imagepath.split("/")[-1])
            xml_out_path = os.path.join(output_path, img.split(".")[0] +'.xml')

            copyfile(imagepath, img_out_path)
            copyfile(xmlpath, xml_out_path)






get_image_paths(args["input_dir"], args["output_dir"])
