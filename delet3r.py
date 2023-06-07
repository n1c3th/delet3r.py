import argparse
import csv

def compare_and_delete_entries(file1, file2):
    # Read the contents of the first file
    with open(file1, 'r') as f1:
        reader1 = csv.reader(f1)
        rows1 = list(reader1)

    # Read the contents of the second file
    with open(file2, 'r') as f2:
        reader2 = csv.reader(f2)
        rows2 = list(reader2)

    # Check if rows2 is empty or has fewer columns
    if len(rows2) == 0 or len(rows2[0]) == 0:
        print("The second file is empty or has an invalid format.")
        return

    # Extract the entries from the first column of the second file (converted to lowercase)
    entries_to_delete = [row[0].lower() for row in rows2 if len(row) > 0]

    # Remove the corresponding entries from the first file, excluding the first row (converted to lowercase)
    updated_rows = [rows1[0]] + [row for row in rows1[1:] if len(row) > 0 and row[0].lower() not in entries_to_delete]

    # Write the updated rows to a new file
    with open('updated_file.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(updated_rows)

    print("Entries deleted successfully. Updated file saved as 'updated_file.csv'.")

# Create an ArgumentParser object
parser = argparse.ArgumentParser(description='Compare and delete entries from a CSV file.')

# Add the -f1 (or --file1) argument
parser.add_argument('-f1', '--file1', type=str, help='Path to the first CSV file.')

# Add the -f2 (or --file2) argument
parser.add_argument('-f2', '--file2', type=str, help='Path to the second CSV file.')

# Parse the command-line arguments
args = parser.parse_args()

# Check if the --help option is provided
if args.file1 is None or args.file2 is None:
    parser.print_help()
else:
    # Run the comparison and deletion logic
    compare_and_delete_entries(args.file1, args.file2)

