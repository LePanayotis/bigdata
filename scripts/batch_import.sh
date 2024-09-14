#!/bin/bash

TABLE_NAME=
CSV_DIR=

for FILE in $CSV_DIR/*; do
    echo "Importing $FILE..."
    psql  postgresql://user:password@address/databsase -c "\COPY $TABLE_NAME (inv_date_sk,inv_item_sk,inv_warehouse_sk,inv_quantity_on_hand) FROM '$FILE' WITH DELIMITER '|' CSV HEADER;"
    echo "$FILE imported successfully."
done