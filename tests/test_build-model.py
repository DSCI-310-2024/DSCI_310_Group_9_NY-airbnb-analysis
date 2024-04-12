
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
from sklearn.model_selection import RandomizedSearchCV
from unittest.mock import patch, MagicMock
import click
from scipy.stats import randint
import pandas as pd
import numpy as np
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.function_build_model import build_clf_model, knn_param_optimization

X, y = make_classification(n_samples=100, n_features=4, n_informative=2, n_redundant=0, random_state=42)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


def test_build_clf_model():
    """_summary_
    Tests using the clf function to preprocess data and run with the model 
    """
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
    os.rmdir(tbl_out_dir)

@pytest.fixture
def setup_data():

    X_train = np.random.rand(100, 5)
    y_train = np.random.randint(0, 2, size=(100,))
    X_test = np.random.rand(20, 5)
    y_test = np.random.randint(0, 2, size=(20,))
    return X_train, y_train, X_test, y_test

def test_knn_param_optimization(tmp_path, setup_data):
    # Using tmp_path fixture for directory handling
    X_train, y_train, X_test, y_test = setup_data
    knn_model = KNeighborsClassifier()
    tbl_out_dir = tmp_path  # Temporary directory
    replacement_dict = {'0': 'Class_0', '1': 'Class_1'}
    output_file_name = 'test_hyperparam_report.csv'

    param_dist = {
        'n_neighbors': randint(1, 5),
    }
    
    # Execute the function under test
    knn_param_optimization(knn_model, str(tbl_out_dir), X_train, y_train, X_test, y_test, replacement_dict, output_file_name,param_dist)

    # Validate the output file's existence
    output_file_path = tbl_out_dir / output_file_name
    assert output_file_path.is_file(), "Output file was not created."

    # Optionally, verify some aspects of the file's content
    df_output = pd.read_csv(output_file_path)
    assert not df_output.empty, "Output file is unexpectedly empty."
    
    os.remove(output_file_path)
    
    
    
