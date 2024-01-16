import os
import pandas
from category import getSubCat, getCat, getScore
from find_file import extract_search_prefix_lines, find_file, extract_number_from_line, search_prefix, fix_headers, \
    fix_headers_in_directory

import pandas as pd

# List of file names to read
file_names = [
    #"results/INC.csv",
    #"results/INC-ia.csv",
    #"results/INC-iac"
]

search_dir = [
    #"KIND/output/logs/",
    #"KIND-IA/output/logs/",
    #"KIND-IAC/output/logs/"
]

# Initialize an empty list to store individual DataFrames
# Define a dictionary to store the total score and CPU time for each subcategory



def do_folder(folder_name):
    new_folder = folder_name+"_mod"
    fix_headers_in_directory(folder_name,new_folder)

    file_names = os.listdir(new_folder)
    selected_columns = []

    read_first_2_columns_once = False
    # Read each CSV file and append its DataFrame to the list
    for file_name in file_names:
        try:
            df = pd.read_csv(new_folder+"/"+file_name, delimiter='\t')
            print(file_name)
            if not read_first_2_columns_once:
                selected_columns.append(df.iloc[:, 0:2])
                read_first_2_columns_once = True
            selected_cols = df.iloc[:, [2, 3, 5]]
            selected_columns.append(selected_cols)
            print(f"'{file_name}'==>")
        except FileNotFoundError:
            print(f"File '{file_name}' not found. Skipping.")

    # Combine the DataFrames into a single DataFrame
    if selected_columns:
        combined_df = pd.concat(selected_columns, axis=1)
        # You can perform operations on the combined DataFrame here if needed
        combined_df.insert(0, "sub category", combined_df.iloc[:, 0].str.split('/').str[0])
        combined_df.insert(1, "Benchmark", combined_df.iloc[:, 1].str.split('/').str[1])
        # Drop column 2
        combined_df.drop(columns=combined_df.columns[2], inplace=True)
        combined_df.insert(0, "category", combined_df.iloc[:, 0].apply(getSubCat))

        # Save the combined DataFrame to a new CSV file
        combined_df.to_csv(new_folder+"_combined_data.csv", sep='\t', index=False)
        print("CSV files successfully combined and saved as 'combined_data.csv'.")

def process_folders(directory):
    # Check if the given directory exists
    if not os.path.isdir(directory):
        print(f"Directory not found: {directory}")
        return

    # Iterate through each item in the directory
    for item in os.listdir(directory):
        # Construct full path
        item_path = os.path.join(directory, item)

        # Check if the item is a folder/directory
        if os.path.isdir(item_path):
            # Perform the desired function on the folder
            do_folder(item_path)

#process_folders("./rafael")
do_folder("./rafael")