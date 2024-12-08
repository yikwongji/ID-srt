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

# Folder paths
input_folder = "before"
output_folder = "after"

# Create the output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Process all .srt files in the input folder
for filename in os.listdir(input_folder):
    if filename.endswith(".srt"):
        input_file = os.path.join(input_folder, filename)
        output_file = os.path.join(output_folder, filename)
        correct_srt_ids(input_file, output_file)
        print(f"Processed: {filename}")

print("All files processed successfully!")
