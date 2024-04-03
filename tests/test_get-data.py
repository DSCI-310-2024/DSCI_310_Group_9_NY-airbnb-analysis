import os
import sys
import pandas as pd
import pytest
from click.testing import CliRunner
from unittest.mock import patch
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from scripts.fetch_data_and_export import create_dir_if_not_exists, main

# Test the create_dir_if_not_exists function
def test_create_dir_if_not_exists(tmp_path):
    directory = tmp_path / "new_directory"
    assert not directory.exists()
    create_dir_if_not_exists(str(directory))
    assert directory.exists()
    
def test_main_valid_input(tmp_path):
    with patch('pandas.read_csv', return_value=pd.DataFrame({'test': [1, 2, 3]})):
        with patch('pandas.DataFrame.to_csv') as mocked_to_csv:
            runner = CliRunner()
            result = runner.invoke(main, ['--data_url', 'http://data.insideairbnb.com/united-states/ny/new-york-city/2023-12-04/visualisations/listings.csv', '--out_dir', str(tmp_path)])
            assert result.exit_code == 0
            assert "File Saved!" in result.output
            # Verify that to_csv was called to ensure the data saving logic was triggered
            mocked_to_csv.assert_called_once()
            mocked_to_csv.assert_called_with(os.path.join(str(tmp_path), 'airbnb_data_2023.csv'), index=False)

# Test handling of invalid URL
def test_main_invalid_url(tmp_path):
    with patch('pandas.read_csv', side_effect=Exception("Invalid URL")):
        runner = CliRunner()
        result = runner.invoke(main, ['--data_url', 'http://invalidurl.com/data.csv', '--out_dir', str(tmp_path)])
        assert result.exit_code != 0
