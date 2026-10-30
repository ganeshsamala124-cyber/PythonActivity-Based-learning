
# Examination Result System

n = int(input("Enter Number of Subjects: "))

total = 0
failed = 0

for i in range(n):
    print("\nSubject", i + 1)

    marks = float(input("Enter Marks: "))

    # Grace Marks
    if marks >= 33 and marks < 35:
        marks = min(marks + 2, 100)

    print("Final Marks:", marks)

    total += marks

    if marks < 35:
        failed += 1

# Calculate Percentage
percentage = total / n

# Final Classification
print("\n--- EXAM RESULT ---")
print("Total Marks:", total)
print("Percentage:", percentage)

if failed > 0:
    print("Result: FAIL")
elif percentage >= 75:
    print("Class: DISTINCTION")
elif percentage >= 60:
    print("Class: FIRST CLASS")
elif percentage >= 50:
    print("Class: SECOND CLASS")
else:
    print("Class: THIRD CLASS")
