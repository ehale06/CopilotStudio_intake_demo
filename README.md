# Patient Intake Summary Agent - Copilot Studio + Claude AI

A fully functional AI agent built on Microsoft Copilot Studio that automates clinical patient intake summary generation for healthcare care coordinators. The agent accepts a conversational request, searches a structured patient dataset, retrieves multi-field patient records, and generates a professional clinical intake summary using Anthropic's Claude AI model - all within a single conversational interaction.

---

## Demo

[Watch the demo] https://www.loom.com/share/4e666cbb0d874827ab3db236a1b35e6b

---

## What It Does

A care coordinator opens the agent and types a patient name or partial name. The agent searches the patient dataset, returns matching results, asks the user to confirm the correct patient, then generates a complete professional clinical intake summary including demographics, vital signs with clinical interpretation, administrative status, a synthesized clinical narrative, and specific recommended next steps - all in one conversation.

See `sample_output.md` for an example of the generated output.

---

## Architecture

**Conversational layer - Microsoft Copilot Studio**

The agent handles natural language input, orchestrates two underlying Power Automate workflows, and presents generated output inline in the conversation. It manages the full interaction from initial patient name search through final document delivery.

**Workflow layer - Power Automate**

Two flows handle the core logic.

*SearchPatients* accepts a partial patient name, retrieves patient data via HTTP from a structured JSON dataset, filters for matching records, and returns candidate patients to the agent for user confirmation.

*GenerateIntakeSummary* accepts a unique PatientID, retrieves the complete patient record, constructs an engineered prompt combining the patient data with a structured clinical template, calls the Anthropic Claude API via HTTP, and returns the generated intake summary to the agent.

**AI layer - Anthropic Claude Haiku**

Called directly via REST API from Power Automate. Claude receives the patient data and clinical template as injected context and generates professional clinical narrative across all sections of the intake summary - interpreting vital signs, synthesizing a clinical narrative, and producing clinically appropriate recommended next steps based on the full patient presentation.

---

## Key Technical Capabilities

- Natural language patient search and disambiguation
- Multi-field data retrieval from structured JSON via HTTP
- Dynamic prompt construction with patient data and template injection as context
- LLM powered clinical document generation with clinical reasoning
- End to end conversational workflow from request to formatted output
- Enterprise Microsoft platform integration using Copilot Studio and Power Automate

---

## Repository Contents

| File | Description |
|------|-------------|
| `patients.json` | Synthetic patient dataset - 50 fictional patients across 3 merged data sources |
| `PatientIntakeTemplate.txt` | Clinical intake summary template injected into the Claude prompt |
| `generate_data.py` | Python script to generate synthetic patient Excel files |
| `generate_json.py` | Python script to merge and convert Excel data to JSON |
| `sample_output.md` | Example of a generated patient intake summary |

---

## Synthetic Data

All patient data is completely fabricated using Python and the Faker library. The dataset contains no real protected health information. It was designed to reflect realistic clinical diversity across demographics, diagnoses, medications, vital signs, and administrative statuses for demonstration purposes only.

The dataset was generated from three merged synthetic data sources: patient demographics, clinical intake data, and administrative flags. The data was joined on a unique PatientID key. This mirrors how real enterprise healthcare data is structured across systems.

---

## A Note on Data Storage

In this prototype the patient data is hosted as a JSON file on GitHub and retrieved via HTTP GET request from Power Automate. This approach was a practical workaround specific to the development environment used - a William and Mary institutional Microsoft account with restricted SharePoint and OneDrive Business connector access in Power Automate.

In a production deployment or within an organizational Microsoft 365 environment the data layer would be implemented using SharePoint lists, Microsoft Dataverse, or Azure SQL - all of which integrate natively with Power Automate without the HTTP workaround. The agent and flow architecture remains identical regardless of the underlying data storage choice.

---

## Stack

- Microsoft Copilot Studio
- Power Automate
- Anthropic Claude Haiku via REST API
- Python with Faker and pandas for synthetic data generation
- GitHub for dataset hosting

---

## Legal

All data in this repository is entirely synthetic and fictional. No real patient information was used at any stage of development. This project was built on personal time using personal accounts and personal API credentials. It is intended solely as a technical portfolio demonstration.

---

## Author

Ethan Hale
[github.com/ehale06](https://github.com/ehale06) | [linkedin.com/in/ethan-hale06](https://linkedin.com/in/ethan-hale06)
