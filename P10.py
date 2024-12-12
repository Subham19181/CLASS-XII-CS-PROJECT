#Program 10

Tops = (("Subham", "XII SCIENCE", 97.8),
           ("Spandan", "XII COMMERCE", 99.0),
           ("Trishika", "XII HUMANITIES", 92.0))
for i in Tops:
    print(i)
choice = input("Do you want to edit the details?(Y/N) ")
if choice == 'y' or choice == 'Y' or choice == 'N' or choice == 'n':
    name = input("Enter name of student whose details is to be edited: ")
    n_name = input("Enter the correct name: ")
    n_course = input("Enter the correct course: ")
    n_aggr = input("Enter the correct aggregate: ")
    i = 0
    new_Tops = ()
    while i<len(Tops):
        if Tops[i][0] == name:
            new_Tops += (n_name, n_course, n_aggr)
        else:
            new_Tops += Tops[i]
        i+=1
else:
    print("exiting the program...")
for i in new_Tops:
    print(i,end=' ')