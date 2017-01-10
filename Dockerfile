FROM ubuntu:16.04

FROM php:7.0-apache

MAINTAINER kishorereddyanekalla@gmail.com

RUN apt-get update -y
RUN apt-get install -y python zip unzip wget curl bzip2
CMD ["/bin/bash"]

RUN apt-get install -y git curl apache2 php5

# chcek for th updates if any 
RUN apt-get update

# apt -get install php......

#LABEL
LABEL com.example.version="0.0.1-beta"

CMD ["/bin/bash"]
#opening ports
EXPOSE 80