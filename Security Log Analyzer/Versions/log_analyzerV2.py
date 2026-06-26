with open(r"C:\Users\Brett\Python\Security Log Analyzer\security_log.txt", "r") as file:
    for line in file:
        line = line.strip()
        

        if "Failed" in line:
            parts = line.split()
            print(parts[-1])



# Split the line into parts
# Grab the IP at the end