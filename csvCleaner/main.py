import csv
import os
import yaml
import logging
from datetime import datetime

#Setup

with open("config.yaml") as f:
    config = yaml.safe_load(f)

INPUT_DIR = config["input_dir"]
OUTPUT_DIR = config["output_dir"]
LOG_FILE = config["log_file"]
REQUIRED_COLS = config["required_columns"]

os.makedirs(OUTPUT_DIR, exist_ok = True)
os.makedirs("logs", exist_ok = True)

logging.basicConfig(
        filename = LOG_FILE,
        level = logging.INFO,
        format = "%(asctime)s [%(levelname)s] %(message)s"
        )

logging.info("Script Started")

#Helpers

def valid_row(row):
    return all(row.get(col, "").strip() for col in REQUIRED_COLS)

#Main

output_file = os.path.join(
        OUTPUT_DIR, f"cleaned_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
        )

total = valid = skipped = 0

with open(output_file, 'w', newline = "") as out:
    writer = None

    for filename in os.listdir(INPUT_DIR):
        if not filename.endswith(".csv"):
            continue

        path = os.path.join(
                INPUT_DIR, filename)

        logging.info(f"Processing {filename}")
        
        with open(path, newline = "") as f:
            reader = csv.DictReader(f)
            
            if writer is None :
                writer = csv.DictWriter(out, fieldnames = reader.fieldnames)
                writer.writeheader()

            for row in reader:
                total += 1
                if valid_row(row):
                    writer.writerow(row)
                    valid += 1
                else:
                    skipped += 1

logging.info("Script Finished")
logging.info(f"Total Rows: {total}")
logging.info(f"Valid Rows: {valid}")
logging.info(f"Skipped Rows: {skipped}")

print("Done!!")
