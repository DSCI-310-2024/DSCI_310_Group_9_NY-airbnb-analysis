import click
from pynyairbnb.data_preprocessing import data_preprocessing

# parse/define command line arguments here

@click.command()
@click.option('--data_url', type=str,
              default="http://data.insideairbnb.com/united-states/ny/new-york-city/2023-12-04/visualisations/listings.csv",
              help = 'URL to input data')
@click.option('--out_dir', type=str,
              default="data/cleaned",
              help = 'Path to save / retrieve the data files')

# define main function

def main(data_url, out_dir):
    """Reads and preprocesses the data for this analysis."""
    
    data_preprocessing(data_url, out_dir, "data/raw")
    
    click.echo("Data File Saved!")

# code for other functions & tests goes here

# call main function

if __name__ == "__main__":
    main() # pass any command line args to main here
