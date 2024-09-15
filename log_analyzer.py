# Open and read through each line of the file
def read_log_file(log_file):
    with open(log_file, 'r') as file:
        logs = file.readlines()
    return logs

# Flag lines with "ERROR"
def flag_unusual_activity(logs):
    flagged = []
    for line in logs:
        if "ERROR" in line:
            flagged.append(line)
    return flagged

# Write flagged entries to an output file
def write_flagged_entries(flagged_logs, output_file):
    with open(output_file, 'w') as file:
        for log in flagged_logs:
            file.write(log)

logs = read_log_file('log_file.txt')

flagged_logs = flag_unusual_activity(logs)

write_flagged_entries(flagged_logs, 'flagged_logs.txt')
