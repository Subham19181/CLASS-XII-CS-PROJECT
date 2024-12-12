#Program 14

file = open("data.txt", "w+")
str_dat = input("Enter the string of your choice: ")
file.write(str_dat)
file.seek(0)
data = file.read()
c_vowels = 0
c_consonents = 0
for char in data:
    if char in 'aeiou':
        c_vowels += 1
    else:
        c_consonents += 1
file.close()
print("Number of vowels = ", c_vowels)
print("Number of consonents= ", c_consonents)
print("Total length of file= ", len(data))
print("Percentage of vowels in the file= ",((c_vowels)*100/len(data)),"%")
print("Percentage of consonents in the file= ",((c_consonents)*100/len(data)),"%")