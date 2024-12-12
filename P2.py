#Program 2

import pickle

s = {}
sfile = open('Stu.dat', 'wb')
ans = 'y'
while ans == 'y' :
    rn = int(input("Enter roll number: "))
    n = input("Enter name:")
    m = float(input("Enter marks: "))
    s['Rollno'] = rn
    s['Name'] = n
    s['Marks'] = m
    pickle.dump(s, sfile)
    ans = input("Want to enter more records? (y/n)...")
sfile.close()