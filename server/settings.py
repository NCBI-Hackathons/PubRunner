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

# Whether to use FTP or a local directory (that should be mounted as an FTP)
USE_FTP = False

### FTP
FTP_ADDRESS = ""
FTP_USERNAME = ""
FTP_PASSWORD = ""

### LOCAL DIRECTORY
LOCAL_DIRECTORY = ""
