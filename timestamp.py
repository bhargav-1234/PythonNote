# import filecmp
# import re

# def line_compare(line1, line2):
#     # Ignore any characters that match a date or timestamp format
#     date_regex = r'\d{4}-\d{2}-\d{2}'
#     time_regex = r'\d{2}:\d{2}:\d{2}'
#     datetime_regex = f'{date_regex} {time_regex}'
#     pattern = re.compile(f'({datetime_regex}|{date_regex}|{time_regex})')
#     stripped_line1 = re.sub(pattern, '', line1)
#     stripped_line2 = re.sub(pattern, '', line2)
#     return stripped_line1 == stripped_line2

# file1 = 'C:/Users/naget/OneDrive/Documents/test/file1.txt'
# file2 = 'C:/Users/naget/OneDrive/Documents/test/file2.txt'
# cmp = filecmp.cmp(file1, file2, shallow=False, cmpfunc=line_compare)

# if cmp:
#     print('Files are equal')
# else:
#     print('Files are not equal')


# import re

# def compare_files(file1, file2):
#     with open(file1, 'r') as f1, open(file2, 'r') as f2:
#         for line1, line2 in zip(f1, f2):
#             # Remove the date and timestamp from each line
#             line1 = remove_date_and_time(line1)
#             line2 = remove_date_and_time(line2)
#             # Compare the lines
#             if line1 != line2:
#                 return False
#     return True

# def remove_date_and_time(line):
#     # Replace the date and timestamp patterns with an empty string
#     line = re.sub(r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}', '', line)
#     return line.strip()

# # Example usage
# if compare_files('C:/Users/naget/OneDrive/Documents/test/file1.txt', 'C:/Users/naget/OneDrive/Documents/test/file2.txt'):
#     print("Files are the same")
# else:
#     print("Files are different")


# import os
# import difflib
# import pdb

# differ = difflib.Differ()
# folder1 = r'C:\Users\naget\OneDrive\Documents\test'
# folder2 = r'C:\Users\naget\OneDrive\Documents\test1'
# outfolder = r'C:\Users\naget\OneDrive\Documents\output'
# # Get a list of all files in folder1
# files1 = os.listdir(folder1)

# # Get a list of all files in folder2
# files2 = os.listdir(folder2)    

# # Loop through the files in folder1
# for file1 in files1:
#     # Check if the file exists in folder2
#     # out_fh = open()
#     if file1 in files2:
#         out_fh = open(os.path.join(outfolder, file1.split(".")[0]+'.html'), 'w')
#         # If the file exists in both folders, compare them
#         with open(os.path.join(folder1, file1), 'r') as f1, open(os.path.join(folder2, file1), 'r') as f2:
#             lines1 = f1.readlines()
#             lines2 = f2.readlines()
#             # content1 = f1.read()
#             # content2 = f2.read()
#             # if content1 == content2:
#             #     print(f"{file1} is the same in both folders.")
#             # else:
#             #     print(f"{file1} is different in both folders.")
#         # # compare the lines and generate a list of differences
#         # diffs = difflib.unified_diff(lines1, lines2, lineterm='')
#         diffs = list(differ.compare(lines1, lines2))
#     # loop through the differences and print them with highlighting
#         # with open(outfolder+file1+'.out', 'w') as output_file:
#         for line in diffs:
#             if line.startswith('+'):  # Added line
#                 out_fh.write('\x1b[32m' + line + '\x1b[0m')  # Green color
#             elif line.startswith('-'):  # Removed line
#                 out_fh.write('\x1b[31m' + line + '\x1b[0m')  # Red color
#             else:  # Unchanged line
#                 out_fh.write(line)
#     else:
#         print(f"{file1} only exists in folder1.")
#     out_fh.close()
        
##open the files to compare

import difflib
with open(r'C:\Users\naget\OneDrive\Documents\test\file1.csv', 'r') as file1, open(r'C:\Users\naget\OneDrive\Documents\test1\file2.csv', 'r') as file2:
    # read the lines of each file
    lines1 = file1.readlines()
    lines2 = file2.readlines()

# create a differ object to compare the lines
differ = difflib.Differ()

# compare the lines and generate a list of differences
diffs = list(differ.compare(lines1, lines2))

# loop through the differences and print them with highlighting
for diff in diffs:
    if diff.startswith('-'):
        # deleted lines are highlighted in red
        print(f'\033[31m{diff}\033[0m', end='')
    elif diff.startswith('+'):
        # added lines are highlighted in green
        print(f'\033[32m{diff}\033[0m', end='')
    else:
        # unchanged lines are printed as is
        print(diff, end='')


# import os

# # Set the directory path
# directory_path = r"C:\Users\naget\OneDrive\Documents"

# # Get a list of all the files in the directory
# files = os.listdir(directory_path)

# # Loop through the list of files and print each one
# for file in files:
#     print(file)

# with open(r'C:\Users\naget\OneDrive\Documents\test\file1.txt') as file1, open(r'C:\Users\naget\OneDrive\Documents\test1\file1.txt') as file2:
#     for line1, line2 in zip(file1, file2):
#         if line1 != line2:
#             print("Files are different")
#             break
#     else:
#         print("Files are the same")


# import os
# import filecmp

# # Define the paths of the folders to compare
# folder1 = r'C:\Users\naget\OneDrive\Documents\test'
# folder2 = r'C:\Users\naget\OneDrive\Documents\test1'

# # Get the list of all files in folder1
# folder1_files = os.listdir(folder1)

# # Iterate over the files in folder1
# for file in folder1_files:
#     # Check if the file exists in folder2
#     if os.path.exists(os.path.join(folder2, file)):
#         # Compare the files using filecmp
#         if filecmp.cmp(os.path.join(folder1, file), os.path.join(folder2, file)):
#             print(f"{file} is identical in both folders.")
#         else:
#             print(f"{file} is different in both folders.")
#     else:
#         print(f"{file} does not exist in {folder2}.")



# import os

# folder1 = r'C:\Users\naget\OneDrive\Documents\test'
# folder2 = r'C:\Users\naget\OneDrive\Documents\test1'
# # Get a list of all files in folder1
# files1 = os.listdir(folder1)

# # Get a list of all files in folder2
# files2 = os.listdir(folder2)

# # Loop through the files in folder1
# for file1 in files1:
#     # Check if the file exists in folder2
#     if file1 in files2:
#         # If the file exists in both folders, compare them
#         with open(os.path.join(folder1, file1), 'r') as f1, open(os.path.join(folder2, file1), 'r') as f2:
#             content1 = f1.read()
#             content2 = f2.read()
#             if content1 == content2:
#                 print(f"{file1} is the same in both folders.")
#             else:
#                 print(f"{file1} is different in both folders.")
#     else:
#         print(f"{file1} only exists in folder1.")
        
# # Loop through the files in folder2 that are not in folder1
# for file2 in files2:
#     if file2 not in files1:
#         print(f"{file2} only exists in folder2.")


# import difflib


# def compare_files(file1_path, file2_path, output_path):
#     # Read the contents of the files
#     with open(file1_path, 'r') as file1:
#         file1_lines = file1.readlines()

#     with open(file2_path, 'r') as file2:
#         file2_lines = file2.readlines()

#     # Perform the comparison
#     diff = difflib.unified_diff(file1_lines, file2_lines, lineterm='')

#     # Write the differences with color highlighting to the output file
#     with open(output_path, 'w') as output_file:
#         for line in diff:
#             if line.startswith('+'):  # Added line
#                 output_file.write('\x1b[32m' + line + '\x1b[0m')  # Green color
#             elif line.startswith('-'):  # Removed line
#                 output_file.write('\x1b[31m' + line + '\x1b[0m')  # Red color
#             else:  # Unchanged line
#                 output_file.write(line)

# # Example usage
# file1_path = r'C:\Users\naget\OneDrive\Documents\test'
# file2_path = r'C:\Users\naget\OneDrive\Documents\test1'
# output_path = r'C:\Users\naget\OneDrive\Documents\out'

# compare_files(file1_path, file2_path, output_path)



#import difflib

# def highlight_diff(file1_path, file2_path, output_path):
#     with open(file1_path, 'r') as file1, open(file2_path, 'r') as file2:
#         lines1 = file1.readlines()
#         lines2 = file2.readlines()

#     differ = difflib.HtmlDiff()

#     with open(output_path, 'w') as output_file:
#         diff_html = differ.make_file(lines1, lines2)
#         output_file.write(diff_html)

# # Example usage
# highlight_diff(r'C:\Users\naget\OneDrive\Documents\test\file1.txt', r'C:\Users\naget\OneDrive\Documents\test1\file1.txt', r'C:\Users\naget\OneDrive\Documents\out\diff.html')



### New 18/05/2023

# import csv
# import pdb

# def compare_csv_files(file1, file2):
#     missing_rows = []
#     added_rows = []
#     file1_dict = {}
#     file2_dict = {}
#     # Read the first CSV file and extract the values from the first column
#     with open(file1, 'r') as csvfile:
#         reader = csv.reader(csvfile, delimiter='\t')
#         #pdb.set_trace()
#         # rows_file1 = [row for row in reader]
#         # values_file1 = [row[0] for row in rows_file1]
#         for row in reader:
#             file1_dict[row[0]] = row

#         # rows_file1 = [row for row in reader]
    
#     # Read the second CSV file and extract the values frn
#     # om the first column
#     with open(file2, 'r') as csvfile:
#         reader = csv.reader(csvfile, delimiter='\t')
#         # rows_file2 = [row for row in reader]
#         # values_file2 = [row[0] for row in rows_file2]
#         for row in reader:
#             file2_dict[row[0]] = row

#     # Checking for missing rows
#     for key in file1_dict.keys():
#         if key not in file2_dict.keys():
#             missing_rows.append(file1_dict[key])
#         else:
#             if file1_dict[key] ==  file2_dict[key]:
#                 pass
#             else:
#                 print("row is not matching. Baseline : {}, output: {}".format(file1_dict[key], file2_dict[key]))

#     #Checking for newly added rows
#     for key in file2_dict.keys():
#         if key not in file1_dict.keys():
#             added_rows.append(file2_dict[key])
#         else:
#             if file2_dict[key] == file1_dict[key]:
#                 pass
#             else:
#                 print("row is not matching. Baseline : {}, output: {}".format(file1_dict[key], file2_dict[key]))

#     return missing_rows, added_rows

# # Provide the paths to your CSV files
# file1_path = r'C:/Users/naget/OneDrive/Documents/test/file1.csv'
# file2_path = r'C:/Users/naget/OneDrive/Documents/test1/file1.csv'

# # Compare the two CSV files and get the missing rows
# missing_rows, added_rows = compare_csv_files(file1_path, file2_path)
# print("added_rows:{}, missed_rows:{}".format(added_rows, missing_rows))

# # Print the missing rows
# if missing_rows:
#     print("Missing rows:")
#     for row in missing_rows:
#         print('\t'.join(row))
# if added_rows:
#     print("New rows added:")
#     for row in added_rows:
#         print('\t'.join(row))
# else:
#     print("no new rows.")
    




    #### 22/05/2023
# import difflib
# import os
# import csv
# folder1 = r"C:\Users\naget\OneDrive\Documents\test"
# folder2 = r"C:\Users\naget\OneDrive\Documents\test1"
# output = r"C:\Users\naget\OneDrive\Documents\output"

# def compare_csv_files(file1, file2):
#     file1_dict = {}
#     file2_dict = {}
#     missing_rows = []
#     added_rows = []

    

#   # Get a list of all files in folder1
#     files1 = os.listdir(folder1)

#   # Get a list of all files in folder2
#     files2 = os.listdir(folder2)

#     # Loop through the files in folder1
#     for file1 in files1:
#         # Check if the file exists in folder2
#         # out_fh = open()
#         if file1 in files2:
#             #out_fh = open(os.path.join(outfolder, file1.split(".")[0]+'.html'), 'w')
#             # If the file exists in both folders, compare them
#             with open(os.path.join(folder1, file1), 'r') as baseline:
#                 #lines1 = file1.readlines()
#                 baseline_data = csv.reader(baseline, delimiter='\t')
#                 #pdb.set_trace()
#                 # rows_file1 = [row for row in reader]
#                 # values_file1 = [row[0] for row in rows_file1]
#                 for row in baseline_data:
#                     file1_dict[row[0]] = row

#             # rows_file1 = [row for row in reader]
        
#         # Read the second CSV file and extract the values frn
#         # on the first column
#             with open(os.path.join(folder2, file1), 'r') as out:
#                 current_data = csv.reader(out, delimiter='\t')
#                 #lines2 = file1.readlines()
#                 # rows_file2 = [row for row in reader]
#                 # values_file2 = [row[0] for row in rows_file2]
#                 for row in current_data:
#                     file2_dict[row[0]] = row

#     # Checking for missing rows
#         for key in file1_dict.keys():
#             if key not in file2_dict.keys():
#                 missing_rows.append(file1_dict[key])
#             else:
#                 if file1_dict[key] ==  file2_dict[key]:
#                     pass
#                 else:
#                     print("row is not matching. Baseline : {}, output: {}".format(file1_dict[key], file2_dict[key]))

# #Checking for newly added rows
#         for key in file2_dict.keys():
#             if key not in file1_dict.keys():
#                 added_rows.append(file2_dict[key])
#             else:
#                 if file2_dict[key] == file1_dict[key]:
#                     pass
#                 else:
#                     print("row is not matching. Baseline : {}, output: {}".format(file1_dict[key], file2_dict[key]))

#         differ = difflib.HtmlDiff()

#         with open(os.path.join(folder1, file1), 'r') as fh1, open(os.path.join(folder2, file1), 'r') as fh2:
#             lines1 = fh1.readlines()
#             lines2 = fh2.readlines()

#         with open(os.path.join(output, file1.split('.')[0]+".html"), 'w') as output_file:
#             diff_html = differ.make_file(lines1, lines2)
#             print("generating output diff file")
#             output_file.write(diff_html)
    

#         return missing_rows,added_rows
#     # Compare the two CSV files and get the missing rows
# missing_rows, added_rows = compare_csv_files(folder1, folder2)
# print("added_rows:{}, missed_rows:{}".format(added_rows, missing_rows))

#     # Print the missing rows
# if missing_rows:
#     print("Missing rows:")
#     for row in missing_rows:
#         print('\t'.join(row))
# if added_rows:
#     print("New rows added:")
#     for row in added_rows:
#         print('\t'.join(row))
# else:
#     print("no new rows.")
                               
                                                
# # 26/05/2023

# # 1.

# import csv

# def compare_csv_files(file1, file2):
#     with open(file1, 'r') as f1, open(file2, 'r') as f2:
#         reader1 = csv.reader(f1)
#         reader2 = csv.reader(f2)

#         rows1 = list(reader1)
#         rows2 = list(reader2)

#         # Find added and removed rows
#         added_rows = [row for row in rows2 if row not in rows1]
#         removed_rows = [row for row in rows1 if row not in rows2]

#         # Find modified rows
#         modified_rows = []
#         for i in range(min(len(rows1), len(rows2))):
#             if rows1[i] != rows2[i]:
#                 modified_rows.append((rows1[i], rows2[i]))

#         return added_rows, removed_rows, modified_rows

# def highlight_differences(file1, file2):
#     added_rows, removed_rows, modified_rows = compare_csv_files(file1, file2)

#     print("Added rows:")
#     for row in added_rows:
#         print("+", row)

#     print("\nRemoved rows:")
#     for row in removed_rows:
#         print("-", row)

#     print("\nModified rows:")
#     for row1, row2 in modified_rows:
#         print("Original:", row1)
#         print("Modified:", row2)
#         print()

# #Example usage
# file1 = r"C:\Users\naget\OneDrive\Documents\test\file1.csv"
# file2 = r"C:\Users\naget\OneDrive\Documents\test1\file2.csv"

# highlight_differences(file1, file2)


# # 2.

# import pandas as pd
# from termcolor import colored

# def compare_csv_files(file1, file2):
#     # Read the CSV files
#     df1 = pd.read_csv(file1)
#     df2 = pd.read_csv(file2)

#     # Compare the dataframes and create a boolean dataframe highlighting the differences
#     diff_df = df1.ne(df2)

#     # Iterate over each cell in the dataframe and highlight the differences with colors
#     for row in range(len(diff_df)):
#         for col in range(len(diff_df.columns)):
#             if diff_df.iloc[row, col]:
#                 cell_val = str(df2.iloc[row, col])
#                 diff_df.iloc[row, col] = colored(cell_val, 'red')

#     return diff_df

# # Specify the paths of the CSV files
# file1_path = r"C:\Users\naget\OneDrive\Documents\test\file1.csv"
# file2_path = r"C:\Users\naget\OneDrive\Documents\test1\file1.csv"

# # Compare the CSV files and highlight the differences
# #pdb.set_trace()
# result_df = compare_csv_files(file1_path, file2_path)

# # Print the result
# print(result_df)


#3.
# import difflib
# import pandas as pd

# # Read the CSV files
# df1 = pd.read_csv(r"C:\Users\naget\OneDrive\Documents\test\file2.csv")
# df2 = pd.read_csv(r"C:\Users\naget\OneDrive\Documents\test1\file2.csv")

# # Find differences between the two dataframes
# diff_df = df1.compare(df2)

# # Highlight the differences
# highlighted_diff = diff_df.style.highlight_null(null_color='lightyellow')

# # Display the highlighted differences
# print(highlighted_diff)

#4.

# import pandas as pd

# def compare_csv_files(file1, file2):
#     # Read the CSV files
#     df1 = pd.read_csv(file1)
#     df2 = pd.read_csv(file2)

#     # Compare the dataframes and identify the differences
#     differences = df1.ne(df2)

#     # Highlight the differences in a new column
#     df1['Differences'] = differences.any(axis=1)

#     # Save the updated dataframe to a new CSV file
#     df1.to_csv('highlighted_differences.csv', index=False)

# # Usage example
# compare_csv_files(r"C:\Users\naget\OneDrive\Documents\test\file2.csv", r"C:\Users\naget\OneDrive\Documents\test1\file2.csv")


#5.

# import pandas as pd
# from termcolor import colored

# def compare_csv_files(file1, file2):
#     df1 = pd.read_csv(file1)
#     df2 = pd.read_csv(file2)

#     # Find differences between the two dataframes
#     diff = df1.compare(df2)

#     # Iterate over the differences and highlight them
#     for row in diff.iterrows():
#         index, data = row
#         for col, value in data.items():
#             if pd.notnull(value[0]) and pd.notnull(value[1]):
#                 diff_str = f'{value[0]} != {value[1]}'
#             elif pd.notnull(value[0]):
#                 diff_str = f'{value[0]}'
#             else:
#                 diff_str = f'{value[1]}'

#             print(colored(f'Difference at index {index}: {diff_str}', 'red'))

# # Example usage
# compare_csv_files(r"C:\Users\naget\OneDrive\Documents\test\file1.csv", r"C:\Users\naget\OneDrive\Documents\test1\file1.csv")
