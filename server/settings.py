import os

"""
Definition of config parameters
"""

### Static, do not touch
VERSION = 0.2
ROOT = os.path.dirname(os.path.realpath(__file__)) + "/"

### General
DB = "medline/"
TOOLS = "tools/"
OUTPUT = "output/"
FAIL_LIMIT = 3

# Whether to use FTP or a local directory (that should be mounted as an FTP)
USE_FTP = False
FTP_ADDRESS = ""
FTP_USERNAME = ""
FTP_PASSWORD = ""

# Whether to copy to a local directory (that is mounted as a FTP or HTTP server)
USE_LOCAL_DIRECTORY = False
LOCAL_DIRECTORY = ""

# Whether to push to Zenodo
USE_ZENODO = True
ZENODO_AUTHOR = 'Joe Bloggs'
ZENODO_AUTHOR_AFFILIATION = 'University of New New York'

