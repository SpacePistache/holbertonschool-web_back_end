#!/usr/bin/env python3
"""A module that uses regex to filter out unnecessary data"""
import re
import logging
from typing import List
from typing import Tuple


PII_FIELDS: Tuple[str, ...] = ("name", "email", "phone", "ssn", "password")


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """ Function to select and return key information"""
    filtered_data = rf"({'|'.join(fields)})=[^{separator}]*"
    return re.sub(filtered_data, rf"\1={redaction}", message)


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class"""

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """Class initialisation"""
        super().__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """Build string with correct format"""
        message = super().format(record)
        return filter_datum(self.fields, self.REDACTION,
                            message, self.SEPARATOR)
    
def get_logger() -> logging.Logger:
       """Creates a logger"""
       logger = logging.getLogger("user_data")
       logger.setLevel(logging.INFO)
       logger.propagate = False
       
       handler = logging.StreamHandler()
       handler.setFormatter(RedactingFormatter(list(PII_FIELDS)))
       logger.addHandler(handler)
       
       return logger
