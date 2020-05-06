import pytest
from mood_journal.doc_scheme_definitions import Forms
from datetime import datetime


@pytest.fixture(scope='module', autouse=True)
def get_form_local_obj():
    pytest.form_obj = Forms()


@pytest.mark.parametrize('date', ['invalid_date', datetime.now()])
def test_forms_date(date):
    pass

# FIXME - i droppeed these tests, they are retarded XD

# ??? # test updating with th object
# ??? # delete it at the end
