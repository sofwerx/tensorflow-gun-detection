# tensorflow-gun-detection

### Scores
| Model          | Mobile SSD | Faster RCNN |
|----------------|------------|-------------|
| Test Loss      | 1.5        | 0.1016      |
| Trained Rounds | 5114       | 7167        |  

### Instructions
  - Uncompress the train & test images
    - Images inside images are compressed into train.tar.gz and test.tar.gz folders.
    - Navigate to images folder and type "bash uncompress.sh" in your terminal.

  - Create csv records for the xml files
    - Navigate to images and run xml_to_csv.py file

  - Create tfrecords
    - Navigate to images and see the generate_tfrecords.py script for instructions.

  - Once you generate xml files and tfrecords, the files should be available under images/data
  - Create a folder called training in the root folder.
  - If you want to do transfer learning pull the model & config files from tensorflow zoo and put the in the root folder.
  - Move the config file to training/ folder and change the config file to match the paths.
  - To train the model:
    - python train.py --logstderr --train_dir=training/ --pipeline_config_path=training/ssd_mobilenet_v1_pets.config
  - Export inference graphs
  - Paste the graph folders to outputs/ folder
  - Count the no.of bounding boxes
    - python image_detection.py


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
