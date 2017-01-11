FROM ubuntu:latest
MAINTAINER docker@ekito.fr

RUN apt-get update && apt-get -y install cron r-base

# Add crontab file in the cron directory
ADD crontab /etc/cron.d/pubrunner

# Give execution rights on the cron job
RUN chmod 0644 /etc/cron.d/pubrunner

# Create the log file to be able to run tail
RUN touch /var/log/cron.log

# Run the command on container startup
CMD cron && tail -f /var/log/cron.log
