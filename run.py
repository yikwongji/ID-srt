import re
import os

def correct_srt_ids(input_file, output_file):
    # Read the input SRT file
    with open(input_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    
    corrected_lines = []
    for line in lines:
        # Match and correct lines starting with "第<Number>章"
        match = re.match(r'^第(\d+)章$', line.strip())
        if match:
            corrected_lines.append(f"{match.group(1)}\n")
        else:
            corrected_lines.append(line)
    
    # Write the corrected content to the output file
    with open(output_file, 'w', encoding='utf-8') as file:
        file.writelines(corrected_lines)

# List of all the SRT file names
srt_files = [
    "lecture 1 CN.srt",
    "lecture 2 CN.srt",
    "lecture 3 CN.srt",
    "lecture 4 CN.srt",
    "lecture 5 CN.srt",
    "lecture 6 CN.srt",
    "lecture 7 CN.srt",
    "lecture 14 CN.srt",
    "lecture 13 CN.srt"
]

# Process each file
output_directory = "corrected_srt"  # Directory to save the corrected files
os.makedirs(output_directory, exist_ok=True)  # Create directory if it doesn't exist

for srt_file in srt_files:
    input_file = srt_file
    output_file = os.path.join(output_directory, srt_file)
    correct_srt_ids(input_file, output_file)
    print(f"Processed: {srt_file}")

print("All files processed successfully!")
