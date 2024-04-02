import pandas as pd
import pytest
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.function_add_price_category import add_price_category  # Adjust the import based on your project structure

def test_add_price_category_spanning_all_ranges():
    data = pd.DataFrame({'price': [-10, 25, 75, 125, 175, 225, 275, 325, 375]})
    result = add_price_category(data)
    expected_categories = ['0-50', '0-50', '50-100', '100-150', '150-200', '200-250', '250-300', '300-350', '350+']
    assert all(result['price_category'] == expected_categories), "Test failed: Prices spanning all ranges are not categorized correctly."

def test_add_price_category_single_category():
    data = pd.DataFrame({'price': [100, 105, 110]})
    result = add_price_category(data)
    # Ensure the expected_series has the same categories and order as the result
    expected_series = pd.Series(['50-100', '100-150', '100-150'], name='price_category')
    expected_dtype = pd.CategoricalDtype(categories=['0-50', '50-100', '100-150', '150-200', '200-250', '250-300', '300-350', '350+'], ordered=True)
    expected_series = expected_series.astype(expected_dtype)
    pd.testing.assert_series_equal(result['price_category'], expected_series, check_categorical=True)

def test_add_price_category_empty_dataframe():
    data = pd.DataFrame({'price': []})
    result = add_price_category(data)
    assert result.empty, "Test failed: The function should return an empty DataFrame when provided with one."


def test_add_price_category_with_negative_prices():
    data = pd.DataFrame({'price': [-1, -20]})
    result = add_price_category(data)
    assert all(result['price_category'] == ['0-50', '0-50']), "Test failed: Negative prices are not categorized correctly."

def test_add_price_category_with_floats():
    data = pd.DataFrame({'price': [49.99, 100.01]})
    result = add_price_category(data)
    assert all(result['price_category'] == ['0-50', '100-150']), "Test failed: Float prices are not categorized correctly."

def test_add_price_category_with_boundary_prices():
    data = pd.DataFrame({'price': [50, 100, 150, 200, 250, 300, 350]})
    result = add_price_category(data)
    expected_categories = ['0-50', '50-100', '100-150', '150-200', '200-250', '250-300', '300-350']
    assert all(result['price_category'] == expected_categories), "Test failed: Boundary prices are not categorized correctly."

def test_add_price_category_preserves_dtype():
    data = pd.DataFrame({'price': [25, 75], 'other_column': [1, 2]})
    original_dtype = data.dtypes
    result = add_price_category(data)
    assert data.drop(columns=['price_category']).dtypes.equals(original_dtype), "Test failed: Original data types are altered."
