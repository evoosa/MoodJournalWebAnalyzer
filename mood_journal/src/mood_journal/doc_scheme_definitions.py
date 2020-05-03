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
    fill_date = DateField(required=True, unique=True, primary_key=True)
    submission_timestamp = DateTimeField(required=True)
    saddest = IntField(required=True)
    happiest = IntField(required=True)
    happy_reasons = ListField(ReferenceField(HappyReasons, reverse_delete_rule='DENY'), required=True)
    # it is stored as DBRef automatcally
    sad_reasons = ListField(ReferenceField(SadReasons, reverse_delete_rule='DENY'), required=True)
    # TODO - use this
    # https://docs.mongoengine.org/guide/defining-documents.html#one-to-many-with-listfields
    detox_progress = IntField(required=True)
    detox_pitfalls = ListField(ReferenceField(DetoxPitchfallReasons, reverse_delete_rule='DENY'), required=True)
    to_keep = StringField(required=True)
    to_improve = StringField(required=True)


class Reasons(Document):
    """ a class for other Reason classes to derive from """
    reason = StringField(required=True, unique=True, primary_key=True)
    rating_frequency = MapField(IntField(required=True, default=0), required=True)
    pass


class HappyReasons(Reasons):
    super()


class SadReasons(Reasons):
    super()


class DetoxPitchfallReasons(Reasons):
    super()
