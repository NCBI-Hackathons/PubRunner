#!/usr/bin/env RScript

library(Rcurl)
url = "ftp://ftp.ncbi.nlm.nih.gov/pubmed/updatefiles/"
filenames = getURL(url, ftp.use.epsv = FALSE, dirlistonly = TRUE)
filenames<-strsplit(filenames, "\n")
filenames = unlist(filenames)
filenames
for (filename in filenames) {
download.file(paste(url, filename, sep = ""), paste(getwd(), "/", filename,
sep = ""))
}