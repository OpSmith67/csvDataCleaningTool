# CSV Summary Report Generator

A Python automation tool that generates clear, human-readable summary reports from CSV datasets.

This tool is designed to give quick insights into data quality and structure without requiring any technical background.

---

## What this tool does

- Processes one or more CSV files
- Validates rows based on required columns
- Counts total, valid, and skipped rows
- Generates a readable summary report
- Breaks down records by email domain
- Logs execution details for transparency

---

## Typical use cases

- Data quality checks before analytics
- Dataset audits and reporting
- Business and compliance summaries
- Quick overview of large CSV exports
- Validation reports for cleaned datasets

---

## Configuration

All behavior is controlled via `config.yaml`.  
No code changes are required.

Example configuration:

```yaml
input_dir: data/input
output_dir: data/output
log_file: logs/run.log
report_dir: data/reports

required_columns:
  - id
  - name
  - email

## Usage 
- Configure the environment throug config.yaml
- Run ./main.py 
- Check the report ar report_dir
- Check the errors and warnings at ./logs/logs.txt
