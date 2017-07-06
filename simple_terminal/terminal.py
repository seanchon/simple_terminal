import os
import subprocess


class Terminal(object):
    def __enter__(self, *args, **kwargs):
        return self

    def __exit__(self, *args, **kwargs):
        pass

    def command(self, command):
        if command.split(' ')[0] == 'cd':
            self.chdir(command.split(' ')[1])
            output = None
            return self.command('pwd')
        else:
            proc = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
            output = proc.stdout.readlines()
            output = [x.decode('utf8').strip() for x in output]
            proc.wait()
            return list(output)

    def chdir(self, directory):
        if directory[0] == '~':
            directory = os.path.expanduser(directory)
        os.chdir(directory)
