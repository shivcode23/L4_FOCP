# 1. The Unix nl command prints the lines of a text file with a line number at the start
# of each line. (It can be useful when printing out programs for dry runs or white-box
# testing). Write an implementation of this command. It should take the name of the
# files as a command-line argument.


import os, sys

if len(sys.argv) > 1:
    fileName = sys.argv[1:][0]
    command = "nl "+fileName
    print("The file content Along with Line number .")
    os.system(command)
else:
    print("No input Provided !")