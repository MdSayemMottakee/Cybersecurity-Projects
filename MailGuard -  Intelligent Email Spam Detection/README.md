# MailGuard: Intelligent Email Spam Detection

## Overview
**MailGuard** is a machine learning-based system that classifies emails as **spam** or **ham (not spam)**. It uses **NLP preprocessing** and an **SVM classifier** with TF-IDF features to detect spam emails effectively. The goal is to improve inbox security by filtering unwanted or malicious messages.

This project uses the dataset from Kaggle: [Spam Mails Dataset by venky73](https://www.kaggle.com/datasets/venky73/spam-mails-dataset?resource=download).

---

## Dataset
The dataset contains:  
- `text`: Email content including subject line  
- `label`: Categorical label (`spam` or `ham`)  
- `label_num`: Numeric label (`0` = ham, `1` = spam)  

> Note: Only email body text is included; email header analysis is not used.

---

## Project Workflow

### 1. Data Preprocessing
- Convert text to lowercase  
- Replace email addresses, URLs, phone numbers, and numbers with placeholders  
- Remove punctuation, extra spaces, and stopwords  
- Compute `length` and `clean_length` for message analysis  

### 2. Exploratory Data Analysis (EDA)
- Visualize message length distributions for spam vs. ham  
- Generate WordClouds to identify frequent words in spam and ham emails  

### 3. Feature Extraction
- Convert email text into numerical features using **TF-IDF vectorization**  

### 4. Model Training
- Train a **Support Vector Machine (SVM)** classifier  
- Split data into training and testing sets  
- Evaluate performance with accuracy, precision, recall, F1-score, and confusion matrix  

### 5. Model Evaluation
- Display metrics and confusion matrix for spam detection performance  
- Save trained model using `pickle` for future predictions  

---

## Results
- The SVM classifier achieves high accuracy in distinguishing spam from ham emails  
- WordClouds provide insights into common words used in spam and ham messages  
- Cleaned and preprocessed text improves model performance  
