# Loading and Saving the Data

# import libraries/packages

import click
import pandas as pd

# parse/define command line arguments here

@click.command()
@click.option('--data_url', type=str,
              default="http://data.insideairbnb.com/united-states/ny/new-york-city/2023-12-04/visualisations/listings.csv",
              help = 'URL to input data')
@click.option('--destination', type=str,
              default="data/raw/airbnb_data_2023.csv",
              help = 'Path (including filename) of where to write the file')

# define main function

def main(data_url, destination):
    """Loads and saves the data for this project."""
    
    data = pd.read_csv(data_url)
    data.to_csv(destination, index=False)
    click.echo("File Saved!")

# code for other functions & tests goes here

# call main function

if __name__ == "__main__":
    main() # pass any command line args to main here
