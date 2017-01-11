#!/bin/sh

echo "cron job inititaed at $(date +"%m-%d-%y")"

0 6 * * * Rscript ~/home/ubuntu/kishore/pubmed_download.R > ~/home/ubuntu/CronLogs 2>&1
