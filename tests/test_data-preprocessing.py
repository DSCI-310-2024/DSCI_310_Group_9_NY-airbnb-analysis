import os
import pandas as pd
import sys
from click.testing import CliRunner
from unittest.mock import patch, MagicMock
import pytest

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from scripts import data_preprocessing

@pytest.fixture
def mock_data():
    return pd.DataFrame({
        'id': range(10),  # 10 samples
        'host_id': range(10, 20),
        'price': [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],
        'reviews_per_month': [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0],
        'price_category': ['0-50', '50-100', '100-150', '150-200', '200-250', '250-300', '300-350', '350+', '350+', '350+']
    })


def test_create_dir_if_not_exists(tmp_path):
    dir_path = tmp_path / "new_dir"
    data_preprocessing.create_dir_if_not_exists(str(dir_path))
    assert dir_path.exists()

@patch('scripts.data_preprocessing.pd.read_csv')
def test_read_data(mock_read_csv, mock_data):
    mock_read_csv.return_value = mock_data
    data = data_preprocessing.read_data("dummy_path.csv")
    pd.testing.assert_frame_equal(data, mock_data)

def test_preprocess_data(mock_data):
    processed_data = data_preprocessing.preprocess_data(mock_data)
    assert all(processed_data['id'].apply(lambda x: isinstance(x, str)))
    assert all(processed_data['host_id'].apply(lambda x: isinstance(x, str)))
    assert 'reviews_per_month' in processed_data.columns

def test_add_price_category():
    # Mock data before price categorization
    mock_df = pd.DataFrame({
        'price': [75, 150, 225, 300]
    })

    # Expected data should include the 'price_category' after applying the function
    expected_categories = pd.Categorical(['50-100', '100-150', '200-250', '250-300'],
                                        categories=['0-50', '50-100', '100-150', '150-200', '200-250', '250-300', '300-350', '350+'],
                                        ordered=True)

    expected_df = mock_df.copy()
    expected_df['price_category'] = expected_categories

    # Apply the function to mock data
    result_df = data_preprocessing.add_price_category(mock_df)

    # Assert the correctness of the result
    pd.testing.assert_frame_equal(result_df, expected_df)

@patch('scripts.data_preprocessing.pd.DataFrame.to_csv')
def test_save_dataframes(mock_to_csv, tmp_path, mock_data):
    train_df, test_df = mock_data, mock_data  # Simplification for testing
    data_preprocessing.save_dataframes(str(tmp_path), train_df, test_df)
    mock_to_csv.assert_called()

def test_main_functionality(tmp_path, mock_data):
    runner = CliRunner()
    with runner.isolated_filesystem():
        input_csv = tmp_path / "input.csv"
        output_dir = tmp_path / "output"
        mock_data.to_csv(input_csv)  # Use the fixture data

        result = runner.invoke(data_preprocessing.main, ['--input_path', str(input_csv), '--out_dir', str(output_dir)])
        assert result.exit_code == 0
        assert "Files Saved!" in result.output

        # Check if output files exist
        expected_files = ['train_df.csv', 'test_df.csv', 'X_train.csv', 'y_train.csv', 'X_test.csv', 'y_test.csv']
        for file_name in expected_files:
            assert os.path.exists(os.path.join(output_dir, file_name))

        
@patch('scripts.data_preprocessing.pd.read_csv')
def test_invalid_data_formats(mock_read_csv, tmp_path):
    mock_read_csv.return_value = pd.DataFrame({
        'id': ['one', 'two'],
        'host_id': [3, 4],
        'price': ['a hundred', 'two hundred'],
        'reviews_per_month': [1.0, 'two']
    })
    runner = CliRunner()
    with runner.isolated_filesystem():
        result = runner.invoke(data_preprocessing.main, ['--input_path', 'dummy.csv', '--out_dir', str(tmp_path)])
        assert result.exit_code != 0


def test_price_categorization_logic():
    mock_df = pd.DataFrame({
        'price': [75, 150, 225, 300]
    })
    expected_categories = ['50-100', '100-150', '200-250', '250-300']
    categorized_df = data_preprocessing.add_price_category(mock_df)
    assert all(categorized_df['price_category'] == expected_categories)

    
def test_data_splitting_proportions(mock_data):
    train_df, test_df = data_preprocessing.split_data(mock_data)
    total_len = len(mock_data)
    train_len = len(train_df)
    test_len = len(test_df)
    # Check if the proportions approximately match the expected 80-20 split
    assert train_len / total_len == pytest.approx(0.8, 0.05)
    assert test_len / total_len == pytest.approx(0.2, 0.05)
