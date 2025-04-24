#!/usr/bin/env python3
"""Module defining a func erturning list of tuples with elements and length"""
from typing import Sequence, List, Tuple, Iterable


def element_length(lst: Iterable[Sequence]) -> [Tuple[Sequence, int]]:
    """Takes iterable list of sequences and returns list of tuples"""
    return [(i, len(i)) for i in lst]
