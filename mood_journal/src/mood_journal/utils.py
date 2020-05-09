from mongoengine import connect
import urllib.request
import shutil
import pandas as pd
from mood_journal.consts import FORM_RESULTS_URL, RESULTS_CSV_PATH, MOOD_JOURNAL_DB_NAME, DB_HOST, DB_PORT


def get_results_data_from_google_docs():
    """ Copy the up to date results CSV file from Google Docs to a local path """
    with urllib.request.urlopen(FORM_RESULTS_URL) as response, open(RESULTS_CSV_PATH, 'wb') as results_csv:
        shutil.copyfileobj(response, results_csv)


def convert_results_csv_to_rows_dict() -> dict:
    """
    Convert the results CSV to a dict containing it's rows
    :return: dict containing the results CSV's rows
    """
    data_frame = pd.read_csv(RESULTS_CSV_PATH, header=0)
    return data_frame.to_dict(orient='records')[1:]


def connect_to_db():
    connect(db=MOOD_JOURNAL_DB_NAME, host=DB_HOST, port=DB_PORT)
