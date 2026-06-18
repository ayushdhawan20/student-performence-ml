Student Performance Predictor
Overview

Student Performance Predictor is a beginner-friendly Machine Learning project developed using Python and Scikit-Learn. The project predicts whether a student is likely to Pass or Fail based on key academic factors such as attendance, study hours, and marks.

This project demonstrates the basic Machine Learning workflow, including data collection, model training, prediction, and evaluation.

Features
Predicts student performance (Pass/Fail)
Uses a Machine Learning Decision Tree Classifier
Simple and easy-to-understand implementation
Beginner-friendly project for Data Science learners
Command-line based prediction system
Technologies Used
Python
Pandas
Scikit-Learn
Pickle
Project Structure
student-performance-ml/
│
├── data.csv
├── train.py
├── predict.py
├── model.pkl
├── requirements.txt
└── README.md
Dataset

The dataset contains the following features:

Feature	Description
attendance	Student attendance percentage
study_hours	Daily study hours
marks	Internal examination marks
result	Pass or Fail
Machine Learning Algorithm

The project uses a Decision Tree Classifier from Scikit-Learn to learn patterns from student data and make predictions.

Installation
1. Clone the Repository
git clone https://github.com/your-username/student-performance-ml.git
cd student-performance-ml
2. Install Dependencies
pip install -r requirements.txt
Training the Model

Run the following command:

python train.py

Output:

Model Trained Successfully!

A trained model file named model.pkl will be generated.

Making Predictions

Run:

python predict.py

Example:

Enter Attendance (%): 85
Enter Study Hours: 3
Enter Marks: 75

Prediction: Pass
Learning Outcomes

Through this project, I learned:

Data preprocessing using Pandas
Training Machine Learning models
Decision Tree Classification
Model serialization using Pickle
Making predictions using trained models
Basic Data Science workflow
Future Improvements
Add a graphical user interface using Streamlit
Increase dataset size for better accuracy
Add visualization and analytics dashboards
Predict multiple performance categories instead of Pass/Fail
Author

Ayush Dhawan

BCA Student (2024–2027) | Aspiring Data Scientist

Skills: Python, Data Science, Machine Learning, Power BI, Excel
