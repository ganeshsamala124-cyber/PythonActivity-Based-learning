
# Manufacturing Cost and Profit Analysis

material = float(input("Enter Material Cost: "))
labour = float(input("Enter Labour Charges: "))
wastage = float(input("Enter Wastage Cost: "))
machine = float(input("Enter Machine Cost: "))
selling = float(input("Enter Selling Price: "))
target = float(input("Enter Profit Target: "))

# Total Production Cost
cost = material + labour + wastage + machine

# Profit Calculation
profit = selling - cost
percentage = (profit / cost) * 100

# Display Result
print("\n--- PRODUCTION REPORT ---")
print("Total Cost:", cost)
print("Selling Price:", selling)
print("Profit:", profit)
print("Profit Percentage:", percentage, "%")

if profit >= target:
    print("Target Achieved")
else:
    print("Target Not Achieved")
