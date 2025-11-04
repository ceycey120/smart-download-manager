import os 
import shutil

def list_files_info(path="."):
    """Print file's name, type, and size in the current folder."""
    print("Listing files in current folder:\n")
    # Loop for printing each file name, type, and size
    for f in os.listdir(path):
        if os.path.isfile(os.path.join(path, f)):
            size = os.path.getsize(f)
            ext = os.path.splitext(f)[1] or "(no extension)"
            print("Name:", f) # Print file's name
            print("Type:", ext) # Print file's type
            print("Size:", size) # Print file's size
            print("-------")

def move_file(source, destination):
    """Function for moving a file(source) to destinated location(destination)"""

    # Check if 'destination' exist. If not, create the destination directory
    if not os.path.exists(destination):
        os.makedirs(destination)
        print(f"New destination folder {destination} created")

    try:
        # Try to move the file from source to destination
        shutil.move(source, destination)
        print(f"Successfully moved file from {source} to {destination}")
        # In case error occur during moving operation, these specific error warning will be printed as output
    except FileNotFoundError:
        print(f"Error: File not found")
    except PermissionError:
        print(f"Error: Permission denied to move file.")
    except  Exception as e:
        print(f"Error: {e}")

# Example usage
if __name__ == "__main__":
    list_files_info(".")
    # move_file("example.txt", "backup/")
