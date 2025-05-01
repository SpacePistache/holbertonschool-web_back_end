#!/usr/bin/env python3
"""A module that lists all documents in a collection"""


def list_all(mongo_collection):
    """Lists all docs in mongo collection"""
    if mongo_collection is None:
        return []
    return list(mongo_collection.find())
