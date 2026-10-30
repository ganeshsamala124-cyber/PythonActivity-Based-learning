
# Retail Billing System

n = int(input("Enter Number of Products: "))

total = 0

for i in range(n):
    print("\nProduct", i + 1)

    name = input("Enter Product Name: ")
    price = float(input("Enter Price: "))
    qty = int(input("Enter Quantity: "))
    category = input("Enter Category (food/other): ")

    amount = price * qty

    # Category Tax
    if category.lower() == "food":
        tax = amount * 0.05
    else:
        tax = amount * 0.18

    total = total + amount + tax

    print("Product:", name)
    print("Amount:", amount)
    print("Tax:", tax)

# Discount Rules
if total >= 5000:
    discount = total * 0.15
elif total >= 2000:
    discount = total * 0.10
else:
    discount = 0

# Maximum Discount Limit
discount = min(discount, 1000)

final_bill = total - discount

# Final Invoice
print("\n--- RETAIL INVOICE ---")
print("Total Amount:", total)
print("Discount:", discount)
print("Final Bill: Rs.", final_bill)
