import click
from pynyairbnb.pynyairbnb import nyairbnb_analysis

# parse/define command line arguments here

@click.command()
@click.option('--out_dir', type=str,
              default="data/cleaned",
              help = 'Path to save / retrieve the data files')
@click.option('--tbl_out_dir', type=str,
              default="results/tables",
              help = 'Path to write the tables')

# define main function

def main(out_dir, tbl_out_dir):
    """Builds the model, runs hyperparameter optimization and saves the output tables."""
    
    nyairbnb_analysis(out_dir, tbl_out_dir)
    
    click.echo("Analysis Files Saved!")

# code for other functions & tests goes here

# call main function

if __name__ == "__main__":
    main() # pass any command line args to main here
