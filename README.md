# Overview
This project aims to classify received MRI images from patients and organize them into appropriate archive folders. In this project, I train a small Convolutional Neural Network (CNN) to classify X-ray images using Kaggle data and deploy it on Streamlit.

## Setup
```pip install -r requirements.txt```

## Data Processing
1. Fill in the "kaggle.json" file with your Kaggle API token information.
2. Run the "xray_classifier_data.ipynb" notebook to download and process data

## Model Training
1. Run ```export WANDB_API_KEY=XXXXXXXXX```
2. Run the notebook "xray_classifier_model.ipynb" notebook, to train the model.

## Inference
Run Streamlit server:
```streamlit run app.py```

<p align="center">
  <img src="https://github.com/Pazuzzu/X-ray_classifier/blob/main/assets/landing_screenshot.png?raw=true" alt="Classifier GUI"/>
</p>

### Credits
Credits to the Kaggle dataset repos:
- [paultimothymooney/chest-xray-pneumonia](https://www.kaggle.com/datasets/paultimothymooney/chest-xray-pneumonia)
- [nazmul0087/ct-kidney-dataset-normal-cyst-tumor-and-stone](https://www.kaggle.com/datasets/nazmul0087/ct-kidney-dataset-normal-cyst-tumor-and-stone/data)
- [abdulkader90/brain-ct-hemorrhage-dataset](https://www.kaggle.com/datasets/abdulkader90/brain-ct-hemorrhage-dataset)
- [nikhilroxtomar/ct-heart-segmentation](https://www.kaggle.com/datasets/nikhilroxtomar/ct-heart-segmentation)
- [shashwatwork/knee-osteoarthritis-dataset-with-severity](https://www.kaggle.com/datasets/shashwatwork/knee-osteoarthritis-dataset-with-severity)
