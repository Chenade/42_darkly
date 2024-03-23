#!/bin/bash

# Check if input file is provided
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <folder_names_file>"
    exit 1
fi

# Input file containing folder names
folder_names_file="$1"

# Check if input file exists
if [ ! -f "$folder_names_file" ]; then
    echo "Error: File '$folder_names_file' not found."
    exit 1
fi

rm -rf Project
# Create folders based on names in the input file
while IFS= read -r folder; do
    # Check if folder name ends with ":"
    if [[ "$folder" == *":" ]]; then
        folder_name=$(echo "$folder" | sed 's/:$//') # Remove trailing ":"
        mkdir -p "Project/$folder_name"
        flag=1 # Set flag to indicate to read the next line
	mkdir -p "Project/$folder_name/Resources"
	echo "" > "Project/$folder_name/Resources/readme.md" 
    elif [ "$flag" -eq 1 ]; then
        echo "$folder" > "Project/$folder_name/flag.txt" # Write the next line to flag.txt
        flag=0 # Reset flag
    fi
done < "$folder_names_file"

#echo "Folders created successfully."

