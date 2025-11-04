import os 
import shutil

def list_files_info(path="."):
    """print name, extension, and size for files in the given folder."""
    print("Listing files in current folder:\n")
    for f in os.listdir(path):
        if os.path.isfile(os.path.join(path, f)):
            size = os.path.getsize(f)
           ext = os.path.splitext(f)[1] or "(no extension)"
            print("Name:", f)
            print("Type:", ext)
            print("Size:", size)
            print("-------")

def move_file(source, destination):

    if not os.path.exists(destination):
        os.makedirs(destination)
        print(f"New destination folder {destination} created")

    try:
        shutil.move(source, destination)
        print(f"Successfully moved file from {source} to {destination}")
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
