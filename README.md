# Emotion Detection App 

A Machine Learning web app that predicts the emotion behind a given text using **Natural Language Processing (NLP)**.

This project uses **TF-IDF Vectorization** for text feature extraction and a **Logistic Regression model** for emotion classification. The web app is built using **Streamlit**.

##  Live Demo

Try the deployed app here:

[https://your-streamlit-app-link.streamlit.app/](https://emotionpredictor-app.streamlit.app/)


##  Project Overview

The Emotion Detection App takes text input from the user and predicts the emotion expressed in the sentence.

The app can classify text into the following emotions:

- Sadness
- Anger
- Love
- Surprise
- Fear
- Joy

##  Dataset

The dataset used in this project was taken from **Kaggle**.

Dataset name:

```txt
Emotions Dataset for NLP
```

This dataset was used to train the machine learning model for emotion classification.

##  Machine Learning Model

The final model used in this project is:

```txt
Logistic Regression
```

Logistic Regression is a supervised machine learning algorithm used for classification problems.

In this project, it is used to classify text into different emotion categories.

##  Model Accuracy

The best model achieved an accuracy of:

```txt
86.16%
```

Model performance:

| Feature Extraction | Model | Accuracy |
|---|---|---|
| Bag of Words | Naive Bayes | 76.78% |
| TF-IDF | Naive Bayes | 66.09% |
| TF-IDF | Logistic Regression | 86.16% |

Therefore, **TF-IDF with Logistic Regression** was selected as the final model.

##  Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Natural Language Processing
- TF-IDF Vectorizer
- Logistic Regression
- Streamlit
- Joblib
- GitHub

This project was created as a beginner-friendly NLP and Machine Learning project to understand text classification, TF-IDF vectorization, Logistic Regression, model evaluation, and deployment using Streamlit.
