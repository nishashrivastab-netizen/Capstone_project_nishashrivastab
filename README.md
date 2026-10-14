Mamaearth Growth Analytics Pipeline

This documentation explains how to execute my data pipeline from top to bottom, detailing each operational step and the insights generated.

1. Database Setup (SQL)

To initialize the database, load and execute the SQL files in this exact order:
• sql/schema.sql: Relational tables logic map definition (customers, products, orders).
• sql/seed_data.sql: Populates the operational records for Mamaearth skincare, haircare, and babycare lines.
• sql/reports.sql: Runs baseline SQL diagnostic checking to verify database integrity.

2. Python Data Analysis

To run the automated data cleaning and analytics workflow, execute the scripts in this sequence:
• analysis/clean_and_eda.py: Fixes single-string formats, standardizes text casing (UPI, CARD, COD), imputes empty entries (missing rating filled by median), and cleans out 5 duplicate rows (leaving exactly 175 clean rows).
• analysis/visualize.py: Runs outlier-corrected time series analysis. Filters out January bulk orders to reveal March 2026 as the genuine sales peak month (₹20,318.90). Runs Pearson checks confirming negligible metrics correlation (r < 0.2).

3. Verified Metrics Storage

• The validated statistical figures from my code execution are exported directly into data/findings.json, mapping:
	• Cleaned Revenue tracking at ₹97,358.30 (Delta of ₹2,501.90 lower than raw logs due to duplicates removal).
	• High-risk operational fields tracking: COD transactions show a 44.4% return rate, heavily concentrated in Tier 2 locations with 54.5% discounts.

4. GenAI Narrative Generation

To run the final business report script narrator/generate_narrative.py, choose between two workspace settings:
• Online Mode: Runs with the deterministic Gemini 1.5 Flash framework via the NISHA_GEMINI_API_KEY to automate the executive operations summary.
• Offline Mode: Uses system pre-formatted local fallback routing for seamless execution.
• Validation Checker: Programmatically audits the narrative text logic against findings.json to verify metrics accuracy (Result: METRIC CHECK: HARD PASS).
