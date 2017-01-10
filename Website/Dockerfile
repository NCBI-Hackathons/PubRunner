FROM php:7.0-apache
FROM ubuntu:16.04

RUN apt-get update -y
RUN apt-get install -y python zip unzip wget curl bzip2
CMD ["/bin/bash"]

# 
#COPY src/ /Users/kra804/Documents/Projects/PubRunner/PubRunner/Website/
#RUN apt-get install -y git curl apache2 php5
#docker run -d -p 80:80 --name my-apache-php-app -v "$PWD":/Users/kra804/Documents/Projects/PubRunner/PubRunner/Website/ php:7.0-apache # to run the files #without dockerfile 