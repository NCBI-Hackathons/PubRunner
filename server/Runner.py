from settings import *
import os
from subprocess import run, PIPE
from threading import Timer
import datetime

class Runner:
    def __init__(self, params):
        # Load everything from the object translated from the JSON file
        self.__dict__ = params

    def run(self):
        self.successed = False
        tries = 0
        while not self.successed and tries < 5:
            try:
                process = run([self.command, "tools/"+self.name+"/"+self.main, "-i"+ROOT+DB, "-o"+ROOT+FTP+self.name+"/"], stdout=PIPE, stderr=PIPE, timeout=self.timeout, check=True)
                self.successed = True
            except:
                tries += 1
                pass
            self.lastRun = datetime.datetime.now().strftime("%m-%d-%Y")
