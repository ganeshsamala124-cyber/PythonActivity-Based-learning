
# Travel Budget Analysis

budget = float(input("Enter Travel Budget (INR): "))
rate = float(input("Enter Exchange Rate: "))
fee = float(input("Enter Conversion Fee (%): "))

food = float(input("Enter Food Expense (Foreign Currency): "))
hotel = float(input("Enter Hotel Expense: "))
travel = float(input("Enter Transport Expense: "))
shopping = float(input("Enter Shopping Expense: "))

# Total Expenses
total = food + hotel + travel + shopping

# Currency Conversion
converted = total * rate
charges = converted * fee / 100
final = converted + charges

# Largest Expense
expenses = {
    "Food": food,
    "Hotel": hotel,
    "Transport": travel,
    "Shopping": shopping
}

largest = max(expenses, key=expenses.get)

# Display Report
print("\n--- TRAVEL BUDGET REPORT ---")
print("Total Foreign Expense:", total)
print("Converted Amount:", converted)
print("Conversion Fee:", charges)
print("Total INR Expense:", final)
print("Travel Budget:", budget)
print("Largest Expense:", largest)

if final <= budget:
    print("Budget Status: Within Budget")
else:
    print("Budget Status: Over Budget")
