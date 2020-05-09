from mongoengine import connect
import urllib.request
import shutil
import pandas as pd
from mood_journal.consts import FORM_RESULTS_URL, RESULTS_CSV_PATH, MOOD_JOURNAL_DB_NAME, DB_HOST, DB_PORT, RESULTS_CSV_HEADERS_TO_DB_KEYS_MAPPING as head_key_map
import csv


def get_results_data_from_google_docs():
    """ Copy the up to date results CSV file from Google Docs to a local path """
    with urllib.request.urlopen(FORM_RESULTS_URL) as response, open(RESULTS_CSV_PATH, 'wb') as results_csv:
        shutil.copyfileobj(response, results_csv)


def convert_results_csv_to_rows_dict() -> dict:
    """
    Convert the results CSV to a dict containing it's rows
    :return: dict containing the results CSV's rows
    """
    db_keys_header = convert_csv_headers_to_db_keys()
    data_frame = pd.read_csv(RESULTS_CSV_PATH, header=0, names=db_keys_header)
    return data_frame.to_dict(orient='records')[1:]


def convert_csv_headers_to_db_keys() -> list:
    """
    Convert the results CSV headers to the DB keys, instead of the question strings
    It's purpose is to:
        1. prevents loading heavy shatty hebrew strings to memory
        2. prevents doing this conversion for each form later; saves running time
    :return: the header containing the DB keys, instead of the question strings
    """
    with open(RESULTS_CSV_PATH, 'r') as results_csv:
        csv_reader = csv.reader(results_csv)
        old_headers = next(csv_reader)

        new_headers = []
        for header in old_headers:
            try:
                new_headers.append(head_key_map[header])
            except KeyError:
                pass
    return new_headers
    pass

def connect_to_db():
    connect(db=MOOD_JOURNAL_DB_NAME, host=DB_HOST, port=DB_PORT)

# TODO - manage versions of the CSV, delete the ones that are older than a week, or keep 7 copies, pasten