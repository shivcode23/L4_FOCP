# 2. The Unix diff command compares two files and reports the dierences, if any.
# Write a simple implementation of this that takes two file names as command-line
# arguments and reports whether or not the two files are the same. (Define "same" as
# having the same contents.)



import subprocess, sys

if len(sys.argv) > 2:
    firstFileName = sys.argv[1]
    secondFileName = sys.argv[2]
    command = f"diff {firstFileName} {secondFileName}"
    print("The file content Along with Line number.")

    # Run the diff command with shell=True
    result = subprocess.run(command, shell=True, capture_output=True, text=True)

    # Check the return code
    if result.returncode == 0:
        print("Both files are the same.")
    elif result.returncode == 1:
        print("Files are different:\n")
        print(result.stdout)  # Print the actual diff output
    else:
        print("An error occurred:", result.stderr)
else:
    print("No input provided! Please specify two files.")
