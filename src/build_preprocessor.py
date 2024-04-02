
import click
import pandas as pd
import os
from sklearn.pipeline import make_pipeline
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.dummy import DummyClassifier
from sklearn.compose import make_column_transformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.metrics import classification_report
from sklearn.preprocessing import OrdinalEncoder
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import RandomizedSearchCV
from scipy.stats import randint

def build_preprocessor(numerical_data, text_data, categorical_data):
    """_summary_
    Builds a preprocessor for numerical, text, and categorical data 
    Args:
        numerical_data (_type_): numeric data
        text_data (_type_): text data 
        categorical_data (_type_): cateogorical data 

    Returns:
        _type_: _description_
    """
    # Numerical Transformer
    numerical_transformer = StandardScaler()

    # Categorical Transformer
    categorical_transformer = OneHotEncoder(handle_unknown='ignore')

    # Text Data Transformer
    text_transformer = CountVectorizer()
    
    # Making Our Preprocessor
    preprocessor = make_column_transformer(
        (numerical_transformer, numerical_data),
        (categorical_transformer, categorical_data),
        (text_transformer, text_data),
        remainder='drop'
    )
    
    return preprocessor