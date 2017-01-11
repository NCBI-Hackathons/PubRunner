FROM ubuntu:latest
MAINTAINER nicolas.fiorini@nih.gov

RUN apt-get update && apt-get -y install cron
RUN apt-get -y install r-base
RUN apt-get -y install libcurl4-gnutls-dev
RUN apt-get -y install openssl

# Add crontab file in the cron directory
ADD crontab /etc/cron.d/pubrunner
ADD . /app

# Give execution rights on the cron job
RUN chmod 0644 /etc/cron.d/pubrunner

# Create the log file to be able to run tail
RUN touch /var/log/cron.log

# Run the command on container startup
#CMD cron && tail -f /var/log/cron.log
CMD Rscript /app/pubmed_download.R
