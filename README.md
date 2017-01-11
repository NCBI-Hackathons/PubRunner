![Logo](logo.png)

This project was part of the [January 2017 NCBI Hackathon](https://www.ncbi.nlm.nih.gov/news/11-17-2016-biomedical-informatics-hackathon/)

And here's an overview.

![Overview diagram](overview.png)

#What is PubRunner

PubRunner is a framework which runs on a user defined schedule allowing you to download latest PubMed abstracts,
run them through your favorite text mining tool and then uploads the results to Public FTP. Additionally the user has the option to post a link to their FTP on the public PubRunner website (www.pubrunner.org).

#How to use PubRunner

##Installation options:

###Docker Option:
  1. `docker pull ftp_pubrunner` command to pull the image from the DockerHub (hyperlink
  2. `docker run -p 80:80 ftp_pubrunner` Run the docker image from the master shell script
  3. 


###Non-Docker Option:

1. Clone repo or Download to appropriate directory.
    Source code for PubRunner is found at [server/](server/)

##Configuration
  - Update the JSON file [server/tools.json](https://github.com/NCBI-Hackathons/PubRunner/blob/master/server/tools.json) with your tool's          information
  -  add ftp credentials to [server/settings.py](server/settings.py)
  
  - Provide an example parameter file to demonstrate a configuration.

  - set the Cron Job

