with open(r"C:\Users\Brett\Python\Security Log Analyzer\security_log.txt", "r") as file:

    failed_counts = {}

    for line in file:
        line = line.strip()
        

        if "Failed" in line:
            parts = line.split()
            ip = parts[-1]

            if ip in failed_counts:
                failed_counts[ip] += 1
            else:
                failed_counts[ip] = 1

    for ip, count in failed_counts.items():
        if count >= 3:
            print("ALERT:", ip, "->", count, "failed logins")
        else:
            print(ip, "->", count)


# Create an empty dictionary for counting the IP addresses that failed
# Loop through the IPS for fail, add each IP with fail to dictioary with acount and increase count by occurence
# Add threshold alert
# Sort by most dangerous IP