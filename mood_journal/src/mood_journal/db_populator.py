from mood_journal.utils import connect_to_db, get_results_data_from_google_docs, convert_results_csv_to_rows_dict
from mood_journal.doc_schemes import Forms
from mood_journal.consts import REASON_FIELDS


class DBPopulator():
    """ Creates the whole DB with it's collections from scratch """

    def __init__(self):
        get_results_data_from_google_docs()
        connect_to_db()
        self.db_objs_dict = convert_results_csv_to_rows_dict()

    def _create_reason_field(self, reasons_str) -> list: # FIXME!!!!!!!
        """ Create a sad / happy reason field, from a given reasons string """
        # FIXME - it has to return DBrefs :((((
        return reasons_str.split(',')

    def create_form_document(self, parsed_row_dict) -> Forms:
        """ Create the document from the dict retrieved from the results CSV row """
        form_doc = Forms()
        for field in parsed_row_dict:
            if field in REASON_FIELDS:
                field_value = self._create_reason_field(parsed_row_dict[field])
            else:
                field_value = parsed_row_dict[field]
            setattr(form_doc, field, field_value)
        return form_doc

    def populate_forms_collection(self):
        """ Create the collection containing the forms from scratch """
        # TODO - create a field name to Q name mapping file dictionary
        # for form in the forms dict:
        # db_form = create_form_document
        pass

    def populate_reasons_collection(self):
        """ Create the collections containing the sad / happy reasons """
        # query the db in a way youll get a list of unique values for the sad/happy reasons already added!
        pass
