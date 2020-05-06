import pytest
from mood_journal.utils import connect_to_db
from mongoengine import connect, disconnect


@pytest.fixture(scope='session', autouse=True)
def mongoengine_db_connect():
    print('\nConnecting to DB..\n')
    yield connect_to_db()
    print('\nDisconnecting from DB..\n')
    disconnect()

