import sys
import os
import math

def count_rows(file_path):
    try:
        with open(file_path, 'r') as file:
            row_count = sum(1 for _ in file)
        return row_count
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return None

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

def get_file_size_abs(file_path):
    """Return the size of the file in a human-readable format."""
    size_bytes = os.path.getsize(file_path)
    return size_bytes


def main():
    if len(sys.argv) < 2:
        sys.exit(1)
    total = 0
    for file_path in sys.argv[1:]:
        row_count = get_file_size_abs(file_path)
        if row_count is not None:
            print(f"{file_path}: {row_count} B")
            total += row_count
    print(f"Total rows: {total}")
if __name__ == "__main__":
    main()
