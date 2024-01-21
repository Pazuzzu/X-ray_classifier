# Overview
This project involves training a simple Convolutional Neural Network (CNN) to classify X-ray images using Kaggle data.

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

![alt text](https://github.com/Pazuzzu/X-ray_classifier/tree/main/assets/landing_screenshot.png?raw=true)