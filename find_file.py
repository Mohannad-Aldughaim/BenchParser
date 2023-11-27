import os
import re

search_prefix = "Runtime decision procedure:"


def find_file(file_name, search_directory):
    for root, dirs, files in os.walk(search_directory):
        if file_name in files:
            return os.path.join(root, file_name)
    return None


# Function to extract lines starting with "solver time"
def extract_search_prefix_lines(file_path, search_prefix):
    search_prefix_lines = []
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            for line in lines:
                if line.startswith(search_prefix):
                    search_prefix_lines.append(line.strip())
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    return search_prefix_lines


def find_and_extract_form_file(file_name_to_find, search_directory):
    found_file = find_file(file_name_to_find, search_directory)

    if found_file:
        print(f"File '{file_name_to_find}' found at: {found_file}")
    else:
        print(f"File '{file_name_to_find}' not found in the specified directory.")
        return

    filename = found_file
    sum = 0
    # Call the function and print the result
    solver_time_lines = extract_search_prefix_lines(filename)
    if solver_time_lines:
        for line in solver_time_lines:
            print(line)
    else:
        print("No lines starting with 'search_prefix' found in the file.")

    print(sum)


# Function to extract the number from a line after a specific prefix
def extract_number_from_line(line, prefix):
    # Remove the prefix and any leading/trailing whitespace
    line = line[len(prefix):].strip()
    numbers = re.findall(r'\d+\.\d+|\d+', line)
    # Attempt to convert the remaining text to a number
    if numbers:
        # Convert the first found number to float (you can modify this if needed)
        return float(numbers[0])
    else:
        return 0
