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
    "KIND/output/logs/",
    "KIND-IA/output/logs/",
    "KIND-IAC/output/logs/"
]

# Initialize an empty list to store individual DataFrames
# Define a dictionary to store the total score and CPU time for each subcategory
subcategory_data = {}
read_first_2_columns_once = False
selected_columns = []

fix_headers_in_directory("results","new_results")

file_names = os.listdir("new_results")

# Read each CSV file and append its DataFrame to the list
for file_name in file_names:
    try:
        df = pd.read_csv("new_results/"+file_name, delimiter='\t')
        print(file_name)
        if not read_first_2_columns_once:
            selected_columns.append(df.iloc[:, 0:2])
            read_first_2_columns_once = True
        selected_cols = df.iloc[:, [2, 3, 5]]
        selected_columns.append(selected_cols)
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

    """
    solver_times = {}
    contractor_parse_time = []
    contractor_apply_time = []

    for tool in search_dir:
        solver_times[tool] = []
    # print(solver_times[tool])
    log_prefix = "SV-COMP23_unreach-call."
    search_prefix = "Runtime decision procedure:"
    for benchmark_name in combined_df["Benchmark"]:
        # In each tool
        print(benchmark_name)
        for tool in search_dir:
            # Find the file with the same name
            # print(tool)
            found_file = find_file(log_prefix + benchmark_name + ".log", tool)
            if found_file:
                lines = extract_search_prefix_lines(found_file, search_prefix)

                solver_time = 0
                for line in lines:
                    solver_time += extract_number_from_line(line, search_prefix)
                solver_times[tool].append(solver_time)

            #if tool.startswith("KIND-IAC"):
                #parse_lines = extract_search_prefix_lines(found_file, "Contractor parse time:")
                #apply_lines = extract_search_prefix_lines(found_file, "Contractor contarct time:")
               # parse_time = 0
               # for line in parse_lines:
                 #   parse_time += extract_number_from_line(line, "Contractor parse time:")
                #contractor_parse_time.append(parse_time/1000)
                #apply_time = 0
               # for line in apply_lines:
                #    apply_time += extract_number_from_line(line, "Contractor contarct time:")
               # contractor_apply_time.append(apply_time/1000)


    # print(solver_times)
    #combined_df["parse time"] = contractor_parse_time
    #combined_df["apply time"] = contractor_apply_time


    for tool in search_dir:
        combined_df[tool] = solver_times[tool]
    """
    # Save the combined DataFrame to a new CSV file
    combined_df.to_csv("combined_data.csv", sep='\t', index=False)
    print("CSV files successfully combined and saved as 'combined_data.csv'.")

"""
# --------------------------------------------------------------------------
# Create a new DataFrame with the "score" column calculated using getScore
score_df = combined_df.copy()
score_df["score1"] = score_df.apply(lambda row: getScore(row["CTRL"], row[4]), axis=1)
score_df["score2"] = score_df.apply(lambda row: getScore(row["CTRL"], row[7]), axis=1)
score_df["score3"] = score_df.apply(lambda row: getScore(row["CTRL"], row[10]), axis=1)
score_df.drop(columns=score_df.columns[[2, 3, 4]], inplace=True)
score_df.columns.values[2] = "time1"
score_df.columns.values[3] = "memory1"
score_df.columns.values[4] = "time2"
score_df.columns.values[5] = "memory2"
score_df.columns.values[6] = "time3"
score_df.columns.values[7] = "memory3"
# Display the data type of each column
print(combined_df.dtypes)
# Save the new DataFrame to a CSV file
score_df.to_csv("score_data.csv", sep='\t', index=False)
print("Score data saved as 'score_data.csv'.")

# Group by "category" and "sub category" and calculate the sum of scores
grouped_df = score_df.groupby(["category", "sub category"]).agg({"score1": "sum", "time1": "sum", "memory1": "sum",
                                                                 "score2": "sum", "time2": "sum", "memory2": "sum",
                                                                 "score3": "sum", "time3": "sum",
                                                                 "memory3": "sum"}).reset_index()
# grouped_df.reset_index(inplace=True)

# Save the grouped DataFrame to a new CSV file
grouped_df.to_csv("grouped_scores.csv", sep=',', index=False)
print("Grouped scores saved as 'grouped_scores.csv'.")
else:
print("No CSV files were successfully read and combined.")
"""