#!/usr/bin/env python3
"""
Module for summing a list of floats.
Provides a function that returns the sum of all floats in a list.
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Sum a list of floats.

    Args:
        input_list (List[float]): The list of float numbers to sum.

    Returns:
        float: The sum of all floats in the list.
    """
    return sum(input_list)
