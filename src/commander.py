import subprocess
import os

class commander:
    @staticmethod
    def execute(command):
        try:
            process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)

            #Launch the shell command:
            output, err = process.communicate()
            return output, err
        except subprocess.CalledProcessError as e:
            return "error", e

    @staticmethod
    def checkFile(filepath):
        return os.path.exists(filepath)

    @staticmethod
    def checkDir(dirPath):
        if os.path.isdir(dirPath):
            print("isdir")
        else:
            print("isnotdir")
        return os.path.isdir(dirPath)
