#!/usr/bin/env python3
"""Additions list of ints and floats and returns their sum"""
from typing import Union, List


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """Additions list of floats and ints returns float

    Args:
        mxd_list (list[float, int]): list of float and int to addition.

    Return:
        float: The sum of ints and floats.
    """
    return float(sum(mxd_list))
