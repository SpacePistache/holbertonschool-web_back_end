#!/usr/bin/env python3
"""A module using Simple Pagination"""


def index_range(page=1, page_size=15):
    """Returns a tuple containing start and end index"""
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return (start_index, end_index)
