# tensorflow-gun-detection

### Instructions
  - Uncompress the train & test images
    - Images inside data/images/processed are compressed into train.tar.gz and test.tar.gz folders.
    - Navigate to data/images/processed folder and type "bash uncompress.sh" in your terminal.

  - Create csv records for the xml files
    - Navigate to data/images/processed and run xml_to_csv.py file


### utils/image_resizer.py
  - usage
    - python image_resizer.py -input=input_folder_images -output=output_folder -height=800 -width=600


### Notes:
  - To compress the images which are inside train & test folders inside data/images/processed
    - tar -cvzf train.tar.gz train
    - tar -cvzf test.tar.gz test

  - Rectlabel App in Mac / LabelImg open source:
    - The bounding boxes around the images were created using Rectlabel tool available for MAC.
    - We can also use Labelimg open source tool for this task.


### References:
  - Modified version of xml_to_csv.py from racoon github repo.
  - generate_tfrecord.py from racoon github repo.
