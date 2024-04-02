import pandas as pd

def add_price_category(data):
    """
    Adds a 'price_category' column to the DataFrame based on predefined price ranges, facilitating easier analysis of data by price segments.
    
    This function categorizes each entry into one of seven price ranges, thereby enabling quick insights into the distribution of prices. The categories are defined as follows: 
    '0-50', '50-100', '100-150', '150-200', '200-250', '250-300', '300-350'. 
    Each range captures the minimum inclusive and maximum exclusive price points for that category, except for the '0-50' range, which is inclusive of 50, and '300-350', which is inclusive of 350.
    
    Parameters:
    -----------
    - data (pd.DataFrame): A DataFrame containing at least a 'price' column with numeric values. The 'price' values should be integers or floats.
    
    Returns:
    --------
    - pd.DataFrame: The modified DataFrame with an additional column 'price_category'. This column contains categorical labels indicating the price range for each row.
    
    Examples:
    ---------
    >>> import pandas as pd
    >>> data = pd.DataFrame({"price": [25, 75, 125, 175, 225, 275, 325, 375]})
    >>> add_price_category(data)
        price price_category
    0     25           0-50
    1     75         50-100
    2    125       100-150
    3    175       150-200
    4    225       200-250
    5    275       250-300
    6    325       300-350
    7    375           350+
    
    Notes:
    ------
    - The function directly modifies the input DataFrame by adding a new column 'price_category'.
    - Prices are categorized based on predefined bins, which are set to be inclusive of the lower bound and exclusive of the upper bound for all categories except for the first ('0-50') and the last ('350+'), which includes all prices above 350.
    - Negative price values are treated as errors in input data and will be categorized into the lowest bin ('0-50'), implying the need for data cleaning if such values exist.
    """
    categories = pd.cut(
        data['price'],
        bins=[-float('inf'), 50, 100, 150, 200, 250, 300, 350, float('inf')],
        labels=['0-50', '50-100', '100-150', '150-200', '200-250', '250-300', '300-350', '350+'],
        include_lowest=True
    )
    data['price_category'] = categories
    return data
