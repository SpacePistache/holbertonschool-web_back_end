#!/usr/bin/env python3
"""Takes float multiplier as arg returns function that multiplies float"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Function returns a function multiplying floats"""
    return lambda aupif: aupif * multiplier
