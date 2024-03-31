# Loading and Saving the Raw Data

# import libraries/packages

import click
import pandas as pd
import os

# Function to create the directory if it doesn't exist
def create_dir_if_not_exists(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

# parse/define command line arguments here

@click.command()
@click.option('--data_url', type=str,
              default="http://data.insideairbnb.com/united-states/ny/new-york-city/2023-12-04/visualisations/listings.csv",
              help = 'URL to input data')
@click.option('--out_dir', type=str,
              default="data/raw",
              help = 'Path (including filename) of where to write the file')

# define main function

def main(data_url, out_dir):
    """Loads and saves the data for this project."""
    
    create_dir_if_not_exists(out_dir)

    data = pd.read_csv(data_url)
    data.to_csv(os.path.join(out_dir, 'airbnb_data_2023.csv'), index=False)
    click.echo("File Saved!")

# code for other functions & tests goes here

# call main function

if __name__ == "__main__":
    main() # pass any command line args to main here
