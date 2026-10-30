
# Hospital Billing System

name = input("Enter Patient Name: ")

consultation = float(input("Enter Consultation Charges: "))
diagnostic = float(input("Enter Diagnostic Charges: "))
treatment = float(input("Enter Treatment Charges: "))

# Calculate Total Bill
total = consultation + diagnostic + treatment

# Apply Concession
if total >= 10000:
    concession = total * 0.10
elif total >= 5000:
    concession = total * 0.05
else:
    concession = 0

# Final Bill
bill = total - concession

# Patient Classification
if bill >= 10000:
    category = "High Payment"
elif bill >= 5000:
    category = "Medium Payment"
else:
    category = "Low Payment"

# Display Bill
print("\n--- HOSPITAL BILL ---")
print("Patient Name:", name)
print("Total Charges:", total)
print("Concession:", concession)
print("Final Bill:", bill)
print("Patient Category:", category)
