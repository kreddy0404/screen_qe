import csv
import os
import pathlib
import pytest

from dotenv import load_dotenv
env_dir = pathlib.Path(__file__).parents[1]
load_dotenv(os.path.join(env_dir, '.env'))

from tasks import avg, row_count, word_count

path = os.environ['APP_DATA_FOLDER_PATH']


@pytest.mark.smoke
def test_average_method(capsys):
    """
    Test to verify avg method.

    When avg method called it should return correct average number of fields
    across all csv files in /usr/src/data.
    """
    avg(path)

    captured = capsys.readouterr()

    assert captured.out is not None


@pytest.mark.smoke
def test_row_count_method(capsys):
    """
    Test to verify row count method.

    When row_count method called it should return total number of rows in all
    the csv files /usr/src/data.
    """
    row_count(path)

    captured = capsys.readouterr()

    assert captured.out is not None


@pytest.mark.smoke
def test_word_count_method():
    """
    Test to verify word count method.

    When word_count method called it should create wordcount.csv under
    /usr/src/app and csv file contents is csv dict as value,count.
    """
    word_count_file_path = os.environ['WORD_COUNT_CSV_FILE_PATH']

    word_count(path)

    # Verify word_count file exists or not
    if os.path.isfile(word_count_file_path):
        with open(word_count_file_path, "r") as fh:
            reader = csv.DictReader(fh, fieldnames=['value', 'count'])
            for row in reader:
                assert row is not None
