
# Mobile Plan Cost Optimization

usage = float(input("Enter Data Usage (GB): "))
validity = int(input("Enter Required Validity (Days): "))
budget = float(input("Enter Your Budget: "))

# Mobile Plans: Data, Validity, Price, Extra Charge
plans = [
    ("Plan A", 2, 28, 199, 50),
    ("Plan B", 3, 56, 299, 40),
    ("Plan C", 5, 84, 399, 30)
]

best_plan = None
min_cost = float('inf')

for name, data, days, price, extra in plans:

    excess = max(0, usage - data)
    total = price + excess * extra

    print(name, "Total Cost:", total)

    if usage <= data and validity <= days and total <= budget:
        if total < min_cost:
            min_cost = total
            best_plan = name

print("\n--- PLAN RESULT ---")

if best_plan:
    print("Best Plan:", best_plan)
    print("Minimum Cost: Rs.", min_cost)
else:
    print("No Eligible Plan Found")
