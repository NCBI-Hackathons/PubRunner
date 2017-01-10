import os

"""
Definition of config parameters
"""

### General
VERSION = 0.1

DB = "medline/"
TOOLS = "tools/"
OUTPUT = "output/"
ROOT = os.path.dirname(os.path.realpath(__file__)) + "/"
FAIL_LIMIT = 3

### FTP
FTP_ADDRESS = ""
FTP_USERNAME = ""
FTP_PASSWORD = ""
