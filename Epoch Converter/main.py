"""This script converts a Unix timestamp to a human-readable date and time format.
It also displays the current Unix timestamp when the script is run."""

import datetime
import time

def convert():
    """Main function to execute the timestamp conversion."""
    print(f"Current Unix timestamp: {datetime.datetime.now().timestamp()}")
    unix_timestamp = float(input("Enter a Unix timestamp: "))
    date_time = datetime.datetime.fromtimestamp(unix_timestamp)
    print("The corresponding date and time is:", date_time)
    print("ISO 8601 format:", date_time.isoformat())
    
def print_current_timestamp_every_second():
    """Prints the current Unix timestamp every second."""
    try:
        while True:
            print(f"Current Unix timestamp: {datetime.datetime.now().timestamp()}")
            time.sleep(1)
    except KeyboardInterrupt:
        print("Stopped printing timestamps.")

def main():
    """Entry point of the script."""
    if input("Do you want to convert a Unix timestamp? (yes/no): ").lower() == "yes":
        convert()
    elif input("Do you want to see the current Unix timestamp? (yes/no): ").lower() == "yes":
        print(f"Current Unix timestamp: {datetime.datetime.now().timestamp()}")
    elif input("Do you want to see the current date and time? (yes/no): ").lower() == "yes":
        print(f"Current date and time: {datetime.datetime.now()}")
    elif input("Do you want to see the current date and time in ISO 8601 format? (yes/no): ").lower() == "yes":
        print(f"Current date and time in ISO 8601 format: {datetime.datetime.now().isoformat()}")
    elif input("Do you want to have the current Unix timestamp print in the terminal every second? (yes/no): ").lower() == "yes":
        print_current_timestamp_every_second()
    else:
        print("No valid option selected. Exiting the program.")

if __name__ == "__main__":
    main()
