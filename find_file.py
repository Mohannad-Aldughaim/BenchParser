import os
import re

search_prefix = "Runtime decision procedure:"

def fix_headers_in_directory(input_dir, output_dir):
    # Create the output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # List all files in the input directory
    files = os.listdir(input_dir)

    # Process each file in the input directory
    for file in files:
        if file.endswith(".csv"):  # Filter only .txt files
            input_path = os.path.join(input_dir, file)
            output_path = os.path.join(output_dir, file)
            fix_headers(input_path, output_path)

    print("All files in the directory processed.")
def fix_headers(input_file, output_file):
    # Define the new header
    new_header = "benchmarks\tCTRL\tstatus\tcputime(s)\twalltime(s)\tmemory(MB)\n"

    # Read the input file and replace the first three lines
    with open(input_file, "r") as file_in:
        lines = file_in.readlines()
        lines[:3] = new_header

    # Write the modified content to the output file
    with open(output_file, "w") as file_out:
        file_out.writelines(lines)

    print("Header replacement completed.")

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
