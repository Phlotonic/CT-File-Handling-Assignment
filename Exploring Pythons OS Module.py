import os

def list_directory_contents(path):
    """
    List and print all files and subdirectories in the given path.
    Handle exceptions for invalid paths or inaccessible directories.
    """
    try:
        # Check if the provided path is a valid directory
        if not os.path.isdir(path):
            raise NotADirectoryError(f"The path '{path}' is not a valid directory.")
        
        # List all files and subdirectories in the given path
        with os.scandir(path) as entries:
            for entry in entries:
                if entry.is_file():
                    print(f"File: {entry.name}")
                elif entry.is_dir():
                    print(f"Directory: {entry.name}")
    
    except NotADirectoryError as nde:
        print(nde)
    except PermissionError:
        print(f"Permission denied: Unable to access the directory '{path}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    # Prompt the user for the directory path
    directory_path = input("Enter the directory path: ")
    
    # List the contents of the specified directory
    list_directory_contents(directory_path)

if __name__ == "__main__":
    main()
