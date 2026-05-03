print ("Hello and Good day!, Welcome to our grading system for PSHS students.")

def get_equivalent_and_adjective(grade):
    if grade >= 96:
        return 1.00, "EXCELLENT"
    elif grade >= 90:
        return 1.25, "VERY GOOD"
    elif grade >= 84:
        return 1.50, "VERY GOOD"
    elif grade >= 78:
        return 1.75, "GOOD"
    elif grade >= 72:
        return 2.00, "GOOD"
    elif grade >= 66:
        return 2.25, "SATISFACTORY"
    elif grade >= 60:
        return 2.50, "SATISFACTORY"
    elif grade >= 55:
        return 2.75, "FAIR"
    elif grade >= 50:
        return 3.00, "FAIR"
    elif grade >= 40:
        return 4.00, "FAILED ON CONDITION"
    else:
        return 5.00, "FAILED"

def compute_tentative():
    ww = float(input("WW: "))
    pt = float(input("PT: "))
    qa = float(input("QA: "))
    return (ww * 0.30) + (pt * 0.50) + (qa * 0.20)

print("=== PSHS Grade Calculator ===")

# Q1
print("\nEnter Q1 scores:")
q1 = compute_tentative()

# Q2
print("\nEnter Q2 scores:")
tq2 = compute_tentative()
q2 = (q1 + 2 * tq2) / 3

# Q3
print("\nEnter Q3 scores:")
tq3 = compute_tentative()
q3 = (q2 + 2 * tq3) / 3

# Q4
print("\nEnter Q4 scores:")
tq4 = compute_tentative()
q4 = (q3 + 2 * tq4) / 3

# Final Output
equivalent, adjective = get_equivalent_and_adjective(q4)

print("\n=== RESULTS ===")
print("Q1:", round(q1, 2))
print("Q2:", round(q2, 2))
print("Q3:", round(q3, 2))
print("Final Grade (Q4):", round(q4, 2))
print("Equivalent:", equivalent)
print("Adjectival Equivalent:", adjective)
