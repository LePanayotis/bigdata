import sys

def count_columns_in_psv(file_path):
    
    with open(file_path, 'r') as file:
        
        header_line = file.readline().strip()
        columns = header_line.split('|')
        return len(columns)


def main():
    if len(sys.argv) < 2:
        sys.exit(1)
    for file_path in sys.argv[1:]:
        row_count = count_columns_in_psv(file_path)
        if row_count is not None:
            print(f"{file_path}: {row_count} columns")
if __name__ == "__main__":
    main()
