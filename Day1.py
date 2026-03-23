# Day 1 
# Write code to:
Take 7 inputs (sales)
Store in list sales
Print the list
sales = []
for i in range(7):
    value = int(input("Enter your sales: "))
    sales.append(value)
print("Sales Data:", sales)

#Extend your code and add:
️Total sales
Average sales
️Highest sale
️Lowest sale

total_sales = sum(sales)
avg_sales = total_sales / len(sales)
highest_sales = max(sales)
lowest_sales = min(sales)

print("Total Sales:", total_sales)
print("Average Sales:", avg_sales)
print("Highest Sales:", highest_sales)
print("Lowest Sales:", lowest_sales)
