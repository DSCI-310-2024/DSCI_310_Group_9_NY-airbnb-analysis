
import sys
import os
from sklearn.dummy import DummyClassifier
from sklearn.compose import ColumnTransformer,make_column_transformer
import pytest
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.datasets import make_classification
from sklearn.neighbors import KNeighborsClassifier

import click
import pandas as pd
import numpy as np
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
# sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.build_model import build_clf_model




@pytest.fixture
def data():

    X, y = make_classification(n_samples=100, n_features=4, n_informative=2, n_redundant=0, random_state=42)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    return X_train, X_test, y_train, y_test


def test_build_clf_model(data):
    X_train, X_test, y_train, y_test = data
    preprocessor = StandardScaler()
    model = KNeighborsClassifier()
    tbl_out_dir = "./test_outputs"
    os.makedirs(tbl_out_dir, exist_ok=True)
    replacement_dict = {'0': 'Class 0', '1': 'Class 1'}
    clf_report_file_name = "test_clf_report.csv"
    

    clf_model = build_clf_model(model, preprocessor, tbl_out_dir, X_train, y_train, X_test, y_test, replacement_dict, clf_report_file_name)
    

    assert clf_model is not None

    assert os.path.isfile(os.path.join(tbl_out_dir, clf_report_file_name))
    

    os.remove(os.path.join(tbl_out_dir, clf_report_file_name))
