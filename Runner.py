import os
from subprocess import run, PIPE
from threading import Timer
import datetime

class Runner:
    DB = "medline/"
    FTP = "ftp/"
    root = os.path.dirname(os.path.realpath(__file__)) + "/"

    def __init__(self, name, command, main, timeout, successed, lastRun, active):
        self.name = name
        self.command = command
        self.main = main
        self.timeout = timeout
        self.successed = successed
        self.lastRun = lastRun
        self.active = active

    def run(self):
        self.successed = False
        tries = 0
        while not self.successed and tries < 5:
            try:
                process = run([self.command, "tools/"+self.name+"/"+self.main, "-i"+self.root+self.DB, "-o"+self.root+self.FTP], stdout=PIPE, stderr=PIPE, timeout=self.timeout, check=True)
                self.successed = True
            except:
                tries += 1
                pass
            self.lastRun = datetime.datetime.now().strftime("%m-%d-%Y")
