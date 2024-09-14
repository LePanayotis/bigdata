import sys

def count_rows(file_path):
    try:
        with open(file_path, 'r') as file:
            row_count = sum(1 for _ in file)
        return row_count
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return None

def main():
    if len(sys.argv) < 2:
        sys.exit(1)
    total = 0
    for file_path in sys.argv[1:]:
        row_count = count_rows(file_path)
        if row_count is not None:
            print(f"{file_path}: {row_count} rows")
            total += row_count
    print(f"Total rows: {total}")
if __name__ == "__main__":
    main()
