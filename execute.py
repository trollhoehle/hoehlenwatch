# execute python module
# -*- coding: utf-8 -*-

__version__ = "0.2"

from subprocess import Popen, PIPE
import sys

class execute(object):
    def __init__(self,cmd):
        """ execute

        by Armin Jenewein <armin@arje.de>

        Will execute shell commands.
        Returns a tuple containing:
        0) stdout 1) stderr 2) returncode

        Example usage to get the returncode:

        from Execution import Executor
        e = Executor('yourcommand --some-args foo')
        e.run()
        print e.tup[2]

        """
        self.cmd = cmd
        self.run()
    def run(self):
        try:
            p = Popen(self.cmd, shell=True, stdin=PIPE, stdout=PIPE, stderr=PIPE)
            self.stdout, self.stderr = p.communicate()
            self.returncode = p.returncode
            self.tup = self.stdout, self.stderr, self.returncode
            return self.tup
        except:
            return os.path.relpath(__file__) + " " + sys.exc_info()[0]

if __name__ == '__main__':
    print("This script is intended to run as a module.")
    sys.exit(1)

