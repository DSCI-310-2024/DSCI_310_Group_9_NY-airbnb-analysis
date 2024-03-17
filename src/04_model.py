# Model fitting

# import libraries/packages

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
import warnings
warnings.filterwarnings("ignore")

# Function to create the directory if it doesn't exist
def create_dir_if_not_exists(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

# parse/define command line arguments here

@click.command()
@click.option('--input_dir', type=str,
              default="data/cleaned",
              help = 'Path to input directory')
@click.option('--tbl_out_dir', type=str,
              default="results/tables",
              help = 'Path to write the tables')

# define main function

def main(input_dir, tbl_out_dir):
    """Creates model and saves tables to src/tables."""
    
    create_dir_if_not_exists(tbl_out_dir)
    
    X_train = pd.read_csv(os.path.join(input_dir, 'X_train.csv'))
    y_train = pd.read_csv(os.path.join(input_dir, 'y_train.csv'))
    X_test = pd.read_csv(os.path.join(input_dir, 'X_test.csv'))
    y_test = pd.read_csv(os.path.join(input_dir, 'y_test.csv'))

    # numeric data
    numerical_data = ['latitude', 'longitude', 'minimum_nights', 'number_of_reviews', 'reviews_per_month',
                      'calculated_host_listings_count', 'availability_365', 'number_of_reviews_ltm']

    # text data
    text_data = "name"

    # Categorical Data
    categorical_data = ['neighbourhood_group', 'neighbourhood', 'room_type']
    
    # Numerical Transformer
    numerical_transformer = StandardScaler()

    # Categorical Transformer
    categorical_transformer = OneHotEncoder(handle_unknown='ignore')

    # Text Data Transformer
    text_transformer = CountVectorizer()

    # Encoding our y_train & y_test with ordinal encoder
    categories = [['0-50', '50-100', '100-150', '150-200', '200-250', '250-300', '300-350', '350+']]
    ordinal_encoder = OrdinalEncoder(categories=categories)
    y_train_encoded = ordinal_encoder.fit_transform(y_train.values.reshape(-1, 1)).ravel()
    y_test_encoded = ordinal_encoder.transform(y_test.values.reshape(-1, 1)).ravel()
    
    # Making Our Preprocessor
    preprocessor = make_column_transformer(
        (numerical_transformer, numerical_data),
        (categorical_transformer, categorical_data),
        (text_transformer, text_data),
        remainder='drop'
    )

    # Implementing a Dummy Regressor model as a baseline to assess our model with
    dummy_model = DummyClassifier()
    dummy_pipe = make_pipeline(preprocessor, dummy_model)
    dummy_pipe.fit(X_train, y_train_encoded)
    dummy_clf_report = classification_report(y_test_encoded, dummy_pipe.predict(X_test), output_dict=True)
    replacement_dict = {'0.0':'0-50', '1.0':'50-100', '2.0':'100-150', '3.0':'150-200', '4.0':'200-250','5.0':'250-300',
                        '6.0':'300-350', '7.0':'350+', 'accuracy':'accuracy', 'macro avg':'macro avg', 'weighted avg':'weighted avg'}
    dummy_clf_report = dict((replacement_dict[key], value) for (key, value) in dummy_clf_report.items())
    dummy_clf_report = pd.DataFrame(dummy_clf_report).transpose()

    # Saving table
    dummy_clf_report.to_csv(os.path.join(tbl_out_dir, 'dummy_classification_report.csv'))

    # Method to build model
    def build_model(model, preprocessor, X_train, y_train_encoded, X_test, y_test_encoded, clf=False):
        model_pipe = make_pipeline(preprocessor, model)
        model = model_pipe.fit(X_train, y_train_encoded)
        predictions = model.predict(X_test)
        return model, classification_report(y_test_encoded, predictions, output_dict=True)
    
    knn = KNeighborsClassifier()
    knn_model, knn_clf_report = build_model(knn, preprocessor, X_train, y_train_encoded, X_test, y_test_encoded, clf=True)
    knn_clf_report = dict((replacement_dict[key], value) for (key, value) in knn_clf_report.items())
    knn_clf_report = pd.DataFrame(knn_clf_report).transpose()

    # Saving table
    knn_clf_report.to_csv(os.path.join(tbl_out_dir, 'knn_classification_report.csv'))

    # KNN Hyperparameter Optimization
    param_dist = {
        'kneighborsclassifier__n_neighbors': randint(1, 30),
        'kneighborsclassifier__weights': ['uniform', 'distance'],
        'kneighborsclassifier__p': [1, 2]  
    }

    try:
        rand_search = RandomizedSearchCV(knn_model, param_distributions=param_dist, n_iter=5,  
                                        n_jobs=-1,  
                                        scoring='accuracy', cv=3, 
                                        verbose=1, random_state=42, pre_dispatch='2*n_jobs')  
    except Exception as e:
        print(f"Error with rand_search: {e}")
        rand_search = RandomizedSearchCV(knn_model, param_distributions=param_dist, n_iter=5,
                                        scoring='accuracy', cv=3, verbose=1, random_state=42)

    rand_search.fit(X_train, y_train_encoded)

    # Classification Report After Hyperparameter Optimization
    rand_search_predictions = rand_search.predict(X_test)
    hyperparam_clf_report = classification_report(y_test_encoded, rand_search_predictions, output_dict=True)
    hyperparam_clf_report = dict((replacement_dict[key], value) for (key, value) in hyperparam_clf_report.items())
    hyperparam_clf_report = pd.DataFrame(hyperparam_clf_report).transpose()

    # Saving table
    hyperparam_clf_report.to_csv(os.path.join(tbl_out_dir, 'hyperparam_classification_report.csv'))

    click.echo("Files Saved!")

# code for other functions & tests goes here

# call main function

if __name__ == "__main__":
    main() # pass any command line args to main here
