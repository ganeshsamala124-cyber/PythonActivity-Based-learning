
# Employee Payroll System

name = input("Enter Employee Name: ")

basic = float(input("Enter Basic Pay: "))
allowance = float(input("Enter Allowances: "))
overtime = float(input("Enter Overtime: "))
incentive = float(input("Enter Incentives: "))

# Gross Salary
gross = basic + allowance + overtime + incentive

# Progressive Deduction
if gross <= 10000:
    tax = gross * 0.05
elif gross <= 20000:
    tax = gross * 0.10
else:
    tax = gross * 0.15

pf = basic * 0.12
total = tax + pf

net = gross - total

# Salary Statement
print("\n--- SALARY STATEMENT ---")
print("Employee:", name)
print("Basic Pay:", basic)
print("Gross Salary:", gross)
print("Tax:", tax)
print("PF:", pf)
print("Total Deduction:", total)
print("Net Salary:", net)
