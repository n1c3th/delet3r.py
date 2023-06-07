# delet3r.py

The CSV Comparison and Deletion Script is a Python script designed to compare entries between two CSV files and delete corresponding entries from one of the files. The script takes two CSV files as input and performs the following steps:

1. Reads the contents of the first CSV file.
2. Reads the contents of the second CSV file.
3. Extracts the entries from the first column of the second file.
4. Converts the extracted entries to lowercase for case-insensitive comparison.
5. Removes the corresponding entries from the first file, excluding the first row.
6. Writes the updated rows to a new CSV file named "updated_file.csv".

The script utilizes the `argparse` module to handle command-line arguments. The user can provide the paths to the two CSV files using either the long options (`--file1` and `--file2`) or the short options (`-f1` and `-f2`).

Note: The script assumes that the CSV files follow a standard format with comma-separated values and that the first column of each file contains the entries to be compared.

how to use: 
python script.py -f1 file1.csv -f2 file2.csv
python script.py -f1 /path/to/folder1/file1.csv -f2 /path/to/folder2/file2.csv
