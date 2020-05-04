from .consts import DB_HOST, DB_PORT, MOOD_JOURNAL_DB_NAME
from mongoengine import connect, Document
from mongoengine.fields import IntField, StringField, ListField, DateTimeField, DateField, ReferenceField, MapField

# TODO
# use mongoengine to create the objects which will be used to
# create the collections and to update them.
# use these objects in the db_populator class
# TODO - create an __enter__ and __exit__ for connect() and disconnect() funcs - clean your shit

connect(db=MOOD_JOURNAL_DB_NAME, host=DB_HOST, port=DB_PORT)


class Forms(Document):
    """ Definition for the forms collection """
    fill_date = DateField(required=True, primary_key=True)
    submission_timestamp = DateTimeField(required=True)
    saddest = IntField(required=True)
    happiest = IntField(required=True)
    happy_reasons = ListField(ReferenceField(HappyReasons, reverse_delete_rule='DENY'), required=True)
        # it is stored as DBRef automatcally !
    sad_reasons = ListField(ReferenceField(SadReasons, reverse_delete_rule='DENY'), required=True)
        # TODO - use this
        # https://docs.mongoengine.org/guide/defining-documents.html#one-to-many-with-listfields
    detox_progress = IntField(required=True)
    detox_pitfalls = ListField(ReferenceField(DetoxFailReasons, reverse_delete_rule='DENY'), required=True)
    to_keep = StringField(required=True)
    to_improve = StringField(required=True)


class HappyReasons(Document):
    """ a class for the Reasons to be Happy today """
    happy_reason = StringField(required=True, primary_key=True)
    happy_rates_freq = MapField(IntField(required=True, default=0), required=True)


class SadReasons(Document):
    """ a class for the Reasons to be Sad today """
    sad_reason = StringField(required=True, primary_key=True)
    sad_rates_freq = MapField(IntField(required=True, default=0), required=True)


class DetoxFailReasons(Document):
    """ a class for the Reasons i Failed the Dopamine Detox today """
    detox_fail_reason = StringField(required=True, primary_key=True)
    detox_rates_freq = MapField(IntField(required=True, default=0), required=True)
