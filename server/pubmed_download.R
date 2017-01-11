#!/usr/bin/env RScript

install.packages("RCurl",repos='http://cran.us.r-project.org')
library(RCurl)
install.packages("httr",repos='http://cran.us.r-project.org')
library(httr)


setwd("/app/medline") # all xml files would be stored in medline dir

url = "ftp://ftp.ncbi.nlm.nih.gov/pubmed/baseline/" # update files
base_filenames = getURL(url, ftp.use.epsv = FALSE, dirlistonly = TRUE)
base_filenames<-strsplit(base_filenames, "\n")
base_filenames = unlist(base_filenames)
base_filenames
logname<-paste(format(Sys.time(),"%Y-%m-%d:%H:%M:%S"), "log", sep = ".")# format(Sys.time(), "%a-%b-%d %X %Y %Z")
for (filename1 in base_filenames){
    if (!file.exists(filename1))
        logname<-paste(format(Sys.time(),"%Y-%m-%d"), "log", sep = ".")
        write.table(filename1, file = logname, row.names = FALSE, append = TRUE, col.names = FALSE, sep = ", ")
        download.file(paste(url, filename1, sep = ""), paste( filename1,sep = ""))
}

url = "ftp://ftp.ncbi.nlm.nih.gov/pubmed/updatefiles/" # update files
filenames = getURL(url, ftp.use.epsv = FALSE, dirlistonly = TRUE)
filenames<-strsplit(filenames, "\n")
filenames = unlist(filenames)
filenames
logname<-paste(format(Sys.time(),"%Y-%m-%d"), "log", sep = ".")
for (filename in filenames){
    if (!file.exists(filename))
        #print(filename)
        #logname<-paste(format(Sys.time(),"%Y-%m-%d"), "log", sep = ".")
        #write.table(filename, file = logname, row.names = FALSE, append = TRUE, col.names = FALSE, sep = ", ")
        download.file(paste(url, filename, sep = ""), paste( filename,sep = ""))
}



#Sys.Date()
# logname>>paste(format(Sys.time(),"%Y-%m-%d), "log", sep = ".")"%Y-%m-%d %H:%M:%S"
# paste(format(Sys.time(), "%Y-%m-%d %I-%p"), "log", sep = ".")

#write.table(filename1, file = logname, row.names = FALSE, 
#            append = TRUE, col.names = TRUE, sep = ", ")