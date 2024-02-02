f = open("linkedin_learning/automation/inputFile.txt", "r")
pass_file = open("linkedin_learning/automation/pass_file.txt", "w")
failed_file = open("linkedin_learning/automation/fail_file.txt", "w")
count = 0
for line in f:
    line_split = line.split()
    if line_split[2] == "P":
        pass_file.write(line)
    elif line_split[2] == "F":
        failed_file.write(line)

f.close()
pass_file.close()
failed_file.close()