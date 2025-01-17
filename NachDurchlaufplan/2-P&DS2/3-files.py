#3.1 Write a List of Names to a CSV File.
import csv

names = ["Alice", "Bob", "Charlie", "Diana"]

with open("names.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name"])  # Header
    for name in names:
        writer.writerow([name])

print("Names have been written to names.csv.")


#3.2 Read and Display Data from a CSV File.
import csv

with open("names.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)


#3.3 Append New Data to an Existing CSV File.
import csv

new_names = ["Eve", "Frank", "Grace"]

with open("names.csv", "a", newline="") as file:
    writer = csv.writer(file)
    for name in new_names:
        writer.writerow([name])

print("New names have been appended to names.csv.")


#3.4 Count Rows in a CSV File.
import csv

with open("names.csv", "r") as file:
    reader = csv.reader(file)
    row_count = sum(1 for row in reader) - 1  # Subtract 1 for the header row

print("The file contains", row_count, "names.")


#3.5 Search for a Name in a CSV File.
import csv

search_name = input("Enter a name to search for: ")

with open("names.csv", "r") as file:
    reader = csv.reader(file)
    found = False
    for row in reader:
        if search_name in row:
            found = True
            break

if found:
    print(search_name, "is in the file.")
else:
    print(search_name, "is not in the file.")


#3.6 Copy Data from One CSV File to Another.
import csv

with open("names.csv", "r") as source_file:
    reader = csv.reader(source_file)
    with open("names_copy.csv", "w", newline="") as destination_file:
        writer = csv.writer(destination_file)
        for row in reader:
            writer.writerow(row)

print("Data has been copied to names_copy.csv.")