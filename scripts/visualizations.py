# Data Visualization

# import libraries/packages

import click
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.function_sns_plotting import sns_plotting

# Function to create the directory if it doesn't exist
def create_dir_if_not_exists(directory):
    if not os.path.exists(directory):
        os.makedirs(directory, exist_ok=True)

# Function to rank top 10 correlations
def rank_correlations(corr_matrix):
    # flattening matrix
    flattened_matrix = corr_matrix.stack().reset_index()
    #renaming columns
    flattened_matrix.columns = ['Variable_1', 'Variable_2', 'Correlation']
    # removing duplicate variable names
    flattened_matrix = flattened_matrix.loc[flattened_matrix['Variable_1'] != flattened_matrix['Variable_2']]
    corr_column = flattened_matrix['Correlation']
    flattened_matrix = flattened_matrix.iloc[abs(corr_column).argsort()[::-1]]
    flattened_matrix = flattened_matrix.loc[flattened_matrix['Correlation'].duplicated()]
    #print(f'Top 10 Variable Correlations: \n{flattened_matrix.head(10)}')
    return flattened_matrix.head(10)

@click.command()
@click.option('--input_file', type=str,
              default="data/cleaned/train_df.csv",
              help = 'Path to input data')
@click.option('--viz_out_dir', type=str,
              default="results/figures",
              help = 'Path to write the visualizations')
@click.option('--tbl_out_dir', type=str,
              default="results/tables",
              help = 'Path to write the tables')

# define main function

def main(input_file, viz_out_dir, tbl_out_dir):
    """Creates all visualizations + tables and saves them to src/figures or src/tables."""
    
    create_dir_if_not_exists(viz_out_dir)
    create_dir_if_not_exists(tbl_out_dir)
    
    data = pd.read_csv(input_file)

    # Fig. 1 Correlation Heat Map of Numerical Predictors

    fig1 = sns_plotting('heatmap', data, 7, 5)
    fig1.tight_layout()
    fig1.savefig(os.path.join(viz_out_dir, 'corr_heat_map.jpg'))

    # Fig. 2 Map with Distribution of Listings by Location and Price

    fig2, ax2 = plt.subplots(nrows=1,ncols=2,figsize=(14, 6))

    vmin, vmax = 0, 400 # Setting color limits to more typical range, e.g., 0 to 400

    ax2[0].scatter(data['longitude'], data['latitude'], c=data['price'], #cmap='viridis',
                s=10, alpha=0.6, vmin=vmin, vmax=vmax)
    fig2.colorbar(plt.scatter(data['longitude'], data['latitude'], c=data['price'], #cmap='viridis',
                s=10, alpha=0.6, vmin=vmin, vmax=vmax), label='Price', ax=ax2[0])
    ax2[0].grid(True, which='both', linestyle='--', linewidth=0.5)
    ax2[0].set_title('Distribution of Listings by Location and Price')
    ax2[0].set(xlabel='Longitude', ylabel='Latitude')

    img = mpimg.imread('src/images/New_York_City_Map.jpg')

    ax2[1].imshow(img)
    ax2[1].set_title('Map of New York City')
    ax2[1].axis("off")

    fig2.savefig(os.path.join(viz_out_dir, 'listing_locations.jpg'))

    # Fig. 3 Price vs Number of Reviews Coloured by Room Type Scatterplot
    
    fig3 = sns_plotting('scatterplot', data, x='number_of_reviews', y='price', figlength=20, figheight=6)
    fig3.tight_layout
    fig3.savefig(os.path.join(viz_out_dir, 'price_vs_reviews.jpg'))

    # Fig. 4 Price vs Reviews Per Month Coloured by Room Type Scatterplot

    fig4 = sns_plotting('scatterplot', data, x='reviews_per_month', y='price', figlength=20, figheight=6)
    fig4.tight_layout
    fig4.savefig(os.path.join(viz_out_dir, 'price_vs_reviews_per_month.jpg'))
    
    # Fig. 5 Log Price and Price by Neighbourhood Group Boxplot

    fig5 = sns_plotting('boxplot', data, x='neighbourhood_group', y='price', figlength=12, figheight=6)
    fig5.tight_layout
    fig5.savefig(os.path.join(viz_out_dir, 'neighbourhood_groups_boxplots.jpg'))

    # Fig. 6 Log Price and Price by Room Type Boxplot

    fig6 = sns_plotting('boxplot', data, x='room_type', y='price', figlength=12, figheight=6)
    fig6.tight_layout
    fig6.savefig(os.path.join(viz_out_dir, 'room_type_boxplots.jpg'))

    # Fig. 7 Price Histogram (Outliers Removed)

    fig7 = sns_plotting('histplot', data, y='price', figlength=7, figheight=5)
    fig7.tight_layout
    fig7.savefig(os.path.join(viz_out_dir, 'price_histogram.jpg'))
    
    # Table 1: Correlations Ranked

    corr_matrix = data.select_dtypes(include=["int64", "float64"]).corr()
    table1 = rank_correlations(corr_matrix)
    table1.to_csv(os.path.join(tbl_out_dir, 'correlations_ranked.csv'), index=False)

    click.echo("Files Saved!")

# code for other functions & tests goes here

# call main function

if __name__ == "__main__":
    main() # pass any command line args to main here