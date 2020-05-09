from mood_journal.utils import connect_to_db, get_results_data_from_google_docs, convert_results_csv_to_rows_dict

class DBPopulator():
    """ Creates the whole DB with it's collections from scratch """

    def __init__(self):
        get_results_data_from_google_docs()
        self.mongoengine_conn = connect_to_db()
        self.db_objs_dict = convert_results_csv_to_rows_dict()

    def create_reason_field(self, reason_str):
        """ Create a sad / happy reason field, from a given reasons string """
        pass

    def create_form_document(self, parsed_row_dict):
        """ Create the document from the dict retrieved from the results CSV row """
        form_doc = {}
        # for field in parsed :
            #
            # if field is sad/happy field:
                # change the field using 'create_reason_field'
            # if
        pass

    def add_document_to_db(self, db_document):
        """ Add a single document to the DB """
        # create as generic as you can, so you can use it for ALL of the DBs
        pass

    def populate_forms_col(self):
        """ Create the collection containing the forms from scratch """
        # TODO - create a field name to Q name mapping file dictionary
        # for form in the forms dict:
            # db_form = create_form_document


        pass

    def populate_reasons_col(self):
        """ Create the collections containing the sad / happy reasons """
        # query the db in a way youll get a list of unique values for the sad/happy reasons already added!
        pass
