import os
import shutil

def list_files_info(path="."):
    """Print name, extension, and size for files in the given folder."""
    print(f"Listing files in folder: {os.path.abspath(path)}\n")

    files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
    if not files:
        print("No files found in this folder.\n")
        return

    for f in files:
        full_path = os.path.join(path, f)
        size = os.path.getsize(full_path)
        ext = os.path.splitext(f)[1] or "(no extension)"
        print(f"Name: {f}")
        print(f"Type: {ext}")
        print(f"Size: {size} bytes")
        print("-------")


def move_file(source, destination):
    """Move a file from source to destination, creating the destination if needed."""
    if not os.path.exists(destination):
        os.makedirs(destination)
        print(f"New destination folder '{destination}' created.")

    try:
        shutil.move(source, destination)
        print(f"✅ Successfully moved file from '{source}' to '{destination}'.")
    except FileNotFoundError:
        print("❌ Error: Source file not found.")
    except PermissionError:
        print("❌ Error: Permission denied to move file.")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")


# Example usage
if __name__ == "__main__":
    list_files_info(".")
    # move_file("example.txt", "backup/")
