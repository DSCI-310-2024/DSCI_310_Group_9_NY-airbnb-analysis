# Data Cleaning / Preprocessing

# import libraries/packages

import click
import pandas as pd
from sklearn.model_selection import train_test_split
import os

# Function to create the directory if it doesn't exist
def create_dir_if_not_exists(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

# parse/define command line arguments here

@click.command()
@click.option('--input_path', type=str,
              default="data/raw/airbnb_data_2023.csv",
              help = 'Path to input data')
@click.option('--out_dir', type=str,
              default="data/cleaned",
              help = 'Path to write the file')

# define main function

def main(input_path, out_dir):
    """Cleans the data and saves the cleaned training and testing files."""
    
    create_dir_if_not_exists(out_dir)

    data = pd.read_csv(input_path)

    data['id'] = str(data['id'])
    data['host_id'] = str(data['host_id'])
    data['reviews_per_month'] = data['reviews_per_month'].fillna(0)
    
    train_df, test_df = train_test_split(data, test_size=0.2, shuffle=True)
    
    train_df['price_category'] = pd.cut(
        train_df['price'],
        bins=[-float('inf'), 50, 100, 150, 200, 250, 300, 350, float('inf')],
        labels=['0-50', '50-100', '100-150', '150-200', '200-250', '250-300', '300-350', '350+'],
        include_lowest=True
    )
    
    train_df.to_csv(os.path.join(out_dir, 'train_df.csv'), index=False)

    test_df['price_category'] = pd.cut(
        test_df['price'],
        bins=[-float('inf'), 50, 100, 150, 200, 250, 300, 350, float('inf')],
        labels=['0-50', '50-100', '100-150', '150-200', '200-250', '250-300', '300-350', '350+'],
        include_lowest=True
    )
    
    test_df.to_csv(os.path.join(out_dir, 'test_df.csv'), index=False)

    X_train = train_df.drop(['price'], axis=1)
    y_train = train_df['price_category']
    X_test = test_df.drop(['price'], axis=1)
    y_test = test_df['price_category']

    X_train.to_csv(os.path.join(out_dir, 'X_train.csv'), index=False)
    y_train.to_csv(os.path.join(out_dir, 'y_train.csv'), index=False)
    X_test.to_csv(os.path.join(out_dir, 'X_test.csv'), index=False)
    y_test.to_csv(os.path.join(out_dir, 'y_test.csv'), index=False)

    click.echo("Files Saved!")

# code for other functions & tests goes here

# call main function

if __name__ == "__main__":
    main() # pass any command line args to main here
