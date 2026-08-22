"""
Sales Data Analyzer
-------------------
A clean, modular, and professional Python tool that reads, validates, and analyzes
sales transaction data from a CSV file. It calculates key business performance 
metrics, generates a performance dashboard, and exports the report to a text file.

Author: bk2573011-boop
"""

import os
import csv
from datetime import datetime
from collections import defaultdict
from typing import Dict, List, Tuple, Any

class SalesAnalyzer:
    """Class to load, validate, and analyze sales CSV data."""
    
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.data: List[Dict[str, Any]] = []
        self.total_revenue = 0.0
        self.total_cost = 0.0
        self.total_profit = 0.0
        self.units_sold = 0
        
    def load_data(self) -> bool:
        """Loads data from the CSV file and performs validation.
        
        Returns:
            bool: True if data loaded successfully, False otherwise.
        """
        if not os.path.exists(self.file_path):
            print(f"Error: File not found at '{self.file_path}'")
            return False
            
        try:
            with open(self.file_path, mode='r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                
                # Verify required headers are present
                required_headers = {'Transaction_ID', 'Date', 'Product', 'Category', 
                                    'Quantity', 'Amount', 'Unit_Cost', 'Total_Cost', 'Profit'}
                headers = set(reader.fieldnames or [])
                if not required_headers.issubset(headers):
                    missing = required_headers - headers
                    print(f"Error: Missing required columns in CSV: {missing}")
                    return False
                
                for row_idx, row in enumerate(reader, start=1):
                    try:
                        # Parse and clean fields
                        txn_id = row['Transaction_ID'].strip()
                        date_str = row['Date'].strip()
                        date = datetime.strptime(date_str, '%Y-%m-%d')
                        product = row['Product'].strip()
                        category = row['Category'].strip()
                        quantity = int(row['Quantity'])
                        amount = float(row['Amount'])
                        unit_cost = float(row['Unit_Cost'])
                        total_cost = float(row['Total_Cost'])
                        profit = float(row['Profit'])
                        
                        # Store structured data row
                        self.data.append({
                            'txn_id': txn_id,
                            'date': date,
                            'product': product,
                            'category': category,
                            'quantity': quantity,
                            'amount': amount,
                            'unit_cost': unit_cost,
                            'total_cost': total_cost,
                            'profit': profit
                        })
                        
                        # Accumulate key performance metrics
                        self.total_revenue += amount
                        self.total_cost += total_cost
                        self.total_profit += profit
                        self.units_sold += quantity
                        
                    except ValueError as ve:
                        print(f"Warning: Skipping row {row_idx} due to parsing error: {ve}")
                        continue
                        
            return len(self.data) > 0
            
        except Exception as e:
            print(f"Error reading CSV file: {e}")
            return False

    def get_summary_metrics(self) -> Dict[str, Any]:
        """Calculates global summary metrics."""
        average_margin = (self.total_profit / self.total_revenue * 100) if self.total_revenue > 0 else 0.0
        avg_order_val = (self.total_revenue / len(self.data)) if self.data else 0.0
        
        return {
            "total_transactions": len(self.data),
            "total_revenue": self.total_revenue,
            "total_cost": self.total_cost,
            "total_profit": self.total_profit,
            "total_units_sold": self.units_sold,
            "average_profit_margin_pct": average_margin,
            "average_order_value": avg_order_val
        }

    def get_category_performance(self) -> Dict[str, Dict[str, float]]:
        """Aggregates revenue, profit, and quantity sold by category."""
        category_stats = defaultdict(lambda: {"revenue": 0.0, "profit": 0.0, "quantity": 0})
        
        for item in self.data:
            cat = item['category']
            category_stats[cat]["revenue"] += item['amount']
            category_stats[cat]["profit"] += item['profit']
            category_stats[cat]["quantity"] += item['quantity']
            
        return dict(category_stats)

    def get_top_products(self, metric: str = 'amount', top_n: int = 3) -> List[Tuple[str, float]]:
        """Identifies the top N products by either 'amount' (revenue), 'profit', or 'quantity'."""
        product_totals = defaultdict(float)
        
        for item in self.data:
            prod = item['product']
            product_totals[prod] += item[metric]
            
        sorted_products = sorted(product_totals.items(), key=lambda x: x[1], reverse=True)
        return sorted_products[:top_n]

    def get_monthly_trends(self) -> List[Tuple[str, float]]:
        """Calculates monthly revenue trends."""
        monthly_revenue = defaultdict(float)
        
        for item in self.data:
            month_key = item['date'].strftime('%Y-%m')  # Format: YYYY-MM
            monthly_revenue[month_key] += item['amount']
            
        return sorted(monthly_revenue.items())

    def generate_report_string(self) -> str:
        """Generates a formatted text-based report dashboard."""
        metrics = self.get_summary_metrics()
        category_perf = self.get_category_performance()
        top_rev_products = self.get_top_products(metric='amount', top_n=3)
        top_qty_products = self.get_top_products(metric='quantity', top_n=3)
        monthly_trends = self.get_monthly_trends()
        
        report = []
        report.append("=" * 60)
        report.append("                    SALES PERFORMANCE REPORT                    ")
        report.append("=" * 60)
        report.append(f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        report.append(f"Data source: {os.path.basename(self.file_path)}")
        report.append("-" * 60)
        
        # 1. Summary Metrics
        report.append("\n[1] KEY PERFORMANCE INDICATORS")
        report.append(f"  - Total Transactions:  {metrics['total_transactions']:,}")
        report.append(f"  - Total Units Sold:    {metrics['total_units_sold']:,}")
        report.append(f"  - Total Revenue:       ${metrics['total_revenue']:,.2f}")
        report.append(f"  - Total Net Profit:    ${metrics['total_profit']:,.2f}")
        report.append(f"  - Average Order Value: ${metrics['average_order_value']:,.2f}")
        report.append(f"  - Profit Margin:       {metrics['average_profit_margin_pct']:.2f}%")
        report.append("-" * 60)
        
        # 2. Category Performance Table
        report.append("\n[2] PERFORMANCE BY PRODUCT CATEGORY")
        report.append(f"  { 'Category':<20} | {'Qty':>5} | {'Revenue':>12} | {'Profit':>12}")
        report.append("  " + "-" * 54)
        for cat, stats in sorted(category_perf.items(), key=lambda x: x[1]['revenue'], reverse=True):
            report.append(f"  {cat:<20} | {stats['quantity']:>5} | ${stats['revenue']:>11,.2f} | ${stats['profit']:>11,.2f}")
        report.append("-" * 60)
        
        # 3. Top Products
        report.append("\n[3] TOP PERFORMING PRODUCTS (Revenue)")
        for idx, (prod, val) in enumerate(top_rev_products, 1):
            report.append(f"  {idx}. {prod:<30} | ${val:,.2f}")
            
        report.append("\n[4] TOP PERFORMING PRODUCTS (Volume / Quantity)")
        for idx, (prod, val) in enumerate(top_qty_products, 1):
            report.append(f"  {idx}. {prod:<30} | {int(val):,} units")
        report.append("-" * 60)
        
        # 4. Monthly Trend
        report.append("\n[5] MONTHLY REVENUE TRENDS")
        report.append(f"  {'Month':<10} | {'Monthly Revenue':>15} | {'Visual Trend (Scaled)'}")
        report.append("  " + "-" * 54)
        max_rev = max([val for _, val in monthly_trends]) if monthly_trends else 1.0
        for month, rev in monthly_trends:
            bar_len = int((rev / max_rev) * 20) if max_rev > 0 else 0
            bar = "#" * bar_len
            report.append(f"  {month:<10} | ${rev:>14,.2f} | {bar}")
        report.append("=" * 60)
        
        return "\n".join(report)

def main():
    csv_file = "sales_data.csv"
    analyzer = SalesAnalyzer(csv_file)
    
    print("Initializing Sales Data Analyzer...")
    if not analyzer.load_data():
        print("Failed to initialize. Exiting.")
        return
        
    report = analyzer.generate_report_string()
    
    # Print to console
    print(report)
    
    # Save to a text report file
    report_filename = "sales_report.txt"
    try:
        with open(report_filename, "w", encoding="utf-8") as f:
            f.write(report)
        print(f"\n[Success] Report saved successfully to '{report_filename}'")
    except Exception as e:
        print(f"Error saving report to file: {e}")

if __name__ == "__main__":
    main()
