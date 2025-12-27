import csv
import os
import yaml
import logging
from datetime import datetime
from collections import defaultdict

#Setup

with open("config.yaml") as f:
    config = yaml.safe_load(f)

INPUT_DIR = config["input_dir"]
OUTPUT_DIR = config["output_dir"]
LOG_FILE = config["log_file"]
REQUIRED_COLS = config["required_columns"]
REPORT_PATH = config["report_dir"]

os.makedirs(OUTPUT_DIR, exist_ok = True)
os.makedirs("logs", exist_ok = True)

logging.basicConfig(
        filename = LOG_FILE,
        level = logging.INFO,
        format = "%(asctime)s [%(levelname)s] %(message)s"
        )

logging.info("Script Started")

#Helpers

def extract_domain(email: str) -> str:
    if "@" not in email:
        return "invalid"
    return email.split("@")[-1].lower()

def valid_row(row):
    for col in REQUIRED_COLS:
        if not row.get(col, "").strip():
            return False, f"Missing Field: {col}"
    return True, ""

#Main

total = valid = skipped = 0
domain_counts = defaultdict(int)

for filename in os.listdir(INPUT_DIR):
    if not filename.endswith(".csv"):
        continue
    
    path = os.path.join(INPUT_DIR, filename)
    logging.info(f"Processing {filename}")

    with open(path, newline = "") as f:
        reader = csv.DictReader(f)
        for row in reader:
            is_valid, reason = valid_row(row)
            total += 1

            if is_valid:
                valid += 1
                email = row.get("email","")
                domain = extract_domain(email)
                domain_counts[domain] += 1
            else:
                skipped += 1
                logging.warning(f"Skipped Line : {reason}")

    f.close()

summary_path = os.path.join(REPORT_PATH, f"Summary_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt")

with open(summary_path, "w") as f:
    f.write("CSV Mail User Report\n")
    f.write("="*30 + "\n\n")
    f.write(f"Total rows processed: {total}\n")
    f.write(f"No. of validated rows: {valid}\n")
    f.write(f"No. of Skipped rows: {skipped}\n\n")

    f.write("Email domain breakdown\n")
    for domain, count in sorted(domain_counts.items()):
        f.write(f"{domain} : {count}\n")

logging.info("Script Finished")
logging.info(f"Total Rows: {total}")
logging.info(f"Valid Rows: {valid}")
logging.info(f"Skipped Rows: {skipped}")

print("Done!!")
