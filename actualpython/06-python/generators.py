daily_sales=[100, 200, 150, 300, 250]
def calculate_total_sales(sales):
    total=0
    for sale in sales:
        total+=sale
    return total

total_sales = calculate_total_sales(daily_sales)
print(total_sales)

# with generator expression
total_sales = sum(sale for sale in daily_sales)
print(total_sales)

# generator expression to calculate total sales with a condition
# generator expression is memory efficient way to create iterators in Python. It allows you to generate values on the fly without storing the entire sequence in memory at once.
total_sales = sum(sale for sale in daily_sales if sale > 150)
print(total_sales)