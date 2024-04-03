import sys
import os
from sklearn.dummy import DummyClassifier
from sklearn.compose import ColumnTransformer,make_column_transformer
import pytest
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.feature_extraction.text import CountVectorizer
import click
import pandas as pd
import numpy as np
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.function_build_preprocessor import build_preprocessor


def test_preprocessor_type():
    """Test that the function returns a ColumnTransformer object."""
    numerical_data = ['numerical']
    text_data = 'text'
    categorical_data = ['category']
    
    preprocessor = build_preprocessor(numerical_data, text_data, categorical_data)
    assert isinstance(preprocessor, ColumnTransformer)

def test_transformer_assignment():
    """Test that the correct transformers are assigned to the specified types of data."""
    preprocessor = build_preprocessor(['num'], ['text'], ['cat'])
    transformers = {name: type(trans) for name, trans, cols in preprocessor.transformers}
    
    assert transformers.get('standardscaler') == StandardScaler
    assert transformers.get('onehotencoder') == OneHotEncoder
    assert transformers.get('countvectorizer') == CountVectorizer

def test_preprocessor():
    # Create an artificial dataset
    np.random.seed(0)  # For reproducibility
    data = pd.DataFrame({
        'numerical': np.random.randn(100),
        'text': np.random.choice(['First text', 'Text number 2', 'Third sentence of text'], size=100),
        'category': np.random.choice(['A', 'B', 'C'], size=100),
        'target': np.array([0]*90 + [1]*10)  # target variable made with 90 zeros and 10 1s, meaning dummy classifier should predict 0 everytime
    })
    
    # Split the dataset
    X_train, X_test, y_train, y_test = train_test_split(
        data.drop('target', axis=1), data['target'], test_size=0.25, random_state=42)
    
    # Define columns
    numerical_data = ['numerical']
    text_data = 'text'
    categorical_data = ['category']
    
    # Build the preprocessor
    preprocessor = build_preprocessor(numerical_data, text_data, categorical_data)
    
    # combine preprocessor with a dummymodel with strategy most frequent
    model = make_pipeline(preprocessor, DummyClassifier(strategy='most_frequent'))
    
    # Fit the model
    model.fit(X_train, y_train)
    
    # Make predictions and evaluate
    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)
    
    print(f"Dummy Classifier Accuracy: {accuracy:.4f}")
    
    assert accuracy >= 0.5, "Accuracy should be at least 0.5"
    



test_preprocessor()