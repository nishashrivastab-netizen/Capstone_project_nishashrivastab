# Mamaearth Growth Analytics Pipeline
This documentation explains how to execute my data pipeline from top to bottom.

## 1. Database Setup (SQL)
To initialize the database, load and execute the SQL files in this exact order:
* Execute `sql/schema.sql` to create the required table structures.
* Execute `sql/seed_data.sql` to populate tables with transaction records.
* Execute `sql/reports.sql` to run metrics and check query outputs.

## 2. Python Data Analysis
To run the automated data cleaning and analytics workflow, execute the scripts in this sequence:
* Run `analysis/clean_and_eda.py` to remove duplicates and output cleaned rows.
* Run `analysis/visualize.py` to generate the trend evaluation graphs.

## 3. Verified Metrics Storage
* The validated statistical figures from my code are exported and stored inside `narrator/findings.json`.

## 4. GenAI Narrative Generation
To run the final business report script `narrator/generate_narrative.py`, you can choose between two modes:
* **Online Mode:** Run the script with an active Gemini API key saved in your environment variables as `NISHA_GEMINI_API_KEY`.
* **Offline Mode:** Run the script with no key configured. The pipeline will automatically route through the pre-formatted offline path without any network dependencies.
