
# Campus Event Financial Planning

venue = float(input("Enter Venue Cost: "))
equipment = float(input("Enter Equipment Cost: "))
catering = float(input("Enter Catering Cost: "))
transport = float(input("Enter Transport Cost: "))
certificate = float(input("Enter Certificate Cost: "))

participants = int(input("Enter Expected Participants: "))
sponsorship = float(input("Enter Sponsorship Amount: "))
contribution = float(input("Enter Contribution Per Participant: "))

# Total Cost
total = venue + equipment + catering + transport + certificate

# Financial Calculation
income = sponsorship + (participants * contribution)
shortfall = max(0, total - income)

# Break-even Participants
remaining = max(0, total - sponsorship)

if contribution > 0:
    minimum = (remaining + contribution - 1) // contribution
else:
    minimum = 0

# Display Report
print("\n--- EVENT FINANCIAL REPORT ---")
print("Total Event Cost:", total)
print("Participant Contribution:", participants * contribution)
print("Sponsorship:", sponsorship)
print("Financial Shortfall:", shortfall)
print("Minimum Participants:", int(minimum))

if income >= total:
    print("Status: Event Budget Achieved")
else:
    print("Status: Budget Shortfall")
