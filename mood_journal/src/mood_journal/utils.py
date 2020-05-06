from mongoengine import connect
import urllib.request
import shutil
from .consts import FORM_RESULTS_URL, RESULTS_CSV_PATH

from .consts import MOOD_JOURNAL_DB_NAME, DB_HOST, DB_PORT


def get_results_data_from_google_docs():
    """ copy the up to date results CSV file from Google Docs locally """
    with urllib.request.urlopen(FORM_RESULTS_URL) as response, open(RESULTS_CSV_PATH, 'wb') as results_csv:
        shutil.copyfileobj(response, results_csv)


def convert_csv_to_rows_dict():
    pass


def connect_to_db():
    connect(db=MOOD_JOURNAL_DB_NAME, host=DB_HOST, port=DB_PORT)
