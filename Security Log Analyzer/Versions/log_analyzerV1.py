# Read a text file
# Count failed login attempts
# Shows suspicious IP addresses

with open(r"C:\Users\Brett\Python\Security Log Analyzer\security_log.txt", "r") as file:
    for line in file:
        line = line.strip()
        

        if "Failed" in line:
            print(line)


# Reading Data -> Processing Data -> Filtering Data -> Producing Output