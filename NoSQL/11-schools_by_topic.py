#!/usr/bin/env python3
""" Module that returns the list of school having a specific topic"""


def schools_by_topic(mongo_collection, topic):
    """function returning schools that have certain topic"""
    return list(mongo_collection.find({ "topics": topic }))
