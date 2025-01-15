import os

def rename_file(original_name):
    # Split the original filename into base name and extension
    base_name, extension = os.path.splitext(original_name)
    # Split the base name into characters, adding a space between each character
    new_base_name = ' '.join(base_name)
    # Reattach the extension
    new_name = new_base_name + extension
    return new_name

def rename_files_in_directory(directory):
    for filename in os.listdir(directory):
        # Skip directories, only process files
        if os.path.isfile(os.path.join(directory, filename)):
            new_name = rename_file(filename)
            os.rename(os.path.join(directory, filename), os.path.join(directory, new_name))

#usage:
directory = r'\MyDesktop\Renaming Script'
rename_files_in_directory(directory)
