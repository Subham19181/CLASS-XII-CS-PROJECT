#Program 1

def encrypt (sttr, enkey):
    return enkey.join(sttr)
def decrypt (sttr, enkey):
    return sttr.split(enkey)

#_main_
mainString = input("Enter main string :")
encryptStr = input ("Enter encryption key:")
enStr = encrypt (mainString, encryptStr)
deLst = decrypt (enStr, encryptStr)
deStr="".join(deLst)
print("The encrypted string is", enStr)
print("String after decryption is:", deStr)
