# # Data Cleaning / Preprocessing

# # import libraries/packages


import click
import pandas as pd
from sklearn.model_selection import train_test_split
import os

def create_dir_if_not_exists(directory):
    """Create the directory if it doesn't exist."""
    if not os.path.exists(directory):
        os.makedirs(directory)

def read_data(input_path):
    """Read the data from the input path."""
    return pd.read_csv(input_path)

def preprocess_data(data):
    """Fill missing values and convert columns to string."""
    data['id'] = data['id'].astype(str)
    data['host_id'] = data['host_id'].astype(str)
    data['reviews_per_month'] = data['reviews_per_month'].fillna(0)
    return data

def split_data(data):
    """Split the data into training and testing datasets."""
    return train_test_split(data, test_size=0.2, shuffle=True)

def add_price_category(data):
    """Add price category based on the price."""
    categories = pd.cut(
        data['price'],
        bins=[-float('inf'), 50, 100, 150, 200, 250, 300, 350, float('inf')],
        labels=['0-50', '50-100', '100-150', '150-200', '200-250', '250-300', '300-350', '350+'],
        include_lowest=True
    )
    data['price_category'] = categories
    return data

def save_dataframes(out_dir, train_df, test_df):
    """Save the processed dataframes to the output directory."""
    train_df.to_csv(os.path.join(out_dir, 'train_df.csv'), index=False)
    test_df.to_csv(os.path.join(out_dir, 'test_df.csv'), index=False)

    X_train = train_df.drop(['price'], axis=1)
    y_train = train_df['price_category']
    X_test = test_df.drop(['price'], axis=1)
    y_test = test_df['price_category']

    X_train.to_csv(os.path.join(out_dir, 'X_train.csv'), index=False)
    y_train.to_csv(os.path.join(out_dir, 'y_train.csv'), index=False)
    X_test.to_csv(os.path.join(out_dir, 'X_test.csv'), index=False)
    y_test.to_csv(os.path.join(out_dir, 'y_test.csv'), index=False)

# call helper functions above
@click.command()
@click.option('--input_path', type=str, default="data/raw/airbnb_data_2023.csv", help='Path to input data')
@click.option('--out_dir', type=str, default="data/cleaned", help='Path to write the file')
def main(input_path, out_dir):
    """Main function orchestrating the data cleaning and preprocessing."""
    create_dir_if_not_exists(out_dir)

    data = read_data(input_path)
    data = preprocess_data(data)
    train_df, test_df = split_data(data)
    train_df = add_price_category(train_df)
    test_df = add_price_category(test_df)
    save_dataframes(out_dir, train_df, test_df)

    click.echo("Files Saved!")

# call main function
if __name__ == "__main__":
    main()
