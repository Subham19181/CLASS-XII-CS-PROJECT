#Program 13

num = int(input("Enter the numerator: "))
den = int(input("Enter the denominator: "))
try:
    q = num/den
    print("Quotient:", q)
except ZeroDivisionError:
    print("Denominator cannot be zero.")