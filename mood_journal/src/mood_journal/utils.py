from mongoengine import connect

from .consts import MOOD_JOURNAL_DB_NAME, DB_HOST, DB_PORT


def get_results_from_google_docs():
    pass


def convert_csv_to_rows_dict():
    pass


def connect_to_db():
    connect(db=MOOD_JOURNAL_DB_NAME, host=DB_HOST, port=DB_PORT)
