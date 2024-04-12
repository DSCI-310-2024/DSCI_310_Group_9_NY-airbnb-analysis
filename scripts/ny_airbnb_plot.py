import click
from pynyairbnb.plotting import plot_pynyairbnb

# parse/define command line arguments here

@click.command()
@click.option('--viz_out_dir', type=str,
              default="results/figures",
              help = 'Path to write the visualizations')
@click.option('--tbl_out_dir', type=str,
              default="results/tables",
              help = 'Path to write the tables')

# define main function

def main(viz_out_dir, tbl_out_dir):
    """Generates all figures and tables for this analysis."""
    
    plot_pynyairbnb("data/cleaned/train_df.csv", viz_out_dir, tbl_out_dir)
    
    click.echo("Visualization Files Saved!")

# code for other functions & tests goes here

# call main function

if __name__ == "__main__":
    main() # pass any command line args to main here
