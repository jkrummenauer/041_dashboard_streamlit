# Goods Receiving Inspection Dashboard

🌐 Language: [Português](README.pt-BR.md) | English


Application developed with **Python** and **Streamlit** to automate the control, analysis, and monitoring of goods receiving inspection performance.

The dashboard transforms operational files into clear information to support decision-making, identify bottlenecks, monitor team productivity, and reduce the time spent on manual spreadsheet analysis.

## Overview

Companies that handle goods receiving and inspection operations need to monitor indicators such as inspected volume, operation time, identified discrepancies, and inspector productivity.

When these analyses are performed manually, the process can be time-consuming, generate rework, and make it difficult to identify operational issues.

This project centralizes the information in an interactive dashboard, allowing managers to monitor the main operational indicators quickly and visually.

## Demo

Add an image or animation of the dashboard in operation in this section.

```markdown
![Goods Receiving Inspection Dashboard](docs/images/dashboard.png)
```

## Main Benefits

- Reduction of time spent on manual spreadsheet analysis
- Centralization of inspection performance indicators
- Identification of bottlenecks and productivity losses
- Monitoring of individual inspector performance
- Identification of suppliers with higher discrepancy rates
- Support for data-driven decision-making
- Export of results for sharing and further analysis

## Features

- Upload of CSV or Excel files
- Automatic validation of required columns
- Data processing and standardization
- Filters by period, supplier, goods type, and inspector
- General operational indicators
- Inspector productivity ranking
- Supplier performance analysis
- Discrepancy analysis
- Interactive charts
- Automatic alerts for situations that require attention
- Export of filtered data to CSV
- Export of results to Excel

## Available Indicators

The dashboard allows users to monitor indicators such as:

- Total inspected goods volume
- Number of inspections performed
- Average inspection time
- Average inspected volume per operation
- Productivity by inspector
- Total number of discrepancies
- Discrepancy rate by supplier
- Inspector ranking
- Suppliers with the highest incidence of issues

## Analysis Filters

The data can be analyzed dynamically using filters by:

- Period
- Supplier
- Goods type
- Inspector

The indicators, tables, and charts are automatically updated according to the selected filters.

## Expected File Structure

The imported file must contain the following columns:

```text
data
conferencia_id
fornecedor
tipo_mercadoria
conferente
volume_conferido
tempo_minutos
divergencias
```

## Sample Data

| data | conferencia_id | fornecedor | tipo_mercadoria | conferente | volume_conferido | tempo_minutos | divergencias |
|---|---:|---|---|---|---:|---:|---:|
| 2026-05-01 | 1001 | Supplier A | Food | John | 450 | 35 | 2 |
| 2026-05-01 | 1002 | Supplier B | Beverages | Mary | 620 | 42 | 0 |
| 2026-05-02 | 1003 | Supplier A | Cleaning Products | Charles | 380 | 31 | 4 |

## Technologies Used

- Python
- Streamlit
- Pandas
- Plotly
- OpenPyXL

## How to Run the Project

Clone the repository:

```bash
git clone REPOSITORY_URL
cd PROJECT_NAME
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the virtual environment on macOS or Linux:

```bash
source .venv/bin/activate
```

Activate the virtual environment on Windows:

```bash
.venv\Scripts\activate
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

After execution, the dashboard will open in the browser.

## Customization Possibilities

The solution can be adapted to different operational needs, including:

- Integration with files exported from ERP systems
- Addition of new performance indicators
- Creation of goals by inspector or team
- Automatic report delivery
- Database integration
- User access control
- Deployment to a web or cloud environment
- Customization of the company’s visual identity

## Possible Applications

This dashboard can be used by companies that work with:

- Goods receiving
- Distribution centers
- Supermarkets
- Wholesalers
- Logistics operations
- Inventory control
- Supplier auditing

## Project Objective

This project was developed to demonstrate how Python and Streamlit can be used to transform operational data into a simple, visual, and efficient management tool.

The solution is especially useful for companies that still depend on manual spreadsheets and want to improve control, productivity, and operational quality.

## Author

**Jorge Krummenauer**

Engineering, industrial management, and software development applied to process improvement, cost reduction, and decision-making.