# Sales Data Analyzer
# Created by Bibha Kumari

import csv

def read_data(filename):
    data = []
    with open(filename, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return data

def total_sales(data):
    total = sum(float(row['Amount']) for row in data)
    return total

def sales_by_product(data):
    product_sales = {}
    for row in data:
        product = row['Product']
        amount = float(row['Amount'])
        product_sales[product] = product_sales.get(product, 0) + amount
    return product_sales

def highest_selling_product(product_sales):
    return max(product_sales, key=product_sales.get)

def main():
    print("===== Sales Data Analyzer =====\n")
    data = read_data('sales_data.csv')

    print(f"Total Records: {len(data)}")
    print(f"Total Sales: ₹{total_sales(data):.2f}\n")

    product_sales = sales_by_product(data)
    print("----- Sales by Product -----")
    for product, amount in product_sales.items():
        print(f"{product}: ₹{amount:.2f}")

    print(f"\nTop Selling Product: {highest_selling_product(product_sales)}")
    print("\nThank you for using Sales Data Analyzer!")

main()
