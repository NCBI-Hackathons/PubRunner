#!/usr/bin/bash
set -euxo pipefail

# DL last data
Rscript pubmed_download.R

# Run PubRunner on it
python3 Run.py
