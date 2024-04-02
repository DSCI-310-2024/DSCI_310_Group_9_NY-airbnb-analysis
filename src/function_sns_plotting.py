import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def sns_plotting(plot_type, data, x='number_of_reviews', y='price', figlength=14, figheight=7):
    """
    Generates a plot from the seaborn library with the provided plot type, the x-variable, and the y-variable from provided data.

    This function does so by using matplotlib pyplot subplots and setting the figsize to the provided figlength and figheight.
    
    Parameters:
    -----------
    - plot_type (str): Type of plot to generate - one of 'scatterplot', 'boxplot', 'histplot' or 'heatmap'.
    - data (pd.DataFrame): A DataFrame containing at least 2 columns.
    - x (str): x-variable present in data. (Not applicable for 'heatmap')
    - y (str): y-variable present in data. (Not applicable for 'heatmap')
    - figlength (int): The length of the plotting area in inches.
    - figheight (int): The height of the plotting area in inches.
    
    Returns:
    --------
    - matplotlib.figure.Figure: The matplotlib figure containing the plot.
    
    Examples:
    ---------
    >>> import pandas as pd
    >>> import numpy as np
    >>> import seaborn as sns
    >>> import matplotlib.pyplot as plt
    >>> data = pd.DataFrame({"price": [25, 75, 125, 175, 225, 275, 325, 375],
                            "number_of_reviews": [2, 0, 1, 15, 22, 7, 5, 3]})
    >>> figure = sns_plotting('scatterplot', data, x='number_of_reviews', y='price', figlength=12, figheight=6)
    >>> figure.tight_layout
    
    Notes:
    ------
    - The function directly modifies the input DataFrame to what is necessary for the plot.
    """
    if plot_type == "heatmap":

        corr_matrix = data.select_dtypes(include=["int64", "float64"]).corr()
        train_corr = corr_matrix.corr(method = 'pearson')
        mask = np.zeros_like(train_corr, dtype=bool)
        mask[np.triu_indices_from(mask)] = True

        fig, ax = plt.subplots(figsize=(7, 5))

        sns.heatmap(train_corr, mask=mask, vmin=-1, vmax=1, center=0, linewidths=.5, cmap="vlag")
        fig.suptitle('Correlation Heat Map of Numeric Predictors', fontsize=12)

    elif plot_type == "scatterplot":

        fig, ax = plt.subplots(nrows=1,ncols=2,figsize=(figlength, figheight))

        sns.scatterplot(data=data, x=x, y=y, hue='room_type', ax=ax[0])
        if x == 'number_of_reviews':
            ax[0].set_title("Price vs Number of Reviews Coloured by Room Type")
            ax[0].set(xlabel="# of Reviews", ylabel="Price")
        elif x == 'reviews_per_month':
            ax[0].set_title("Price vs Reviews Per Month Coloured by Room Type")
            ax[0].set(xlabel="# of Reviews Per Month", ylabel="Price")

        sns.scatterplot(data=data, x=x, y=y, hue='room_type', ax=ax[1])
        ax[1].set_ylim(-100, 5000)
        if x == 'number_of_reviews':
            ax[1].set_title("Price (< 5000) vs Number of Reviews For Clarity")
            ax[1].set(xlabel="# of Reviews", ylabel="Price")
        elif x == 'reviews_per_month':
            ax[1].set_title("Price (< 5000) vs Reviews Per Month For Clarity")
            ax[1].set(xlabel="# of Reviews Per Month", ylabel="Price")

    elif plot_type == "boxplot":

        fig, ax = plt.subplots(nrows=1,ncols=2,figsize=(figlength, figheight))
        
        sns.boxplot(data=data, x=x, y=np.log(data[y]), ax=ax[0])
        if x == 'neighbourhood_group':
            ax[0].set_title("Log Price by Neighbourhood Group")
            ax[0].set(xlabel="Neighbourhood Group", ylabel="Log Price")
        elif x == 'room_type':
            ax[0].set_title("Log Price by Room Type")
            ax[0].set(xlabel="Room Type", ylabel="Log Price")

        sns.boxplot(data=data, x=x, y=np.log(data[y]), showfliers=False, ax=ax[1])
        if x == 'neighbourhood_group':
            ax[1].set_title("Price by Neighbourhood Group (Outliers Removed)")
            ax[1].set(xlabel="Neighbourhood Group", ylabel="Price")
        elif x == 'room_type':
            ax[1].set_title("Price by Room Type (Outliers Removed)")
            ax[1].set(xlabel="Room Type", ylabel="Price")
    
    elif plot_type == "histplot":
        Q1 = data[y].quantile(0.25)
        Q3 = data[y].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        filtered_train_df = data[(data[y] >= lower_bound) & (data[y] <= upper_bound)]

        fig, ax = plt.subplots(figsize=(figlength, figheight))

        sns.histplot(data=filtered_train_df, x=y)
        fig.suptitle('Price Distribution without Outliers')
        plt.xlabel('Price')
        plt.ylabel('Frequency')

    else: raise Exception("plot_type must be one of scatterplot, boxplot, histplot or heatmap")
    
    return fig
