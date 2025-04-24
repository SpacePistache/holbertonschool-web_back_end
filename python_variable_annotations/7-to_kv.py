#!/usr/bin/env python3
"""Module takes string, int or float as args and returns a tuple."""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float],) -> Tuple[str, float]:
    """Takes string, int and float and returns Tuple"""
    result = (k, v ** 2)
    return result
