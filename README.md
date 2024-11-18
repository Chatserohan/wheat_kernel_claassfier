Here's a basic README file for your project:

---

# Wheat Kernel Classifier

This project uses machine learning to classify wheat kernels based on features like area, perimeter, and compactness. The model is built using **Logistic Regression** and **Flask** for the web application. The dataset is a set of measurements of wheat kernels, and the goal is to predict the target class based on these features.

## Requirements
- Python 3.x
- Flask
- pandas
- numpy
- scikit-learn

You can install the required packages using pip:
```
pip install pandas numpy scikit-learn flask
```

## Project Structure
```
/wheat_kernel_classifier
│
├── app.py               # Flask web application
├── seeds_dataset.txt    # Input dataset (text file with kernel measurements)
├── output_dataset.csv   # Processed dataset
├── wheat_kernel_classifier.pkl  # Trained model (Pickle file)
├── README.md            # Project documentation
└── requirements.txt     # List of Python dependencies
```

## Dataset
The dataset contains several features related to the dimensions of wheat kernels, including:
- Area (area_A)
- Perimeter (perimeter_P)
- Compactness (compactness_c)
- Length and Width of the kernel
- Asymmetry coefficient and more...

## How It Works
1. **Data Processing**: The `.txt` file containing the raw data is loaded and processed using pandas. It is then saved as a CSV file for further analysis.
2. **Model Training**: The dataset is split into training and test sets. Logistic Regression is used to train a model to predict the target variable (kernel type).
3. **Model Export**: The trained model is saved as a `.pkl` file using pickle, for use in the Flask web app.

## Flask Web App
The Flask app loads the trained model and exposes an endpoint for making predictions based on user input. 

## How to Run
1. Clone the repository:
   ```
   git clone <repo-url>
   cd wheat_kernel_classifier
   ```
2. Run the Flask application:
   ```
   python app.py
   ```
3. Access the web app on `http://127.0.0.1:5000` in your browser.

## Example Prediction
To predict the type of a wheat kernel, input the following features (for example):
```
[15.11, 14.54, 0.8986, 5.579, 3.462, 3.128, 5.180]
```
This will return the predicted class for the wheat kernel based on the model.

## Accuracy
The model's accuracy on the test set is displayed after training:
```
Accuracy: 1.00
```
##Project by
Name: Rohan Chatse 
Email: rohancrchatse@gmail.com
