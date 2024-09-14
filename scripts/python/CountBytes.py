import os
import sys
import math

def get_file_size(file_path):
    """Return the size of the file in a human-readable format."""
    size_bytes = os.path.getsize(file_path)
    
    if size_bytes == 0:
        return "0B"
    
    size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
    i = int(math.floor(math.log(size_bytes, 1024)))
    p = pow(1024, i)
    s = round(size_bytes / p, 2)
    
    return f"{s} {size_name[i]}"

def main():
    if len(sys.argv) < 2:
        sys.exit(1)
    for file_path in sys.argv[1:]:
        row_count = get_file_size(file_path)
        if row_count is not None:
            print(f"{file_path}: {row_count}")
if __name__ == "__main__":
    main()
