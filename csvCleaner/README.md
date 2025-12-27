# CSV Cleaner

A Python automation tool to clean and validate messy CSV datasets using configurable rules.

## What this tool does
- Validates required columns
- Safely removes invalid or incomplete rows
- Generates a clean output CSV
- Logs execution details for transparency
- Safe to re-run (no overwrites)

## Use cases
- Cleaning business datasets
- Preparing data for analytics
- Data migration and audits
- Preprocessing CSV exports

## How it works
- Input CSV files are read as dictionaries (column-based)
- Rows missing required values are skipped
- Valid rows are written to a new cleaned CSV
- Logs track total, valid, and skipped rows

## Configuration
Edit `config.yaml` to change behavior without touching code.

Example:

input_dir: data/input
output_dir: data/output
log_file: logs/run.log

required_columns:
  - id
  - name
  - email

