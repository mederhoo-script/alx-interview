#!/usr/bin/python3
'''A script that reads stdin line by line and computes metrics.'''

import sys

# Dictionary to store the count of each status code
status_counts = {'200': 0, '301': 0, '400': 0, '401': 0,
                 '403': 0, '404': 0, '405': 0, '500': 0}

# Variable to keep track of the total file size
total_file_size = 0

# Counter to track the number of lines processed
line_counter = 0

try:
    for log_entry in sys.stdin:
        log_parts = log_entry.split(" ")

        # Ensure the log entry has enough parts to process
        if len(log_parts) > 4:
            status_code = log_parts[-2]
            try:
                # Convert the size part to an integer
                entry_size = int(log_parts[-1])
            except ValueError:
                # Skip the line if the size is not an integer
                continue

            # Update the status code count if it exists in the dictionary
            if status_code in status_counts:
                status_counts[status_code] += 1

            # Add the size to the total file size
            total_file_size += entry_size

            # Increment the line counter
            line_counter += 1

        # Every 10 lines, print the current statistics
        if line_counter == 10:
            line_counter = 0
            print('File size: {}'.format(total_file_size))
            for code, count in sorted(status_counts.items()):
                if count != 0:
                    print('{}: {}'.format(code, count))

except KeyboardInterrupt:
    # Handle keyboard interruption and print final stats
    print('File size: {}'.format(total_file_size))
    for code, count in sorted(status_counts.items()):
        if count != 0:
            print('{}: {}'.format(code, count))
    sys.exit(0)

except Exception as error:
    # Print any other exceptions to stderr
    sys.stderr.write("Error: {}\n".format(error))

finally:
    # Ensure the final stats are printed when the script ends
    print('File size: {}'.format(total_file_size))
    for code, count in sorted(status_counts.items()):
        if count != 0:
            print('{}: {}'.format(code, count))
