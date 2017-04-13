from settings import *
import os
from subprocess import run, PIPE
import datetime
import resource
import shutil
import sys
import traceback
from FTPClient import *

class Runner:
    def __init__(self, params):
        # Load everything from the object translated from the JSON file
        self.__dict__ = params

    def run(self):
        self.success = False
        tries = 0
        while not self.success and tries < FAIL_LIMIT:
            # Make sure that the directory for output is created
            destination = ROOT+OUTPUT+self.name+"/"+self.version+"/"
            if not os.path.isdir(destination+"PubRunnerLogs/"):
                os.makedirs(destination+"PubRunnerLogs/")

            try:


                # Set log files
                stderrf = open(destination+"PubRunnerLogs/std.err","wb")
                stdoutf = open(destination+"PubRunnerLogs/std.out","wb")
                process = run([self.command,
                              "tools/"+self.name+"/"+self.version+"/"+self.main,
                              "-i"+ROOT+DB,
                              "-o"+destination],
                              stdout=stdoutf,
                              stderr=stderrf,
                              timeout=self.timeout,
                              check=True)

                self.success = True
            except:
                #print (Exception, err)
                traceback.print_exc()
                tries += 1
                pass
            self.lastRun = datetime.datetime.now().strftime("%m-%d-%Y")

            # Also log PubRunner data information
            with open(destination+"PubRunnerLogs/info.txt", "w") as f:
                f.write("PubRunner version: "+str(VERSION)+"\nRun on "+self.lastRun)

    def pushToFTP(self):
        assert FTP_ADDRESS != '', 'FTP address must be completed in the setting.py file'
        assert FTP_USERNAME != '', 'FTP username must be completed in the setting.py file'
        assert FTP_PASSWORD != '', 'FTP password must be completed in the setting.py file'

        output = ROOT+OUTPUT+self.name+"/"+self.version+"/"

	# N.B. This doesn't recursively copy files

        # Push output folder contents
        # 1. Set up FTP
        ftpc = FTPClient(FTP_ADDRESS, FTP_USERNAME, FTP_PASSWORD)
        # 2. Go the the right directory, or create it
        ftpc.cdTree(self.name+"/"+self.version+"/")
        # 3. Upload all files
        for f in os.listdir(output):
            fPath = os.path.join(output, f)
            if os.path.isfile(fPath):
                ftpc.upload(output, f)
        # 4. Close session
        ftpc.quit()

        # Delete that content locally
        for f in os.listdir(output):
            fPath = os.path.join(output, f)
            try:
                if os.path.isfile(fPath):
                    os.unlink(fPath)
            except Exception as e:
                print(e)
    
    def pushToLocalDirectory(self):
        assert LOCAL_DIRECTORY != '', 'Local directory must be completed in the setting.py file'

        output = ROOT+OUTPUT+self.name+"/"+self.version+"/"

        destDir = LOCAL_DIRECTORY.rstrip("/")+"/"+self.name+"/"+self.version+"/"
        if not os.path.isdir(destDir):
            os.makedirs(destDir)

	# N.B. This doesn't recursively copy files
        for f in os.listdir(output):
            src = os.path.join(output, f)
            dst = os.path.join(destDir, f)
            if os.path.isfile(src):
                shutil.copyfile(src,dst)

        # Delete that content locally
        for f in os.listdir(output):
            fPath = os.path.join(output, f)
            try:
                if os.path.isfile(fPath):
                    os.unlink(fPath)
            except Exception as e:
                print(e)

