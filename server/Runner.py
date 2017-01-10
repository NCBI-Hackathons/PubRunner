from settings import *
import os
from subprocess import run, PIPE
import datetime
import resource

class Runner:
    def __init__(self, params):
        # Load everything from the object translated from the JSON file
        self.__dict__ = params

    def run(self):
        self.successed = False
        tries = 0
        while not self.successed and tries < FAIL_LIMIT:
            try:
                destination = ROOT+FTP+self.name+"/"+self.version+"/"

                # Delete previous contents
                for f in os.listdir(destination):
                    fPath = os.path.join(destination, f)
                    try:
                        if os.path.isfile(fPath):
                            os.unlink(fPath)
                    except Exception as e:
                        print(e)

                # Set log files
                stderrf = open(destination+"std.err","wb")
                stdoutf = open(destination+"std.out","wb")
                process = run([self.command,
                              "tools/"+self.name+"/"+self.version+"/"+self.main,
                              "-i"+ROOT+DB,
                              "-o"+destination],
                              stdout=stdoutf,
                              stderr=stderrf,
                              timeout=self.timeout,
                              check=True)
                self.successed = True
            except:
                tries += 1
                pass
            self.lastRun = datetime.datetime.now().strftime("%m-%d-%Y")
