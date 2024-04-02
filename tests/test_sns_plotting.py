import pandas as pd
import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt
import pytest
import os
import sys

# Importing sns_plotting function
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.function_sns_plotting import sns_plotting  # Adjust the import based on your project structure

# Same Data to be used for all tests
data = pd.DataFrame({"price": [25, 75, 125, 175, 225, 275, 325, 375],
                     "number_of_reviews": [2, 0, 1, 15, 22, 7, 5, 3],
                     "reviews_per_month": [0, 3, 4, 1, 2, 0, 3, 4],
                     "room_type": ["cat2", "cat1", "cat5", "cat4", "cat3", "cat6", "cat8", "cat7"]})

# Check to see if output type is correct given correct inputs
def test_sns_plotting_output_type():
    result = sns_plotting('scatterplot', data, 'number_of_reviews', 'price', 20, 10)
    assert type(result) == matplotlib.figure.Figure, "Test failed: Output type is incorrect."

# Check to see if exception raised for n/a plot type
def test_sns_plotting_plottype_error():
    with pytest.raises(Exception):
        result = sns_plotting('barplot', data, 'number_of_reviews', 'price', 20, 10)

# Check to see if value error raised for x-variable not in data
def test_sns_plotting_x_error():
    with pytest.raises(ValueError):
        sns_plotting('scatterplot', data, 'random_x', 'price', 20, 10)

# Check to see if value error raised for y-variable not in data
def test_sns_plotting_y_error():
    with pytest.raises(ValueError):
        sns_plotting('scatterplot', data, 'number_of_reviews', 'random_y', 20, 10)

# Check to see the figlength and figheight are both <= 25 to avoid being too large
def test_sns_plotting_figsize_check():
    result = sns_plotting('scatterplot', data, 'number_of_reviews', 'price')
    assert result.get_size_inches()[0] <= 25 and result.get_size_inches()[1] <= 25, "Test failed: Plot size is too large."