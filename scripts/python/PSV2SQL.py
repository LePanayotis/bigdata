import csv
import sys

def psv_to_sql(psv_file, table_name):
    counter = 0
    with open(psv_file, 'r') as file:
        reader = csv.reader(file, delimiter='|')
        headers = next(reader)

        if headers[-1] == '':
            headers = headers[:-1]

        insert_statements = []

        for row in reader:
            counter += 1

            if row[-1] == '':
                row = row[:-1]
            values = []
            for value in row:
                if value.isdigit() or value.isdecimal():
                    values.append(value)
                elif value == '':
                    values.append('NULL')
                else:
                    values.append(value)

            insert_statement = f"INSERT INTO {table_name} ({', '.join(headers)}) VALUES ({', '.join(values)});"
            insert_statements.append(insert_statement)

    return insert_statements

if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(1)

    psv_file = sys.argv[1]
    table_name = sys.argv[2]

    insert_statements = psv_to_sql(psv_file, table_name)

    output_file = psv_file.replace('.txt', '.sql')
    with open(output_file, 'w') as file:
        for statement in insert_statements:
            file.write(statement + '\n')

    print(f"SQL insert statements have been written to {output_file}")
