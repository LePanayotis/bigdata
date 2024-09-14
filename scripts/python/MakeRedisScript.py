import os
import csv

work_dir = "."
result_dir = "./redis_scripts"
schema = "r"



def convert2redis(table, primary_key):
    infile = os.path.join(work_dir,f"{table}.txt")
    outfile = os.path.join(result_dir,f"redis_{table}.txt")
    with open(infile, mode='r') as csv_file, open(outfile, 'w') as out_csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter="|")
        for row in csv_reader:
            insert = f"""HSET {schema}:{table}:{row[primary_key]} {' '.join(f'{key} "{value}"' for key, value in row.items())}\n"""
            
            out_csv_file.write(insert)

table_data = [
    ("ship_mode", "sm_ship_mode_sk"),
    ("call_center", "cc_call_center_sk"),
    ("customer_address", "ca_address_sk"),
    ("customer_demographics", "cd_demo_sk"),
    ("customer", "c_customer_sk"),
    ("dbgen_version","dv_version"),
    ("household_demographics", "hd_demo_sk"),
    ("income_band", "ib_income_band_sk"),
    ("promotion", "p_promo_sk"),
    ("reason", "r_reason_sk"),
    ("store", "s_store_sk"),

    ("time_dim", "t_time_sk"),
    ("web_site", "web_site_sk")
]

for t in table_data:
    convert2redis(t[0], t[1])
    print(f"{t[0]} completed")
