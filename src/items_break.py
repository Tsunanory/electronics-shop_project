import csv

# Read the CSV file into a list of lists
with open('items.csv', 'r') as file:
    reader = csv.reader(file)
    data = list(reader)

# Now, `data` is a list of lists, where each inner list is a row of the CSV file.
# You can manipulate `data` as needed. For example, to replace the 5th row with a list of spaces:
if len(data) >= 5:
    data[4] = [''] * len(data[4])

# Write the list of lists back to the CSV file
with open('items.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)
