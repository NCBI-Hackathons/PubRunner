import os

"""
Definition of config parameters
"""

### Static, do not touch
VERSION = 0.1
ROOT = os.path.dirname(os.path.realpath(__file__)) + "/"

### General
DB = "medline/"
TOOLS = "tools/"
OUTPUT = "output/"
FAIL_LIMIT = 3

### FTP
FTP_ADDRESS = ""
FTP_USERNAME = ""
FTP_PASSWORD = ""

### WEBSITE
WEB_ADDRESS = "ftp://www.pubrunner.com"
WEB_USERNAME = "pubrunner"
WEB_PASSWORD = "AwZR%ar75JEhNIeh"
