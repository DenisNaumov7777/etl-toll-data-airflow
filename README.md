````markdown
## 1️⃣ Recommended Repository Structure 📁

```text
etl-toll-data-airflow/
├── dags/
│   └── ETL_toll_data.py
├── staging/
│   └── .gitkeep
├── screenshots/
│   ├── dag_args.jpg
│   ├── dag_definition.jpg
│   ├── unzip_data.jpg
│   ├── extract_data_from_csv.jpg
│   ├── extract_data_from_tsv.jpg
│   ├── extract_data_from_fixed_width.jpg
│   ├── consolidate_data.jpg
│   ├── transform.jpg
│   ├── task_pipeline.jpg
│   ├── submit_dag.jpg
│   ├── unpause_trigger_dag.jpg
│   ├── dag_tasks.jpg
│   └── dag_runs.jpg
├── .gitignore
├── README.md
└── LICENSE
````

---

# ETL Toll Data Pipeline (Apache Airflow) 🚦

**Author:** Denis Naumov
**Role:** Data Engineer
**Stack:** Apache Airflow, Bash, Linux, CSV / TSV / Fixed-width files

---

## 📌 Project Overview

This project implements a production-style **ETL pipeline using Apache Airflow** to consolidate heterogeneous toll road traffic data from multiple toll operators into a single structured dataset.

Each operator provides data in a different format:

* CSV
* TSV
* Fixed-width text file

The pipeline extracts, transforms, and consolidates the data into a unified staging dataset for downstream analytics.

---

## 🎯 Objectives

The Airflow DAG performs the following steps:

1. Extract data from a CSV file
2. Extract data from a TSV file
3. Extract data from a fixed-width file
4. Consolidate extracted datasets
5. Transform vehicle type values to uppercase
6. Store the final output in a staging area

---

## 🧱 Architecture

```text
Raw Data (tgz)
   ↓
Unzip
   ↓
Extract (CSV | TSV | Fixed-width)
   ↓
Consolidate
   ↓
Transform
   ↓
Staging Output
```

---

## ⚙️ DAG Details

* **DAG ID:** `ETL_toll_data`
* **Schedule:** Daily
* **Operator Type:** `BashOperator`
* **Retry Policy:**

  * Retries: 1
  * Retry Delay: 5 minutes
* **Email Alerts:** Enabled for failure and retry

---

## 🗂️ Data Flow

| Step                | Output File            |
| ------------------- | ---------------------- |
| CSV Extract         | `csv_data.csv`         |
| TSV Extract         | `tsv_data.csv`         |
| Fixed-width Extract | `fixed_width_data.csv` |
| Consolidation       | `extracted_data.csv`   |
| Transformation      | `transformed_data.csv` |

---

## 📁 Staging Directory

```bash
/home/project/airflow/dags/finalassignment/staging
```

This directory stores the final transformed dataset.

---

## 🚀 How to Run

1. Place the DAG file in your Airflow `dags/` directory
2. Start Airflow:

   ```bash
   airflow webserver
   airflow scheduler
   ```
3. Unpause the DAG:

   ```bash
   airflow dags unpause ETL_toll_data
   ```
4. Trigger the DAG and monitor execution

---

## 🖼️ Screenshots

All required execution and validation screenshots are stored in the `screenshots/` directory:

* DAG definition
* Task pipeline
* Task execution
* Successful DAG runs

---

## 🧠 Engineering Notes

* Uses Linux-native utilities (`cut`, `paste`, `tr`) for efficient ETL processing
* Designed for clarity, reproducibility, and operational simplicity
* Follows Apache Airflow best practices for DAG design and task dependencies

---

## 📜 License

MIT License

© 2025 Denis Naumov

```
```
