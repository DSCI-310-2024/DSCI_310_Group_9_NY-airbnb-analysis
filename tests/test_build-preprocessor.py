
import sys
import os
from sklearn.dummy import DummyClassifier
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import train_test_split

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.build_preprocessor import build_preprocessor




def test_preprocess():
    # making 
    train_data = {
    'category': ['A', 'A', 'A', 'A', 'B', 'B', 'B', 'B'],  # Categorical data
    'numeric': [2, 2, 2, 2, 15, 15, 15, 15],  # Numeric data
    'text': ["cat","cat","cat","cat","dog","dog","dog","dog"], # text data 
    'target': [0, 0, 0, 0, 1, 1, 0, 1]  # Target variable (0 or 1)
    }
    
    test_data = {
    'category': ['A', 'A', 'A', 'A', 'B', 'B', 'B', 'B'],  # Categorical data
    'numeric': [2, 2, 2, 2, 15, 15, 15, 15],  # Numeric data
    'text': ["cat","cat","cat","cat","dog","dog","dog","dog"], # text data 
    'target': [0, 0, 0, 0, 1, 1, 0, 1]  # Target variable (0 or 1)
    }
    
    X_train = train_data.drop(['target'],axis=1)
    X_test = test_data.drop(['target'],axis=1)
    
    y_train = train_data['target']
    y_test = test_data['target']
    
    categorical_data = "Category"
    
    numerical_data = "Numeric"
    
    text_data = "name"
    
    preprocessor = build_preprocessor(numerical_data, text_data, categorical_data)
    
    dummy_model = DummyClassifier()
    
    dummy_pipe = make_pipeline(preprocessor, dummy_model)
    
    dummy_pipe.fit(X_train,y_train)
    
    dummy_predict = dummy_pipe.predict(X_test)
    
    return dummy_predict