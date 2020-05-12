from mood_journal import utils
from mood_journal.doc_schemes import Forms, SadReasons, HappyReasons, DetoxFailReasons
from mood_journal import consts
from mongoengine.base.metaclasses import TopLevelDocumentMetaclass


class DBPopulator():
    """ Creates the whole DB with it's collections from scratch """

    def __init__(self):
        utils.get_results_data_from_google_docs()
        utils.connect_to_db()
        self.forms_dicts = utils.convert_results_csv_to_rows_dict()

    ### Create Documents ###

    def _create_form_document(self, parsed_row_dict) -> Forms:
        """ Create the document from the dict retrieved from the results CSV row """
        form_doc = Forms()
        for field in parsed_row_dict:
            if field in consts.REASON_FIELDS:
                value = parsed_row_dict[field]
                field_value_unstripped = value.split(',') if not type(value) is float else []
                field_value = [reason.strip() for reason in field_value_unstripped]
            else:
                field_value = parsed_row_dict[field]
            setattr(form_doc, field, field_value)
        return form_doc

    def _create_reason_document(self, doc_scheme: TopLevelDocumentMetaclass, reason_key, reason_value):
        """
        Create a Reason Document
        :param doc_scheme: the document scheme
        :param reason_key: the name of the reason field key
        :param reason_value: the value of the reason field
        :return: a document instance, of the reason_doc_scheme Document type
        """
        reason_doc = doc_scheme()
        setattr(reason_doc, reason_key, reason_value)
        return reason_doc

    ### Populate Collections With Forms ###

    def populate_forms_collection(self):
        """ Create the collection containing the forms from scratch """
        for form_dict in self.forms_dicts:
            form_doc = self._create_form_document(form_dict)
            form_doc.save()

    def _populate_reasons_collection(self, doc_scheme, key_name_in_forms_col, key_name_in_reasons_col):
        """
        Create the collections containing the different reasons 
        :param key_name_in_forms_col: the name of the reasons key, as specified in the Forms collection
        """
        unique_reasons = Forms.objects.distinct(key_name_in_forms_col)
        for reason in unique_reasons:
            reason_doc = self._create_reason_document(doc_scheme, key_name_in_reasons_col, reason)
            reason_doc.save()

    def populate_happy_reasons_collection(self):
        """ Create the Happy Reasons collection """
        self._populate_reasons_collection(HappyReasons, consts.HAPPY_REASONS_COLLECTION_NAME, consts.HAPPY_REASONS_FIELD_NAME)

    def populate_sad_reasons_collection(self):
        """ Create the Sad Reasons collection """
        self._populate_reasons_collection(SadReasons, consts.SAD_REASONS_COLLECTION_NAME, consts.SAD_REASONS_FIELD_NAME)

    def populate_detox_fail_reasons_collection(self):
        """ Create the Detox Failure Reasons collection """
        self._populate_reasons_collection(DetoxFailReasons, consts.DETOX_FAIL_REASONS_COLLECTION_NAME, consts.DETOX_FAIL_REASONS_FIELD_NAME)
