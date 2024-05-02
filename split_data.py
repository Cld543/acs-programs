'''
This program uses pandas to split a master file of data into multiple files based
on the unique values in a given column.

After running this function, the user will be asked to enter the name of the source csv file
and the column they want to split up. The function will then create a separate file for each
unique value in the specified column. Each file will contain all records for each unique
column header in the source file.
'''

import pandas as pd

source_file = ''
sheets = []
target_column = ''
col_found = False

def get_source_file():
    file_name = input("Enter name of source file: ")
    return file_name

def check_target_column(df):
    col = input("Enter the name of the column to split by: ")
    if not col in df.columns:
        print(f"Column with name {col} not found in source file.")
    else:
        col_found = True
    
# TODO: Validate file input.
source_file = get_source_file()
print("Opening file: " + source_file)

target_column = input("Enter target column to split by: ")

data = pd.read_csv(source_file)

data = data.sort_values(target_column)


unique_values = data[target_column].unique()



# Create a list to store dataframes of each unique column value.
split_data = []
for u in unique_values:
    split_data.append(data[data[target_column] == u])

# Save split data to .csv files.
for file in split_data:
    label = file[target_column].iloc[0]
    #print(label)
    file_name = f'{label}.csv'
    file.to_csv(file_name, index=False)
