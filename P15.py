#Program 15

def GCD(x, y):
    while y != 0:
        rm = x % y
        x, y = y, rm
    return x

n = int(input("Enter the first number: "))
m = int(input("Enter the second number: "))
print("The GCD of numbers is", GCD(n, m))