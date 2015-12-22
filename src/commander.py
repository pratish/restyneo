import subprocess
import os

class commander:
    @staticmethod
    def execute(command):
        process = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)

        #Launch the shell command:
        output, err = process.communicate()
        print(process.returncode)
        
        return output

    @staticmethod
    def checkFile(filepath):
        return os.path.exists(filepath)
