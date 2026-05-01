# Comparison Operators
age = 22
if age >= 18:
    message = "Eligible"
else:
    message = "Not Eligible"
print("Comparison message: " + message)

# Ternary Operator
age = 22
message = "Eligible" if age >= 18 else "Not Eligible"
print("Ternary operator message: ", message)

# Logical Operators
high_income = True
good_credit = True
student = False
if high_income and good_credit:
    print("Eligible for loan")
elif high_income or good_credit:
    print("Maybe eligible for loan")
elif not student:
    print("Not eligible for loan")
elif (high_income or good_credit) and not student:
    print("Not eligible for loan")
