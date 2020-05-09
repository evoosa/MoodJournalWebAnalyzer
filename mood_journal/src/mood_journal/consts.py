from datetime import datetime
import os

DB_HOST = '192.168.223.128'
DB_PORT = 27017

MOOD_JOURNAL_DB_NAME = 'mj'
FORMS_COLLECTION_NAME = 'forms'
SAD_REASONS_COLLECTION_NAME = 'sad_reasons'
HAPPY_REASONS_COLLECTION_NAME = 'happy_reasons'
DETOX_FAIL_REASONS_COLLECTION_NAME = 'detox_fail_reasons'

MOOD_JOURNAL_FORM_ID = '1UWZwqU-RE8WvqWc5NOHNhhWGzbHFOtkDymwwcD938ww'
FORM_RESULTS_URL = 'https://docs.google.com/spreadsheets/d/{form_id}/export?exportFormat=csv'.format(form_id=MOOD_JOURNAL_FORM_ID)

WIN_RESULTS_DIR = 'C:\\Users\\evoosa\\Desktop\\Projects\\Python\\MoodJournalWebAnalyzer\\FoolingAround'
LIN_RESULTS_DIR = '/tmp/' # FIXME to a legit path thnks

RESULTS_DIR = WIN_RESULTS_DIR if os.name == 'nt' else LIN_RESULTS_DIR

RESULTS_CSV_FILENAME = 'form_results-{curr_datetime}.csv'.format(curr_datetime=datetime.now().strftime("%m-%d-%Y_%H-%M"))
RESULTS_CSV_PATH = os.path.join(RESULTS_DIR, RESULTS_CSV_FILENAME)

RESULTS_CSV_HEADERS_TO_DB_KEYS_MAPPING = {
    'Timestamp': 'sub_timestamp',
    'מה ההכי נמוך שהיה לך היום?': 'saddest',
    'מה תרם לתחושה השלילית?': 'sad_reasons',
    'מה ההכי גבוה שהיה לך היום?': 'happiest',
    'מה תרם לתחושה החיובית?': 'happy_reasons',
    'האם את מרוצה מההתקדמות בגמילה היום?': 'detox_prog',
    'מה הפיל אותך?': 'detox_pitfalls',
    'מה תשפרי להבא?': 'to_improve',
    'מה תשמרי להבא?': 'to_keep',
    'על איזה תאריך מילאת?': 'timestamp'
}
