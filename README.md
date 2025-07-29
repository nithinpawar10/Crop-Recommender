# SowEasy (Crop-Recommender)

## Overview
Crop recommendation is a crucial aspect of precision farming. In agriculture, it is critical that the recommendations made are correct and precise, as errors can result in significant material and capital loss. The project uses Streamlit to create an intelligent web application that helps farmers accomplish the following goals:

* 🌾 Increase agricultural production efficiency
* 🧪 Decrease the usage of harmful chemicals in crop production
* 💧 Maximize the effectiveness of water resources
* 🌱 Prevent soil degradation in cultivated land

## Features
This Application recommends the best crop to plant based on:
- **Nitrogen (N)** content in soil
- **Phosphorus (P)** content in soil  
- **Potassium (K)** content in soil
- **Temperature** conditions
- **Humidity** levels
- **pH** level of soil
- **Rainfall** measurements

## Machine Learning Models
The application uses multiple trained machine learning models for accurate predictions:
- **Logistic Regression** - Linear classification approach
- **Decision Tree** - Rule-based classification with entropy criterion
- **Naive Bayes** - Gaussian probabilistic classifier
- **Random Forest** - Ensemble method with 20 estimators
- **Support Vector Machine (SVM)** - Polynomial kernel with degree 3

## Tech Stack
- **Frontend**: Streamlit
- **Backend**: Python
- **Machine Learning**: Scikit-learn
- **Data Analysis**: Pandas, NumPy
- **Visualization**: Matplotlib, Seaborn
- **Model Persistence**: Pickle

## Dataset
The model was trained on a comprehensive crop recommendation dataset containing 2200 samples with various soil and climate parameters. 

**Dataset Link**: https://www.kaggle.com/datasets/atharvaingle/crop-recommendation-dataset

## Live Demo
**App Link**: https://soweasy.streamlit.app/

## Installation & Setup

### Prerequisites
- Python 3.7 or higher
- pip package manager

### Step 1: Clone the Repository
```bash
git clone https://github.com/nithinpawar10/Crop-Recommender.git
cd Crop-Recommender
```

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 3: Run the Application
```bash
streamlit run crop-webapp.py
```

The application will start running on `http://localhost:8501`

## File Structure
```
SowEasy_Crop-Recommender/
│
├── crop-webapp.py              # Main Streamlit application
├── crop_model.py               # Model training script
├── retrain_model.py            # Individual model retraining
├── retrain_all_models.py       # Batch model retraining
├── Crop_Recommendation_(EDA).ipynb  # Exploratory Data Analysis
├── Crop_recommendation.csv     # Dataset
├── requirements.txt            # Python dependencies
├── cc.jpg                      # Application logo/image
├── DecisionTree_model.pkl      # Trained Decision Tree model
├── LogReg_model.pkl           # Trained Logistic Regression model
├── NaiveBayes_model.pkl       # Trained Naive Bayes model
├── RF_model.pkl               # Trained Random Forest model
└── README.md                  # Project documentation
```

## How to Use
1. Open the application in your web browser
2. Enter the soil parameters (N, P, K values)
3. Input environmental conditions (temperature, humidity, pH, rainfall)
4. Click on the prediction button
5. Get your personalized crop recommendation

## Model Performance
The models have been evaluated and compared for accuracy. The Random Forest classifier shows the best performance among all implemented algorithms.

## Contributing
Feel free to fork this repository and submit pull requests for any improvements.

## License
This project is open source and available under the MIT License.

 

 

