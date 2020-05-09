from mood_journal.utils import connect_to_db, get_results_data_from_google_docs, convert_results_csv_to_rows_dict
from mood_journal.doc_schemes import Forms
from mood_journal.consts import REASON_FIELDS
import math


class DBPopulator():
    """ Creates the whole DB with it's collections from scratch """

    def __init__(self):
        get_results_data_from_google_docs()
        connect_to_db()
        self.forms_dicts = convert_results_csv_to_rows_dict()

    def create_form_document(self, parsed_row_dict) -> Forms:
        """ Create the document from the dict retrieved from the results CSV row """
        form_doc = Forms()
        for field in parsed_row_dict:
            if field in REASON_FIELDS:
                value = parsed_row_dict[field]
                field_value = value.split(',') if not type(value) is float else []
            else:
                field_value = parsed_row_dict[field]
            setattr(form_doc, field, field_value)
        return form_doc

    def populate_forms_collection(self): # FIXME
        """ Create the collection containing the forms from scratch """
        for form_dict in self.forms_dicts:
            form_doc = self.create_form_document(form_dict)
            form_doc.save()
        pass

    def populate_reasons_collection(self):
        """ Create the collections containing the sad / happy reasons """
        # query the db in a way youll get a list of unique values for the sad/happy reasons already added!
        pass
