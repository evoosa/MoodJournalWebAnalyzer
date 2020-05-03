class DBPopulator():
    """ Creates the whole DB with it's collections from scratch """

    def __init__(self):
        # self.mongoengine_connection = # create the connection here
        pass

    def create_reason_field(self, reason_str):
        """ Create a sad / happy reason field, from a given reasons string """
        pass

    def create_document(self, csv_row_dict):
        """ Create the document from the dict retrieved from the results CSV row """
        # create as generic as you can, so you can use it for ALL of the DBs
        pass

    def add_document_to_db(self, db_document):
        """ Add a single document to the DB """
        # create as generic as you can, so you can use it for ALL of the DBs
        pass

    def create_forms_col(self):
        """ Create the collection containing the forms from scratch """
        pass

    def create_reasons_col(self):
        """ Create the collections containing the sad / happy reasons """
        pass
