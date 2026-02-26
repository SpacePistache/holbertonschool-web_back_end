#!/usr/bin/env python3
"""A module that uses regex to filter out unnecessary data"""
import re

def filter_datum(fields, redaction, message, seperator):
	""" Function to select and return key information"""
	filtered_data = rf"({'|'.join(fields)})=[^{seperator}]*"
	return re.sub(filtered_data, rf"\1={redaction}", message)
