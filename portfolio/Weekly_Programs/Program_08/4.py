# 4. The Unix wc command counts the number of lines, words, and characters in a file.
# Write an implementation of this that takes a file name as a command-line
# argument, and then prints the number of lines and characters.
# Note: Linux (and Mac) users can use the "wc" command to check the results of their
# implementation.

import subprocess, sys

if len(sys.argv) > 1:
    fileName = sys.argv[1]
    lineCommand = f"wc -l {fileName}"
    wordCommand = f"wc -m {fileName}"

    result = subprocess.run(lineCommand, shell=True, capture_output=True, text=True)
    result2 = subprocess.run(wordCommand, shell=True, capture_output=True, text=True)
    print(f"There are {result.stdout.split()[0]} Number of Line and {result2.stdout.split()[0]} characters in {fileName} File.")
else:
    print("No input provided! Please specify two files.")
    print("python 4.py <FileName>")
