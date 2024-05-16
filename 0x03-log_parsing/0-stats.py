#!/usr/bin/python3
import sys
import signal


# Initialize metrics
total_size = 0
status_count = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0


def print_stats():
    """Prints the statistics."""
    print(f"File size: {total_size}")
    for status in sorted(status_count):
        if status_count[status] > 0:
            print(f"{status}: {status_count[status]}")


def signal_handler(sig, frame):
    """Handles the keyboard interrupt signal."""
    print_stats()
    sys.exit(0)


# Register the signal handler
signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        # Parse the line
        parts = line.split()
        if len(parts) != 7:
            continue

        ip, _, _, date, request, status_code, file_size = parts

        # Validate the line format
        if not request.startswith('"GET /projects/260 HTTP/1.1"'):
            continue

        try:
            status_code = int(status_code)
            file_size = int(file_size)
        except ValueError:
            continue

        # Update metrics
        if status_code in status_count:
            status_count[status_code] += 1
        total_size += file_size
        line_count += 1

        # Print stats every 10 lines
        if line_count % 10 == 0:
            print_stats()

except KeyboardInterrupt:
    print_stats()
    sys.exit(0)


# Print final stats if the script ends normally
print_stats()
