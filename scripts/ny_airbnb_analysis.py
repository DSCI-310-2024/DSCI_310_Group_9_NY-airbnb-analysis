import click
from pynyairbnb.data_preprocessing import data_preprocessing
from pynyairbnb.plotting import plot_pynyairbnb
from pynyairbnb.pynyairbnb import nyairbnb_analysis

# parse/define command line arguments here

@click.command()
@click.option('--data_url', type=str,
              default="http://data.insideairbnb.com/united-states/ny/new-york-city/2023-12-04/visualisations/listings.csv",
              help = 'URL to input data')
@click.option('--out_dir', type=str,
              default="data/cleaned",
              help = 'Path to save / retrieve the data files')
@click.option('--viz_out_dir', type=str,
              default="results/figures",
              help = 'Path to write the visualizations')
@click.option('--tbl_out_dir', type=str,
              default="results/tables",
              help = 'Path to write the tables')

# define main function

def main(data_url, out_dir, viz_out_dir, tbl_out_dir):
    """Runs analysis from top to bottom and saves all data files, figures, and tables."""
    
    data_preprocessing(data_url, out_dir, "data/raw")
    plot_pynyairbnb("data/cleaned/train_df.csv", viz_out_dir, tbl_out_dir)
    nyairbnb_analysis(out_dir, tbl_out_dir)
    
    click.echo("Files Saved!")

# code for other functions & tests goes here

# call main function

if __name__ == "__main__":
    main() # pass any command line args to main here
