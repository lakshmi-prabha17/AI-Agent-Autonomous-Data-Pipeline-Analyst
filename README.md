# Autonomous Data Pipeline Analyst Agent 📊💼

An enterprise-grade AI agent designed to automate corporate data hygiene workflows. Leveraging the **Google Agent Development Kit (ADK)** and the **gemini-2.5-flash** model, this agent safely ingest raw production datasets, programmatically strips duplicates and missing values using a custom Python pipeline tool, and synthesizes data quality metrics into a polished Executive Business Intelligence Summary.

---

## 🚀 The Solution & Business Value

In corporate environments, data analysts waste up to 80% of their time manually cleaning spreadsheets and fixing pipeline anomalies before generating reports. 

This agent eliminates that operational bottleneck by providing a natural language interface over an immutable data-cleaning function. It prevents LLM hallucinations of critical metrics by strictly isolating data calculations within a deterministic Python function, delivering reliable, boardroom-ready analysis instantly.

---

## 🏗️ System Architecture

The project implements a single-agent orchestrator architecture bounded to native system environments. It strictly separates natural language reasoning from computational data manipulation to ensure execution reliability.

[User Chat Prompt] ---> [Data_Pipeline_Analyst_Agent (gemini-2.5-flash)]
|
(Orchestrates & Validates)
|
v
[Skill Tool: clean_and_analyze_dataset]
|
(Executes pandas Engine)
|
v
[production_data.csv]

### Applied Course Concepts
* **Deterministic Tool Binding:** Connected via the Google ADK framework to allow the model to actively call local functional skills instead of guessing numbers.
* **Token Efficiency:** Leverages `gemini-2.5-flash` for rapid intent recognition and structured reporting.
* **Credential Isolation:** Implements secure `.env` environment variables to prevent accidental exposure of API keys in public codebases.

---

## 🛠️ Code Structure & Implementation

The project directory is structured cleanly to optimize modular execution within the Google ADK web server ecosystem:

* **`agent.py`**: Initializes the main agent instance (`root_agent`), sets its professional analytical personas, maps instructions, and registers the data cleaning skill tool.
* **`data_tool.py`**: Houses the strict data manipulation logic written in Python utilizing the `pandas` library. Processes records, drops duplicates, removes null fields, and passes raw success dictionaries back to the orchestrator.
* **`__init__.py`**: Configures runtime path-appending configurations and exposes `root_agent` cleanly to the development kit server.

---

## 📊 Live Validation Performance

During validation testing on an anonymized workforce dataset (`production_data.csv`), the agent achieved the following data pipeline milestones:
* **Initial Dataset Size:** Ingested 5,150 raw records.
* **Automated Data Quality Protection:** Cleaned and dropped **495 anomalous records** consisting of duplicate entries and null rows.
* **Data Anomaly Suppression:** Safely neutralized a **9.6% data corruption rate** across critical corporate parameters (`employee_id`, `full_name`, `department`, `salary`, `performance_score`, `hire_year`).
* **Cleaned Output Yield:** Exported a 4,655-record, high-fidelity dataset along with a comprehensive executive report.

---

## 💻 Local Setup & Deployment Instructions

Follow these instructions to clone, configure, and execute the agent development kit locally.

### 1. Prerequisites
Ensure you have Python 3.11+ installed on your local machine.

### 2. Installation & Directory Setup
Navigate to your active directory environment and install the required dependencies:
```bash
pip install pandas openpyxl ```
### 3. Environment Configuration
Create a hidden configuration file named `.env` in the project root folder. Add your Google API credentials exactly as follows:

```text
GEMINI_API_KEY=YOUR_SECRET_GEMINI_API_KEY_HERE```
### 4.Pointing the server to look inside the active root path
..\Day3_Agent_Skills\.venv\Scripts\adk web .
### 5.Accessing the Web UI
Open your browser and navigate to the default local address:
[http://127.0.0.1:8000](http://127.0.0.1:8000)

Click "New Session" to clear the chat timeline and submit your pipeline request.
