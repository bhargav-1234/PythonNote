# import filecmp

# f1 = "C:\Users\naget\OneDrive\Documents\test\file1.txt"
# f2 = "C:\Users\naget\OneDrive\Documents\test\file2.txt"

# filecmp.cmp('f1', 'f2').report()

# Python program to explain filecmp.cmpfiles() method

# importing filecmp module
# import filecmp

# # Path of first directory
# dir1 = "C:/Users/naget/OneDrive/Documents/test"

# # Path of second directory
# dir2 = "C:/Users/naget/Downloads"

# # Common files
# common = ["file1.txt", "file2.txt","commands.txt"]

# # Shallow compare the files
# # common in both directories
# match, mismatch, errors = filecmp.cmpfiles(dir1, dir2, common)

# # Print the result of
# # shallow comparison
# print("Shallow comparison:")
# print("Match :", match)
# print("Mismatch :", mismatch)
# print("Errors :", errors, "\n")


# # # Compare the
# # # contents of both files
# # # (i.e deep comparison)
# # match, mismatch, errors = filecmp.cmpfiles(dir1, dir2, common)

# # # Print the result of
# # # deep comparison
# # print("Deep comparison:")
# # print("Match :", match)
# # print("Mismatch :", mismatch)
# # print("Errors :", errors)


# def compare_files(file1_path, file2_path):
#     # Read the contents of the files
#     with open(file1_path, 'r') as file1, open(file2_path, 'r') as file2:
#         file1_contents = file1.readlines()
#         file2_contents = file2.readlines()

#     # Remove date-time values from the file contents
#     file1_contents = remove_date_time(file1_contents)
#     file2_contents = remove_date_time(file2_contents)

#     # Compare the modified file contents
#     if file1_contents == file2_contents:
#         print("The files are identical.")
#     else:
#         print("The files are different.")

# def remove_date_time(file_contents):
#     # Remove date-time values from each line
#     modified_contents = []
#     for line in file_contents:
#         # Assuming the date-time format is in 'YYYY-MM-DD HH:MM:SS' or 'YYYY/MM/DD HH:MM:SS'
#         modified_line = ''.join(line.split()[2:])
#         modified_contents.append(modified_line)

#     return modified_contents

# # Provide the file paths
# file1_path = r'C:/Users/naget/OneDrive/Documents/test/file1.txt'
# file2_path = r'C:/Users/naget/OneDrive/Documents/test/file2.txt'

# # Compare the files
# compare_files(file1_path, file2_path)

# import csv
# from timestamp import compare_csv_files
# file1 = r"C:\Users\naget\OneDrive\Documents\test\file1.csv"
# file2 = r"C:\Users\naget\OneDrive\Documents\test1\file2.csv"

# compare_csv_files(file1, file2)

# import csv

# def compare_csv(file1, file2):
#     with open(file1, 'r') as csv_file1, open(file2, 'r') as csv_file2:
#         reader1 = csv.reader(csv_file1)
#         reader2 = csv.reader(csv_file2)

#         rows1 = list(reader1)
#         rows2 = list(reader2)

#         num_rows1 = len(rows1)
#         num_rows2 = len(rows2)

#         for i in range(max(num_rows1, num_rows2)):
#             if i < num_rows1 and i < num_rows2:
#                 row1 = rows1[i]
#                 row2 = rows2[i]
#                 if row1 != row2:
#                     print(f"Difference in row {i + 1}:")
#                     highlight_difference(row1, row2)
#             elif i < num_rows1:
#                 print(f"Difference in row {i + 1}:")
#                 highlight_difference(rows1[i], [])
#             elif i < num_rows2:
#                 print(f"Difference in row {i + 1}:")
#                 highlight_difference([], rows2[i])

# def highlight_difference(row1, row2):
#     diff_row = []
#     for i, (cell1, cell2) in enumerate(zip(row1, row2)):
#         if cell1 != cell2:
#             diff_row.append(f"({cell1}) -> ({cell2})")
#         else:
#             diff_row.append(cell1)

#     # Handle remaining cells in the longer row, if any
#     if len(row1) > len(row2):
#         for cell in row1[len(row2):]:
#             diff_row.append(f"({cell})")
#     elif len(row2) > len(row1):
#         for cell in row2[len(row1):]:
#             diff_row.append(f"-> ({cell})")

#     print(", ".join(diff_row))

# import pandas as pd
# from openpyxl import Workbook
# from openpyxl.styles import PatternFill

# def compare_csv_files(file1, file2, output_file):
#     # Read the CSV files into pandas DataFrames
#     df1 = pd.read_csv(file1)
#     df2 = pd.read_csv(file2)

#     # Find the differences between the two DataFrames
#     diff_df = df1.merge(df2, indicator=True, how='outer')
#     diff_df = diff_df[diff_df['_merge'] != 'both']

#     # Create a new Excel workbook and select the active sheet
#     wb = Workbook()
#     ws = wb.active

#     # Apply color to the cells with differences
#     fill = PatternFill(start_color="FFFF00", end_color="FFFF00", fill_type="solid")
#     for row in ws.iter_rows(min_row=1, max_col=len(diff_df.columns), max_row=len(diff_df.index) + 1):
#         for cell in row:
#             cell.value = diff_df.iloc[cell.row - 2, cell.column - 1]
#             if cell.row == 1:
#                 cell.font = cell.font.copy(bold=True)  # Bold header row
#             elif cell.column > 1:
#                 cell.fill = fill  # Apply color to non-header cells

#     # Save the Excel workbook
#     wb.save(output_file)



# # Usage example
# compare_csv_files(r"C:\Users\naget\OneDrive\Documents\test\file1.csv", r"C:\Users\naget\OneDrive\Documents\test1\file1.csv", r"C:\Users\naget\OneDrive\Documents\output\file.xlsx")

#02-06-2023

# import pandas as pd

# def compare_csv_files(file1_path, file2_path):
#     # Read CSV files
#     df1 = pd.read_csv(file1_path)
#     df2 = pd.read_csv(file2_path)

#     # Compare the two DataFrames
#     comparison_df = df1 == df2 

#     # Highlight differing cells
#     df_diff = pd.concat([df1.mask(comparison_df), df2.mask(comparison_df)], keys=['File 1', 'File 2'])

#     # Generate a new CSV file with highlighted differences
#     df_diff.to_csv('differences.csv')

#     # Print the highlighted output
#     print(df_diff)

#
# Usage example
#compare_csv_files(r"C:\Users\naget\OneDrive\Documents\test\file1.csv", r"C:\Users\naget\OneDrive\Documents\test1\file1.csv")

# 03-06-2023

# import csv

# def compare_csv_files(file1, file2):
#     with open(file1, 'r') as csv_file1, open(file2, 'r') as csv_file2:
#         csv_reader1 = csv.reader(csv_file1)
#         csv_reader2 = csv.reader(csv_file2)

#         rows1 = list(csv_reader1)
#         rows2 = list(csv_reader2)

#         for i in range(min(len(rows1), len(rows2))):
#             row1 = rows1[i]
#             row2 = rows2[i]

#             if row1 != row2:
#                 print(f"Difference at row {i + 1}:")
#                 for j in range(min(len(row1), len(row2))):
#                     if row1[j] != row2[j]:
#                         print(f"Column {j + 1}: {row1[j]} (File 1) vs {row2[j]} (File 2)")

#         if len(rows1) != len(rows2):
#             print("Files have different number of rows")

#         print("Comparison complete.")

# # Usage example
# compare_csv_files(r"C:\Users\naget\OneDrive\Documents\test\file1.csv", r"C:\Users\naget\OneDrive\Documents\test1\file1.csv")

#2.

# import csv

# def compare_csv(file1, file2):
#     # Read the contents of both CSV files
#     with open(file1, 'r') as csvfile:
#         csv1 = list(csv.reader(csvfile))

#     with open(file2, 'r') as csvfile:
#         csv2 = list(csv.reader(csvfile))

#     # Find the differences between the two CSV files
#     differences = []
#     for i, row in enumerate(csv1):
#         if row != csv2[i]:
#             differences.append((i, row, csv2[i]))

#     # Print the differences
#     for diff in differences:
#         print(f"Row {diff[0]+1}:")
#         print(f"   File 1: {diff[1]}")
#         print(f"   File 2: {diff[2]}")
#         print()


# # Provide the paths to the CSV files
# file1 = r"C:\Users\naget\OneDrive\Documents\test\file1.csv"
# file2 = r"C:\Users\naget\OneDrive\Documents\test1\file1.csv"

# # Compare the CSV files
# compare_csv(file1, file2)

import datetime
a = "Bhargav"
print(a)
x = datetime.datetime.now()
print(x.strftime("%G"))
print(x)