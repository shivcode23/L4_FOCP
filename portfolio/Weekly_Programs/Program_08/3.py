# 3. The Unix grep command searches a file and outputs the lines in the file that
# contain a certain pattern. Write an implementation of this. It will take two
# command-line arguments: the first is the string to look for, and the second is the
# file name. The output should be the lines in the file that contain the string.

import os, sys

if len(sys.argv) > 2:
    search = sys.argv[1:][0]
    fileName = sys.argv[1:][1]
    command = "cat "+fileName + " | grep "+ search
    print(command)
    os.system(command)
else:
    print("No input Provided !")
    print("Usage: python 3.py SEARCH-STRING FileName")