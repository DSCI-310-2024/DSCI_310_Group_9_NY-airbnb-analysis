# Data Visualization

# import libraries/packages

import click
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import os

# Function to create the directory if it doesn't exist
def create_dir_if_not_exists(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

# parse/define command line arguments here

@click.command()
@click.option('--input_file', type=str,
              default="data/cleaned/train_df.csv",
              help = 'Path to input data')
@click.option('--viz_out_dir', type=str,
              default="src/figures",
              help = 'Path to write the visualizations')
@click.option('--tbl_out_dir', type=str,
              default="src/tables",
              help = 'Path to write the tables')

# define main function

def main(input_file, viz_out_dir, tbl_out_dir):
    """Creates all visualizations + tables and saves them to src/figures or src/tables."""
    
    create_dir_if_not_exists(viz_out_dir)
    create_dir_if_not_exists(tbl_out_dir)
    
    data = pd.read_csv(input_file)

    # Fig. 1 Correlation Heat Map of Numerical Predictors

    corr_matrix = data.select_dtypes(include=["int64", "float64"]).corr()
    train_corr = corr_matrix.corr(method = 'pearson')
    mask = np.zeros_like(train_corr, dtype=bool)
    mask[np.triu_indices_from(mask)] = True

    fig1, ax1 = plt.subplots(figsize=(7, 5))

    sns.heatmap(train_corr, mask=mask, vmin=-1, vmax=1, center=0, linewidths=.5, cmap="vlag")
    fig1.suptitle('Correlation Heat Map of Numeric Predictors', fontsize=12)
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
    
    fig3, ax3 = plt.subplots(nrows=1,ncols=2,figsize=(20, 6))

    sns.scatterplot(data, x = 'number_of_reviews', y='price', hue='room_type', ax=ax3[0])
    ax3[0].set_title("Price vs Number of Reviews Coloured by Room Type")
    ax3[0].set(xlabel="# of Reviews", ylabel="Price")

    sns.scatterplot(data, x = 'number_of_reviews', y='price', hue='room_type', ax=ax3[1])
    ax3[1].set_title("Price (< 5000) vs Number of Reviews For Clarity")
    ax3[1].set(xlabel="# of Reviews", ylabel="Price")
    ax3[1].set_ylim(-100, 5000)

    fig3.tight_layout

    fig3.savefig(os.path.join(viz_out_dir, 'price_vs_reviews.jpg'))

    # Fig. 4 Price vs Reviews Per Month Coloured by Room Type Scatterplot

    fig4, ax4 = plt.subplots(nrows=1,ncols=2,figsize=(20, 6))

    sns.scatterplot(data, x = 'reviews_per_month', y='price', hue='room_type', ax=ax4[0])
    ax4[0].set_title("Price vs Reviews Per Month Coloured by Room Type")
    ax4[0].set(xlabel="# of Reviews Per Month", ylabel="Price")

    sns.scatterplot(data, x = 'reviews_per_month', y='price', hue='room_type', ax=ax4[1])
    ax4[1].set_title("Price (< 5000) vs Reviews Per Month For Clarity")
    ax4[1].set(xlabel="# of Reviews Per Month", ylabel="Price")
    ax4[1].set_ylim(-100, 5000)

    fig4.tight_layout

    fig4.savefig(os.path.join(viz_out_dir, 'price_vs_reviews_per_month.jpg'))
    
    # Fig. 5 Log Price and Price by Neighbourhood Group Boxplot

    log_price = np.log(data['price'])

    fig5, ax5 = plt.subplots(nrows=1, ncols=2, figsize=(12, 6))
    
    sns.boxplot(x='neighbourhood_group', y=log_price, data=data, ax=ax5[0])
    ax5[0].set_title('Log Price by Neighbourhood Group')
    ax5[0].set_xlabel('Neighbourhood Group')
    ax5[0].set_ylabel('Log Price')
    
    sns.boxplot(x='neighbourhood_group', y='price', data=data, showfliers=False, ax=ax5[1])
    ax5[1].set_title('Price by Neighbourhood Group (Outliers Removed)')
    ax5[1].set_xlabel('Neighbourhood Group')
    ax5[1].set_ylabel('Price')

    fig5.tight_layout

    fig5.savefig(os.path.join(viz_out_dir, 'neighbourhood_groups_boxplots.jpg'))

    # Fig. 6 Log Price and Price by Room Type Boxplot

    fig6, ax6 = plt.subplots(nrows=1, ncols=2, figsize=(12, 6))

    sns.boxplot(x='room_type', y=log_price, data=data, ax=ax6[0])
    ax6[0].set_title('Log Price by Room Type')
    ax6[0].set_xlabel('Room Type')
    ax6[0].set_ylabel('Log Price')

    sns.boxplot(x='room_type', y='price', data=data, showfliers=False, ax=ax6[1])
    ax6[1].set_title('Price by Room Type (Outliers Removed)')
    ax6[1].set_xlabel('Room Type')
    ax6[1].set_ylabel('Price')

    fig6.tight_layout

    fig6.savefig(os.path.join(viz_out_dir, 'room_type_boxplots.jpg'))

    # Fig. 7 Price Histogram (Outliers Removed)

    Q1 = data['price'].quantile(0.25)
    Q3 = data['price'].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    filtered_train_df = data[(data['price'] >= lower_bound) & (data['price'] <= upper_bound)]

    fig7, ax7 = plt.subplots(figsize=(7, 5))

    sns.histplot(data=filtered_train_df, x='price')

    fig7.suptitle('Price Distribution without Outliers')
    plt.xlabel('Price')
    plt.ylabel('Frequency')
    
    fig7.tight_layout

    fig7.savefig(os.path.join(viz_out_dir, 'price_histogram.jpg'))

    click.echo("Files Saved!")

# code for other functions & tests goes here

# call main function

if __name__ == "__main__":
    main() # pass any command line args to main here
