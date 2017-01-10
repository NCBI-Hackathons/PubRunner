from ftplib import FTP

class FTPClient:

    def __init__(self, address, user, passw):
        self.ftp = FTP(address, user, passw)

    def cdTree(self, currentDir):
        if currentDir != "":
            try:
                self.ftp.cwd(currentDir)
            except IOError:
                cdTree("/".join(currentDir.split("/")[:-1]))
                self.ftp.mkd(currentDir)
                self.ftp.cwd(currentDir)

    def upload(self, path, filename):
        fh = open(os.path.join(path, filename),'rb')
        session.storbinary('STOR '+filename, fh)
        fh.close()

    def quit(self):
        self.ftp.quit()
