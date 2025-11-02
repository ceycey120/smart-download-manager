import os 

def list_files_info(path="."):
    """print name, extension, and size for files in the given folder."""
    print("Listing files in current folder:\n")
    for f in os.listdir(path):
        if os.path.isfile(f):
            size = os.path.getsize(f)
            ext = os.path.splitext(f)[1]
            print("Name:", f)
            print("Type:", ext)
            print("Size:", size)
            print("-------")

    list_files_info(".")            
