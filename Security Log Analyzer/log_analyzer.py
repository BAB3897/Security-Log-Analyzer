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

    print("\n--- Failed Login Summary ---\n")

    for ip, count in sorted(failed_counts.items(), key=lambda x: x[1], reverse=True):

        if count >= 3:
            print(f"ALERT:, {ip} ->, {count} failed login attempts")
        else:
            print(f"{ip}, -> {count} failed login attempts")

# Goal: Reading Data -> Processing Data -> Filtering Data -> Producing Output
# 1. Split the line into parts, Grab the IP at the end
# 2. Create an empty dictionary for counting the IP addresses that failed, Loop through the IPs for fail, add each IP with fail to dictioary with acount and increase count by occurence
# 3. Add threshold alert, Sort by most dangerous IP
# 4. Clean up string formatting, Sort Dictionary Results, Sort by value count using lambda