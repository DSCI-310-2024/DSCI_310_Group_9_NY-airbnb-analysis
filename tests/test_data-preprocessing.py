import pandas as pd
import pytest
import os
from click.testing import CliRunner
from unittest.mock import patch, MagicMock
from sklearn.model_selection import train_test_split
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.data_preprocessing import main, create_dir_if_not_exists

def test_directory_creation(tmp_path):
    output_dir = tmp_path / "cleaned"
    assert not output_dir.exists()
    create_dir_if_not_exists(str(output_dir))
    assert output_dir.exists()

@patch('pandas.read_csv')
def test_file_creation(mock_read_csv, tmp_path):
    # Setup mock DataFrame to avoid reading from actual file
    mock_read_csv.return_value = pd.DataFrame({
        'id': [1, 2, 3, 4],
        'host_id': [3, 4, 5, 6],
        'price': [100, 150, 300, 900],
        'reviews_per_month': [1.0, None, 2.0, 3.0,]
    })
    runner = CliRunner()
    with runner.isolated_filesystem():
        result = runner.invoke(main, ['--input_path', 'dummy_input.csv', '--out_dir', str(tmp_path)])
        assert result.exit_code == 0
        # Check for file creation
        assert (tmp_path / 'train_df.csv').exists()
        assert (tmp_path / 'test_df.csv').exists()
        assert (tmp_path / 'X_train.csv').exists()
        assert (tmp_path / 'y_train.csv').exists()
        assert (tmp_path / 'X_test.csv').exists()
        assert (tmp_path / 'y_test.csv').exists()
        
@patch('pandas.read_csv')
def test_data_content_after_preprocessing(mock_read_csv, tmp_path):
    mock_read_csv.return_value = pd.DataFrame({
        'id': [1, 2, 3, 4],
        'host_id': [3, 4, 5, 6],
        'price': [100, 150, 300, 900],
        'reviews_per_month': [1.0, None, 2.0, 3.0,]
    })
    expected_filled_reviews = pd.Series([1.0, 0.0], name='reviews_per_month')

    runner = CliRunner()
    result = runner.invoke(main, ['--input_path', 'dummy_input.csv', '--out_dir', str(tmp_path)])
    assert result.exit_code == 0
    # ! Further logic to read and assert processed_data contents needs to be added here

def read_csv(file_path):
    return pd.read_csv(file_path)

# ! Figure this out
# def test_data_splitting(tmp_path):
#     """
#     Test if data is split correctly according to the specified test size.
#     """
#     runner = CliRunner()
#     with patch('pandas.read_csv'), runner.isolated_filesystem():
#         runner.invoke(main, ['--input_path', 'dummy_input.csv', '--out_dir', str(tmp_path)])
#         train_df = read_csv(tmp_path / 'train_df.csv')
#         test_df = read_csv(tmp_path / 'test_df.csv')
        
#         # Assuming a 0.2 test split, we can check if the sizes approximately match this ratio
#         total_rows = len(train_df) + len(test_df)
#         assert len(train_df) / total_rows == pytest.approx(0.2, 0.05)

def test_price_category_creation(tmp_path):
    """
    Test if price categories are correctly created.
    """
    runner = CliRunner()
    with patch('pandas.read_csv'), runner.isolated_filesystem():
        runner.invoke(main, ['--input_path', 'dummy_input.csv', '--out_dir', str(tmp_path)])
        train_df = read_csv(tmp_path / 'train_df.csv')
        
        # Check if price categories are as expected
        assert all(train_df['price_category'].notnull())

def test_column_removal_in_X_train_and_X_test(tmp_path):
    """
    Test if 'price' column is removed from X_train and X_test.
    """
    runner = CliRunner()
    with patch('pandas.read_csv'), runner.isolated_filesystem():
        runner.invoke(main, ['--input_path', 'dummy_input.csv', '--out_dir', str(tmp_path)])
        X_train = read_csv(tmp_path / 'X_train.csv')
        X_test = read_csv(tmp_path / 'X_test.csv')
        
        assert 'price' not in X_train.columns
        assert 'price' not in X_test.columns


@pytest.fixture
def mock_df():
    return pd.DataFrame({
        'id': [1, 2],
        'host_id': [3, 4],
        'price': [100, 150],
        'reviews_per_month': [1.0, None]
    })

# ! need to figure this out
# @patch('pandas.read_csv')
# def test_data_splitting(mock_read_csv, tmp_path, mock_df):
#     mock_read_csv.return_value = mock_df
#     runner = CliRunner()
#     result = runner.invoke(main, ['--input_path', 'dummy_input.csv', '--out_dir', str(tmp_path)])
#     assert result.exit_code == 0
#     # Implement your logic to verify the data splitting here

@patch('pandas.read_csv')
def test_fill_NaN_in_reviews_per_month(mock_read_csv, tmp_path, mock_df):
    mock_read_csv.return_value = mock_df
    runner = CliRunner()
    result = runner.invoke(main, ['--input_path', 'dummy_input.csv', '--out_dir', str(tmp_path)])
    assert result.exit_code == 0
    train_df = read_csv(tmp_path / 'train_df.csv')
    assert (train_df['reviews_per_month'] == 0).any()  # Corrected assertion

# import pandas as pd
# import pytest
# from click.testing import CliRunner
# from unittest.mock import patch
# import os
# import sys

# # Adjust the system path to include the parent directory for imports
# sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
# from src.data_preprocessing import main, create_dir_if_not_exists

# # Fixture to simulate input data as a DataFrame
# @pytest.fixture
# def mock_df():
#     # Example DataFrame that includes a 'price_category' column to simulate post-processing state
#     df = pd.DataFrame({
#         'id': [1, 2],
#         'host_id': [3, 4],
#         'price': [100, 150],
#         'reviews_per_month': [1.0, 0.0],  # Assuming preprocessing fills NaN with 0
#         'price_category': ['100-150', '150-200']  # Example price_category values
#     })
#     # Simulate the removal of 'price' column as would be done in preprocessing
#     df_processed = df.drop('price', axis=1)
#     return df_processed


# # Test for verifying the creation of the output directory
# def test_directory_creation(tmp_path):
#     output_dir = tmp_path / "cleaned"
#     assert not output_dir.exists()
#     create_dir_if_not_exists(str(output_dir))
#     assert output_dir.exists()

# # Test to ensure all expected files are created by the preprocessing script
# @patch('pandas.read_csv')
# def test_file_creation(mock_read_csv, tmp_path, mock_df):
#     mock_read_csv.return_value = mock_df
#     runner = CliRunner()
#     result = runner.invoke(main, ['--input_path', 'dummy_input.csv', '--out_dir', str(tmp_path)])
#     assert result.exit_code == 0
#     expected_files = ['train_df.csv', 'test_df.csv', 'X_train.csv', 'y_train.csv', 'X_test.csv', 'y_test.csv']
#     for file_name in expected_files:
#         assert (tmp_path / file_name).exists()

# # Test for ensuring correct price category creation in the DataFrame
# @patch('pandas.read_csv')
# def test_price_category_creation(mock_read_csv, tmp_path, mock_df):
#     mock_read_csv.return_value = mock_df
#     runner = CliRunner()
#     result = runner.invoke(main, ['--input_path', 'dummy_input.csv', '--out_dir', str(tmp_path)])
#     assert result.exit_code == 0
#     train_df = pd.read_csv(tmp_path / 'train_df.csv')
#     assert all(train_df['price_category'].notnull())

# # Test for confirming the removal of the 'price' column from training and testing feature sets
# @patch('pandas.read_csv')
# def test_column_removal_in_X_train_and_X_test(mock_read_csv, tmp_path, mock_df):
#     mock_read_csv.return_value = mock_df
#     runner = CliRunner()
#     result = runner.invoke(main, ['--input_path', 'dummy_input.csv', '--out_dir', str(tmp_path)])
#     assert result.exit_code == 0
#     X_train = pd.read_csv(tmp_path / 'X_train.csv')
#     X_test = pd.read_csv(tmp_path / 'X_test.csv')
#     assert 'price' not in X_train.columns and 'price' not in X_test.columns

# # Test for verifying correct data splitting
# @patch('pandas.read_csv')
# def test_data_splitting(mock_read_csv, tmp_path, mock_df):
#     mock_read_csv.return_value = mock_df
#     runner = CliRunner()
#     result = runner.invoke(main, ['--input_path', 'dummy_input.csv', '--out_dir', str(tmp_path)])
#     assert result.exit_code == 0
#     # Logic to verify data splitting would go here, e.g., checking file sizes or row counts

# # Test to check if NaN values in 'reviews_per_month' are correctly filled with 0
# @patch('pandas.read_csv')
# def test_fill_NaN_in_reviews_per_month(mock_read_csv, tmp_path, mock_df):
#     mock_read_csv.return_value = mock_df
#     runner = CliRunner()
#     result = runner.invoke(main, ['--input_path', 'dummy_input.csv', '--out_dir', str(tmp_path)])
#     assert result.exit_code == 0
#     train_df = pd.read_csv(tmp_path / 'train_df.csv')
#     # This assertion checks that there are indeed rows where 'reviews_per_month' has been filled with 0
#     assert (train_df['reviews_per_month'] == 0).any()
