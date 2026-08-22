# 📊 Sales Data Analyzer

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/bk2573011-boop/sales-data-analyzer)
[![Recruiter-Friendly](https://img.shields.io/badge/Recruiter--Friendly-Ready-brightgreen)](https://github.com/bk2573011-boop)

A clean, modular, and recruiter-friendly Python tool designed to ingest, clean, validate, and analyze sales transaction data from CSV files. It calculates critical business KPIs, runs multi-dimensional aggregations, and automatically generates beautiful terminal dashboards and persistent text reports.

---

## 🔍 Project Overview

In data analytics and software engineering, handling unstructured or semi-structured data robustly is a core requirement. This project showcases how to build a production-grade data analysis pipeline using **Python's standard library** alone, eliminating heavy external dependencies while maintaining clean, object-oriented, and highly readable code.

The analyzer loads sales records from a CSV source, applies validation rules (handling dates, numeric conversions, and edge cases), aggregates metrics across different dimensions (categories, products, time periods), and outputs a structured business report.

---

## ✨ Features

- **Standard Library Only:** Zero external dependencies (no `pandas` or `numpy` required), making it lightweight and instantly executable.
- **Robust Data Pipeline:** Handles common parsing challenges, validates CSV schemas, and flags malformed rows gracefully.
- **Business KPI Aggregations:** Computes essential metrics:
  - **Total Revenue & Cost**
  - **Net Profit & Net Profit Margin (%)**
  - **Average Order Value (AOV)**
  - **Units Sold**
- **Categorical Breakdown:** Evaluates sales volume, total revenue, and profitability per category (e.g., Electronics, Home & Kitchen, Books, Apparel).
- **Top Product Performance:** Lists top 3 performing items by revenue generated and total sales volume (quantity).
- **Temporal Trend Analysis:** Processes transactional dates to calculate monthly revenue trends, outputting a scaled ASCII horizontal bar chart directly to the console.
- **Automated Reporting:** Generates and saves a clean, formatted report file (`sales_report.txt`) for stakeholders.

---

## 🛠️ Technologies Used

- **Core Language:** Python 3.8+
- **Standard Libraries Used:**
  - `csv` — High-performance reading and parsing of tabular data.
  - `datetime` — Parse, sort, and format transaction timestamps.
  - `collections` (`defaultdict`) — Memory-efficient grouping and grouping operations.
  - `os` — Cross-platform path validation and file operations.

---

## 📂 File Structure

```text
sales-data-analyzer/
├── main.py             # Main entry point containing OOP logic & report builder
├── sales_data.csv      # Sample sales database containing mock transaction records
├── sales_report.txt    # Auto-generated text report (created after running main.py)
└── README.md           # Professional project documentation
```

---

## 🚀 How to Run

Follow these simple steps to run the sales data analyzer on your local machine.

### Prerequisites
Make sure you have Python 3 installed on your system. You can verify this by running:
```bash
python --version
```

### Installation & Execution
1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/bk2573011-boop/sales-data-analyzer.git
   cd sales-data-analyzer
   ```
2. Run the main script:
   ```bash
   python main.py
   ```
3. Check the console output or open the newly generated `sales_report.txt` file in your workspace to see the final report.

---

## 📊 Sample Output

Running `python main.py` prints a clean, easy-to-read ASCII dashboard to the terminal and saves it as `sales_report.txt`:

```text
============================================================
                    SALES PERFORMANCE REPORT                    
============================================================
Generated on: 2026-08-22 21:41:05
Data source: sales_data.csv
------------------------------------------------------------

[1] KEY PERFORMANCE INDICATORS
  - Total Transactions:  25
  - Total Units Sold:    358
  - Total Revenue:       $12,730.00
  - Total Net Profit:    $7,241.00
  - Average Order Value: $509.20
  - Profit Margin:       56.88%
------------------------------------------------------------

[2] PERFORMANCE BY PRODUCT CATEGORY
  Category             |   Qty |      Revenue |       Profit
  ------------------------------------------------------
  Home & Kitchen       |    88 | $   3,670.00 | $   1,986.00
  Apparel              |    99 | $   3,580.00 | $   2,103.00
  Electronics          |    64 | $   3,470.00 | $   1,926.00
  Books                |   107 | $   2,010.00 | $   1,226.00
------------------------------------------------------------

[3] TOP PERFORMING PRODUCTS (Revenue)
  1. Running Shoes                  | $1,200.00
  2. Wireless Earbuds               | $1,080.00
  3. Office Chair                   | $900.00

[4] TOP PERFORMING PRODUCTS (Volume / Quantity)
  1. Mechanical Pencil Set          | 40 units
  2. Notebook (5-Pack)              | 35 units
  3. T-Shirt                        | 30 units
------------------------------------------------------------

[5] MONTHLY REVENUE TRENDS
  Month      | Monthly Revenue | Visual Trend (Scaled)
  ------------------------------------------------------
  2026-01    | $        765.00 | #####
  2026-02    | $      2,710.00 | ####################
  2026-03    | $      1,230.00 | #########
  2026-04    | $      1,980.00 | ##############
  2026-05    | $      1,580.00 | ###########
  2026-06    | $      1,590.00 | ###########
  2026-07    | $      1,505.00 | ###########
  2026-08    | $      1,370.00 | ##########
============================================================

[Success] Report saved successfully to 'sales_report.txt'
```

---

## 🔮 Future Improvements

Here are a few exciting features planned for future updates:
1. **Interactive Web Dashboard:** Build a lightweight web application using Streamlit or Flask/React to visualize data dynamically.
2. **Database Integration:** Connect the analyzer to an SQLite or PostgreSQL database to handle large-scale datasets.
3. **Advanced Visualizations:** Use `matplotlib` and `seaborn` to output professional sales graphs (e.g., trend lines, pie charts for category share) as PNG files.
4. **Automated Unit Tests:** Add comprehensive unit tests using `pytest` to verify the accuracy of metrics calculations.
5. **PDF Export Support:** Implement a PDF report exporter using `ReportLab`.

---

## 👤 Author

**Bibha Kumari** (GitHub: [@bk2573011-boop](https://github.com/bk2573011-boop))

*Feel free to star ⭐️ this repository if you found it useful!*
