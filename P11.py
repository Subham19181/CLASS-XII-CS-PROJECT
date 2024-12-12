#Program 11

def find_ch(s, c):
    index = 0
    while(index < len(s)):
        if s[index] == c:
            print (c, "found in string at index: ", index)
            return
        else:
            pass
        index += 1
    print (c, "is not present in the string.")

str = input("Enter a string: ")
ch = input("Enter the character to be searched: ")
find_ch(str, ch)