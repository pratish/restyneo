import subprocess

class commander:
    @staticmethod
    def execute(command):
        process = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)

        #Launch the shell command:
        output = process.communicate()[0]
        #print(err)
        
        return output
