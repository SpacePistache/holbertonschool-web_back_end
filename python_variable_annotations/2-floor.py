#!/usr/bin/env python3
"""
A module employing the floor function rounding down to an int
"""
import math


def get_floored(a: float) -> int:
    """
        Return: the number rounded down from float to int.

        Args: a (float) the number to round down or 'floor'
        
        Returns: (int) the number that has been rounded down.

    """
    return math.floor(a)
