from mongoengine import Document
from mongoengine.fields import IntField, StringField, ListField, DateTimeField, DateField, LazyReferenceField, MapField
from datetime import datetime
from .consts import FORMS_COLLECTION_NAME, HAPPY_REASONS_COLLECTION_NAME, SAD_REASONS_COLLECTION_NAME, DETOX_FAIL_REASONS_COLLECTION_NAME


# TODO - create an __enter__ and __exit__ for connect() and disconnect() funcs - clean your shit


class HappyReasons(Document):
    """ a class for the Reasons to be Happy today """
    modified_time = DateTimeField(default=datetime.now)
    happy_reason = StringField(required=True, primary_key=True)
    happy_rates_freq = MapField(IntField(required=False, default=0), required=False)
    meta = {'collection': HAPPY_REASONS_COLLECTION_NAME}


class SadReasons(Document):
    """ a class for the Reasons to be Sad today """
    modified_time = DateTimeField(default=datetime.now)
    sad_reason = StringField(required=True, primary_key=True)
    sad_rates_freq = MapField(IntField(required=False, default=0), required=False)
    meta = {'collection': SAD_REASONS_COLLECTION_NAME}


class DetoxFailReasons(Document):
    """ a class for the Reasons i Failed the Dopamine Detox today """
    modified_time = DateTimeField(default=datetime.now)
    detox_fail_reason = StringField(required=True, primary_key=True)
    detox_rates_freq = MapField(IntField(required=False, default=0), required=False)
    meta = {'collection': DETOX_FAIL_REASONS_COLLECTION_NAME}


class Forms(Document):
    """ Definition for the forms collection """
    timestamp = DateField(required=True, primary_key=True)
    submission_timestamp = DateTimeField(required=True)
    modified_time = DateTimeField(default=datetime.now)
    saddest = IntField(required=True)
    happiest = IntField(required=True)
    happy_reasons = ListField(LazyReferenceField(HappyReasons, reverse_delete_rule='DENY', dbref=True), required=True)
    sad_reasons = ListField(LazyReferenceField(SadReasons, reverse_delete_rule='DENY'), required=True, dbref=True)
    detox_prog = IntField(required=True)
    detox_pitfalls = ListField(LazyReferenceField(DetoxFailReasons, reverse_delete_rule='DENY'), required=True, dbref=True)
    to_keep = StringField(required=True)
    to_improve = StringField(required=True)
    meta = {'collection': FORMS_COLLECTION_NAME}
