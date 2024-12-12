#Program 5

def interest(principal, time = 2, rate = 0.10):
    return principal*rate*time

#__main__
P = float(input("Enter principal amount: "))
print("Simple interest with default ROI and time values is: ")
SI1 = interest(P)
print("Rs.", SI1)
ROI = float(input("Enter the rateof interest(ROI): "))
T = int(input("Enter the time in years: "))
print("Simple interest with your provided ROi and time values is: ")
SI2 = interest(P, T, ROI/100)
print("Rs.", SI2)