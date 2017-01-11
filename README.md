![Logo](logo.png)

This project was part of the [January 2017 NCBI Hackathon](https://www.ncbi.nlm.nih.gov/news/11-17-2016-biomedical-informatics-hackathon/)

And here's an overview.

![Overview diagram](overview.png)

#What is PubRunner

PubRunner is a tool which runs locally on a user defined schedule allowing you to download latest PubMed abstracts,
run them through your favorite text mining tool and then uploads the results to Public FTP. Additionally the user has the option to post a link to their FTP on a dynamic list of tools running PubRunner.

#How to use PubRunner

##Installation options:

###Docker Option:
  1. Clone docker image set it up.


###Non-Docker Option:

1. Clone repo or Download to appropriate directory.
    Source code for PubRunner is found at https://github.com/NCBI-Hackathons/PubRunner/tree/master/server.

#Configuration
  - Update the JSON file (https://github.com/NCBI-Hackathons/PubRunner/blob/master/server/tools.json) with your tool's          information
  
  - Provide an example parameter file to demonstrate a configuration.

  - set the Cron Job

