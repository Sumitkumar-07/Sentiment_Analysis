# Sentiment Analysis Web App

This is a simple web application built with Streamlit that performs sentiment analysis on user-provided text reviews. The application uses a pre-trained machine learning model to predict whether the sentiment of the review is positive or negative.

## Features

- Allows users to enter their review text.
- Performs sentiment analysis and displays the result (positive or negative).
- Emojis float on the screen based on the sentiment prediction.

## Getting Started

To get started with the Sentiment Analysis Web App, follow these steps:

1. **Navigate to the project directory:**
    ```bash
    cd sentiment-analysis-web-app
    ```

2. **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3. **Run the Streamlit app:**
    ```bash
    streamlit run app.py
    ```

## Usage

To use the Sentiment Analysis Web App, follow these steps:

1. **Enter your review text** in the text input box provided.
2. **Click the "Predict" button** to see the sentiment analysis result.
3. **Emojis representing the sentiment** will float on the screen.

## Model Training

The sentiment analysis model used in this application was trained on a dataset of movie reviews. The code for training the model can be found in the `model_training.ipynb` notebook.

## Technologies Used

The following technologies were used to develop this project:

- **Python**: Programming language used for development.
- **Streamlit**: Open-source app framework for building ML and data science web apps.
- **scikit-learn**: Machine learning library for Python.
- **pickle**: Python library used for serializing and deserializing Python objects.
