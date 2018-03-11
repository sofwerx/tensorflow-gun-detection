import os
import glob
import pandas as pd
import xml.etree.ElementTree as ET


def xml_to_csv(path):
    xml_list = []
    for xml_file in glob.glob(path + '/*.xml'):
        tree = ET.parse(xml_file)
        root = tree.getroot()
        for member in root.findall('object'):
            bndbox = member.find("bndbox")
            value = (root.find('filename').text,
                     int(root.find('size')[0].text),
                     int(root.find('size')[1].text),
                     member.find("name").text,
                     int(bndbox.find("xmin").text),
                     int(bndbox.find("ymin").text),
                     int(bndbox.find("xmax").text),
                     int(bndbox.find("ymax").text)
                     )
            xml_list.append(value)
    column_name = ['filename', 'width', 'height', 'class', 'xmin', 'ymin', 'xmax', 'ymax']
    xml_df = pd.DataFrame(xml_list, columns=column_name)
    return xml_df


def main():
    for directory in ["train", "test"]:
    	image_path = os.path.join(os.getcwd(), directory)
   	xml_df = xml_to_csv(image_path)
        output_dir = os.path.join(os.getcwd(), "data")
	if not os.path.exists(output_dir):
	    os.makedirs(output_dir)
    	xml_df.to_csv("data/{}_labels.csv".format(directory), index=None)
    	print('Successfully converted xml to csv.')


main()
