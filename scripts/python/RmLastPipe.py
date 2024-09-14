import sys

def remove_last_pipe(input_file, output_file):
    try:
        with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
            for line in infile:
                line = line
                if line[-2] == '|':
                    line = line[:-2]
                outfile.write(line)
                outfile.write('\n')
        print(f"Processed file saved as {output_file}")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    if len(sys.argv) != 3:
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]
    remove_last_pipe(input_file, output_file)

if __name__ == "__main__":
    main()
