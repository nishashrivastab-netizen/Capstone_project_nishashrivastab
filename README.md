# Mamaearth Growth Analytics Pipeline
This documentation explains how to execute my data pipeline from top to bottom.

## 1. Database Setup (SQL)
To initialize the database, load and execute the SQL files in this exact order:
* Execute sql/schema.sql: Relational tables logic map definition (customers, products, orders).
* Execute sql/seed_data.sql: Populates the operational records for Mamaearth skincare, haircare, and babycare lines.
* Execute sql/reports.sql: Runs baseline SQL diagnostic checking to verify database integrity.

## 2. Python Data Analysis
To run the automated data cleaning and analytics workflow, execute the scripts in this sequence:
*  Run `analysis/clean_and_eda.py` to fix formats, handle types, impute ratings, and clean 5 duplicates (leaving 175 clean rows).
* Run `analysis/visualize.py` to filter January noise, verify March 2026 peak month (₹20,318.90), and run Pearson matrix checks (r < 0.2). 

## 3. Verified Metrics Storage
  * The validated statistical figures from my code are exported and stored inside `narrator/findings.json` mapping:
  * Cleaned Revenue tracking at **₹97,358.30** (Reconciliation Delta of **₹2,501.90** lower than raw logs).
  * High-risk fields tracking: **COD shows a 44.4% return rate**, spiking inside **Tier 2 locations with 54.5% discounts**.

## 4. GenAI Narrative Generation
To run the final business report script `narrator/generate_narrative.py`, you can choose between two modes:
* **Online Mode:** Run the script with an active Gemini API key saved in your environment variables as `NISHA_GEMINI_API_KEY`.
* **Offline Mode:** Run the script with no key configured. The pipeline will automatically route through the pre-formatted offline path without any network dependencies.
* * **Validation Checker:** Programmatically audits the narrative text logic against findings.json to verify metrics accuracy (Result: METRIC CHECK: HARD PASS).

