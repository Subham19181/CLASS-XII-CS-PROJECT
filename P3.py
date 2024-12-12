
#Program 3

import pickle

stu = {}
found = False
fin = open('Stu.dat', 'rb+')
try:
    while True:
        rpos = fin.tell()
        stu = pickle.load(fin)
        if stu['Marks']>81:
            stu['Marks']+=2
            fin.seek(rpos)
            pickle.dump(stu, fin)
            found = True
except EOFError:
    if found == False:
        print("Sorry, no matching rerord found.")
    else:
        print("Record(s) succesfully updated.")
    fin.close()