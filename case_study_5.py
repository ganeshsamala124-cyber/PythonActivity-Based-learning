
# Railway Fare and Reservation Calculator

n = int(input("Enter Number of Passengers: "))

total = 0

for i in range(n):
    print("\nPassenger", i + 1)

    age = int(input("Enter Age: "))
    distance = float(input("Enter Distance (KM): "))
    travel_class = input("Enter Class (Sleeper/AC): ")

    # Distance Slab Fare
    if distance <= 100:
        fare = distance * 1
    elif distance <= 500:
        fare = distance * 1.5
    else:
        fare = distance * 2

    # Travel Class
    if travel_class.lower() == "ac":
        fare = fare * 2

    # Age Concession
    if age >= 60:
        fare = fare * 0.80

    # Reservation Fee
    fare = fare + 50

    # Cancellation Penalty
    cancel = input("Cancel Ticket? (yes/no): ")

    if cancel.lower() == "yes":
        fare = fare * 0.50

    print("Passenger Fare: Rs.", fare)
    total = total + fare

print("\n--- RAILWAY BILL ---")
print("Total Amount: Rs.", total)
