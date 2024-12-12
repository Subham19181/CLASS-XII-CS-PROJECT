#Program 8

import random
n_list = []
for i in range(10):
    val = random.randint(1, 100)
    n_list.append(val)
print("Original List : ", n_list)
ev_list = []
od_list = []
for i in range(len(n_list)):
    if(n_list[i] % 2 == 0):
        ev_list.append(n_list[i])
    else:
        od_list.append(n_list[i])
print("Even Numbers List = ", ev_list)
print("Odd Numbers List = ",od_list)