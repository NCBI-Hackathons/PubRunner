from subprocess import Popen, PIPE

class Runner:
    DB = "/path/to/DB"
    FTP = "/path/to/FTP"

    def __init__(self, toolName, command, main):
        self.toolName = toolName
        self.command = command
        self.main = main

    def run(self):
        process = Popen([self.command, "tools/"+self.toolName+"/"+self.main, "-i "+self.DB, "-o "+self.FTP], stdout=PIPE)
        (output, err) = process.communicate()
        exitCode = process.wait()
        print(exitCode)
