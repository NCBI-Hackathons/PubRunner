FROM ubuntu:16.04
FROM php:7.0-apache
MAINTAINER kishorereddyanekalla@gmail.com

RUN apt-get update -y
RUN apt-get install -y python zip unzip wget curl bzip2
RUN apt-get install -y git curl apache2 php5

#create directory where application will be palced
RUN mkdir /webapp

#copy the application files 
COPY /server/ /webapp/server
COPY /Website/ /webapp/server

#Set working directory to webapp directory
WORKDIR /webapp
# port 
EXPOSE 80

#LABEL
LABEL com.example.version="0.0.1-beta"
CMD ["/usr/sbin/apache2ctl","-D","FOREGROUND"]

