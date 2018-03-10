# tensorflow-gun-detection

### Instructions
  - Uncompress the train & test images
    - Images inside data/images/processed are compressed into train.tar.gz and test.tar.gz folders.
    - Navigate to data/images/processed folder and type "bash uncompress.sh" in your terminal.


### utils/image_resizer.py
  - usage
    - python image_resizer.py -input=input_folder_images -output=output_folder -height=800 -width=600


### Notes:
  - To compress the images which are inside train & test folders inside data/images/processed
    - tar -cvzf train.tar.gz train
    - tar -cvzf test.tar.gz test
