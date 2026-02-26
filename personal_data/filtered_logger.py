#!/usr/bin/env python3
"""A module that uses regex to filter out unnecessary data"""
import re
from typing import List

def filter_datum(fields: List[str], redaction: str, message: str, separator: str) -> str:
	""" Function to select and return key information"""
	filtered_data = rf"({'|'.join(fields)})=[^{separator}]*"
	return re.sub(filtered_data, rf"\1={redaction}", message)
