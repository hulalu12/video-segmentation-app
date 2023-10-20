# video-segmentation-app
This tool can remove the background surrounding a person. This functionality can be utilized to develop an application or software that removes backgrounds.


## Overview

![Alt text](.images/image.jpg)


## BR5K Dataset
Considering that the misuse of the dataset may lead to ethical concerns, as recommended by AC, we will review the application to access the datasets. To be able to download the BR5K database, please download, sign the [agreement form](https://raw.githubusercontent.com/JianqiangRen/FlowBasedBodyReshaping/main/EULA/EULA0310.pdf), and then use your work e-mail(e.g., xx@xx.edu.cn,  xx@your_company.com) to send the form to ([jianqiang.rjq@alibaba-inc.com](jianqiang.rjq@alibaba-inc.com)).

## Getting Started
### Data
* Download the example data from [google drive](https://drive.google.com/drive/folders/1G7XXEgMHpHnSkvFRVX5iJqN7sk3VjoM4?usp=sharing). I selected this data because there is a high contrast between the person and the background, and the model is working almost perfectly well.
* Put data into the `data` folder.

### Model
* Download the model from [google drive](https://drive.google.com/drive/folders/1B-1mUylAErxEESELRQYs-nFq6LNzGpKw?usp=sharing).
* Put video-seg.pt into the `model` folder.


### Run the Demo


    python run.py

 the results will be in the test_cases_output directory.



## Fine tuning
To fine tune the model took an image make a segmentation mask around it.
 

