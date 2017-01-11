#!/usr/bin/bash

# DL last data
R CMD BATCH pubmed_download.R

# Run PubRunner on it
python3 Run.py
