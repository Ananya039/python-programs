import os

# Specify the directory path (you can modify it)
directory_path = '/'

try:
    # Get the list of files and directories
    contents = os.listdir(directory_path)
    
    # Print each item in the directory
    print(f"Contents of '{directory_path}':")
    for item in contents:
        print(item)
except FileNotFoundError:
    print(f"The directory '{directory_path}' does not exist.")
except PermissionError:
    print(f"Permission denied to access '{directory_path}'.")
