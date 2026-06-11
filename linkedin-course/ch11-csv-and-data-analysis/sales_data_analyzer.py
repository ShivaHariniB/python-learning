import csv
import json

with open("sales.csv", "r") as file:
    order_data = csv.DictReader(file)

    row_count = 0
    total_revenue = 0
    category_wise_revenue = {}
    units_sold = {}
    customer_leaderboard = {}
    for row in order_data:
        row_count += 1
        total_revenue += int(row["quantity"]) * int(row["price"])
# category wise revenue
        categories = row["category"]
        category_wise_revenue[categories] = category_wise_revenue.get(
            categories, 0) + (int(row["price"])*int(row["quantity"]))
# product wise category
        units = row["product"]
        units_sold[units] = units_sold.get(units, 0)+int(row["quantity"])
# customer dict based on revenue
        customer = row["customer"]
        customer_leaderboard[customer] = customer_leaderboard.get(
            customer, 0)+(int(row["price"])*int(row["quantity"]))


print(row_count)
highest_selling_product = max(units_sold, key=units_sold.get)

with open("report.txt", "w") as file:
    file.write(f"Total revenue: {total_revenue}\n\n")
    file.write(f"Category wise revenue:\n")
    file.write("---------------------\n")
    json.dump(category_wise_revenue, file, indent=4)
    file.write(f"\n\nHighest selling product: {highest_selling_product}\n\n")

# customer list sorted in desc of revenue ,
# enumerate is used to display it in table like format, without enumerate result will be displayed in tuples
top_customer_leaderboard = sorted(
    customer_leaderboard.items(), key=lambda item: item[1], reverse=True)
with open("report.txt", "a") as file:
    file.write("Top customer LeaderBoard\n")
    file.write("---------------------\n")
    for rank, (customer, revenue) in enumerate(top_customer_leaderboard, start=1):
        file.write(f"{rank}.{customer} - {revenue}\n")
