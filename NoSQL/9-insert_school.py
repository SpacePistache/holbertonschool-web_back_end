#!/usr/bin/env python3
"""A module inserting new document in a collection based on kwargs"""


def insert_school(mongo_collection, **kwargs):
    """inserts new doc in collection"""
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
