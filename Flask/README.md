# EcoAudit - Regulatory Technology Compliance Dashboard

A Flask-based institutional compliance and verification system prototype designed for demonstration at Delhi Technological University (DTU).

## Overview

EcoAudit is a **third-party national compliance infrastructure** that:

- Enables universities to outsource regulatory reporting
- Converts campus activities into audit-grade evidence
- Benchmarks institutions at a national level
- Aligns data with NAAC, NIRF 2026, SWM 2026, and SEBI BRSR Core frameworks

## Technology Stack

- **Python 3** with **Flask** web framework
- **Jinja2** server-rendered templates
- **Static JSON** data files (no database)
- **Vanilla CSS** styling

## Project Structure

```
Flask/
├── app.py                      # Main Flask application
├── data/
│   ├── dtu_events.json         # Campus events and activities
│   ├── dtu_metrics.json        # Compliance metrics and KPIs
│   └── public_benchmark.json   # National institutional comparison
├── templates/
│   ├── base.html               # Base template with header/footer
│   ├── index.html              # Landing page
│   ├── dtu_dashboard.html      # DTU institutional dashboard
│   └── public_dashboard.html   # Public national benchmark
├── static/
│   └── style.css               # Government/audit-grade styling
└── README.md                   # This file
```

## Setup Instructions

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. **Navigate to the project directory:**
   ```bash
   cd Flask
   ```

2. **Create a virtual environment (recommended):**
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment:**
   - Windows:
     ```bash
     venv\Scripts\activate
     ```
   - macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install Flask:**
   ```bash
   pip install flask
   ```

### Running the Application

```bash
python app.py
```

The application will start on `http://127.0.0.1:5000/`

## Routes / Dashboards

### 1. Home Page (`/`)

Landing page with navigation to both dashboards and overview of supported regulatory frameworks.

### 2. DTU Institutional Dashboard (`/institution/dtu`)

**Primary dashboard** showing:

- **KPI Summary Cards:**
  - Institutional Trust Score (verified activities ratio)
  - Community Wealth Generated (₹ value of impact)
  - The Landfill Gap (waste diversion shortfall)
  - Audit Readiness Status (risk assessment)

- **Verification Pipeline Status:**
  - Logged → Under Verification → Verified → Flagged

- **Events & Activities Table:**
  - Campus events with verification measures and regulatory mapping
  - Categories: Human & Social Capital, Circular Economy, Waste/SWM, Innovation & Research

- **Compliance Coverage Matrix:**
  - NAAC, NIRF 2026, SWM 2026, SEBI CSR coverage and risk levels

- **Metric Clusters:**
  - Human & Social Capital (EVV, NCrF Credits, Knowledge Equity)
  - Circular Economy (CMU Rate, Resource Life Extension)
  - Waste & SWM Compliance (ZWTL%, Segregation Efficiency)
  - Innovation & Research (TRL Score, Pilot Scalability)

### 3. Public Benchmark Dashboard (`/public/benchmark`)

**National comparison dashboard** showing:

- Institutional comparison table (Trust Score, Community Wealth, ZWTL%, Assurance Level)
- Detailed institution profile cards
- Methodology notes explaining metrics
- Includes: IIT Delhi, DTU, NSUT, MAIT, IGDTUW

## Data Files

### `dtu_events.json`
Contains 16 campus events including:
- E-Waste Collection Drive
- Blood Donation Camp
- Tree Plantation Drive
- SATARK Financial Literacy Workshop
- National Voters' Day Mock Elections
- And more...

### `dtu_metrics.json`
Contains:
- Summary KPIs (community wealth, landfill gap, audit readiness)
- Compliance coverage matrix for 4 regulatory frameworks
- Metric clusters with 15+ individual metrics

### `public_benchmark.json`
Contains:
- 5 Delhi-NCR institutions with comparative data
- Trust scores, community wealth, ZWTL percentages
- Assurance levels and methodology notes

## Regulatory Frameworks Supported

| Framework | Description |
|-----------|-------------|
| **NAAC** | National Assessment and Accreditation Council |
| **NIRF 2026** | National Institutional Ranking Framework |
| **SWM 2026** | Solid Waste Management Rules |
| **SEBI BRSR Core** | Business Responsibility and Sustainability Reporting |
| **NCrF** | National Credit Framework |
| **NEP 2020** | National Education Policy |

## Design Philosophy

This prototype is designed to appear as:
- ✅ A government portal
- ✅ An audit console
- ✅ A compliance control room

NOT as:
- ❌ A student app
- ❌ An NGO website
- ❌ A startup landing page

## Disclaimer

**This is a demonstrative prototype.** All data shown is illustrative and does not represent actual institutional performance or compliance status.

---

*EcoAudit RegTech Infrastructure - Prototype Version*  
*Developed for presentation at Delhi Technological University*
