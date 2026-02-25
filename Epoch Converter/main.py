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

def print_current_timestamp_every_second_with_iso_time():
    """Prints the current Unix timestamp and ISO 8601 time every second."""
    try:
        while True:
            current_time = datetime.datetime.now()
            print(f"Current Unix timestamp: {current_time.timestamp()} | "
                  f"ISO 8601 time: {current_time.isoformat()}")
            time.sleep(1)
    except KeyboardInterrupt:
        print("Stopped printing timestamps.")

def main():
    """Entry point of the script."""
    menu = (
        "1) Convert a Unix timestamp\n"
        "2) Show current Unix timestamp\n"
        "3) Show current date and time\n"
        "4) Show current date and time (ISO 8601)\n"
        "5) Print current Unix timestamp every second\n"
        "6) Print current Unix timestamp and ISO 8601 time every second\n"
    )
    print("Choose an action:")
    print(menu)
    choice = input("Enter 1-6 (or anything else to exit): ").strip()

    if choice == "1":
        convert()
    elif choice == "2":
        print(f"Current Unix timestamp: {datetime.datetime.now().timestamp()}")
    elif choice == "3":
        print(f"Current date and time: {datetime.datetime.now()}")
    elif choice == "4":
        print(f"Current date and time in ISO 8601 format: {datetime.datetime.now().isoformat()}")
    elif choice == "5":
        print_current_timestamp_every_second()
    elif choice == "6":
        print_current_timestamp_every_second_with_iso_time()
    else:
        print("No valid option selected. Exiting the program.")

if __name__ == "__main__":
    main()
