#!/usr/bin/env RScript

pkgs<-c("RCurl","httr")
for(i in 1:length(pkgs)){
  if(require(pkgs[i], character.only = TRUE)==FALSE){ install.packages(pkgs[i]);library(pkgs[i], character.only = TRUE)}
  else { library(pkgs[i],character.only = TRUE)}
}

# updates data 

#baselinedata<-"/home/ubuntu/PubRunner/Data/ftp_download/pubmed/baseline" # keep all files in a dir ?
#updatesdata<-"/home/ubuntu/PubRunner/Data/ftp_download/pubmed/updates" # else separately stored 
# baseline xml files 
url = "ftp://ftp.ncbi.nlm.nih.gov/pubmed/baseline" # update files
base_filenames = getURL(url, ftp.use.epsv = FALSE, dirlistonly = TRUE)
base_filenames<-strsplit(base_filenames, "\n")
base_filenames = unlist(base_filenames)
base_filenames
for (filename1 in base_filenames){
    if (!file.exists(filename1))
    	download.file(paste(url, filename1, sep = ""), paste( filename1,sep = "")) 
}

url = "ftp://ftp.ncbi.nlm.nih.gov/pubmed/updatefiles/" # update files
filenames = getURL(url, ftp.use.epsv = FALSE, dirlistonly = TRUE)
filenames<-strsplit(filenames, "\n")
filenames = unlist(filenames)
filenames
for (filename in filenames){
    if (!file.exists(filename))
    	download.file(paste(url, filename, sep = ""), paste( filename,sep = "")) 
}