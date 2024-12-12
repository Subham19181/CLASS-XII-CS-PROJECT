#progrm 7

country = ["Brazil", "India", "China", "Russia", "Sri Lanka"]
is_member = input("Enter the name of country : ")
if is_member in country:
    print(is_member, "has also joined BRICS")
else:
    print(is_member, " is not a member of BRICS")