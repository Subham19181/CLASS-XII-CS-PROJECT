#Program 6

ch = input("Enter any character: ")
up_char = 0
num_char = 0
low_char = 0
if (ch>= '0' and ch<= '9'):
    num_char = num_char +1
elif (ch>= 'a' and ch<= 'z'):
    low_char = low_char+1
elif (ch>= 'A' and ch<= 'Z'):
    up_char = up_char+1
while (ch!= '*'):
    ch = input("Enter any character: ")
    if (ch>= 'a' and ch<= 'z'):
        low_char = low_char+1
    elif (ch== 'A' and ch<= 'Z'):
        up_char = up_char+1
    elif (ch>= '0' and ch<= '9'):
        num_char = num_char+1
print ("Number of uppercase characters are: ", up_char)
print ("Number of lowercase characters are: ", low_char)
print ("Number of numerals are: ", num_char)