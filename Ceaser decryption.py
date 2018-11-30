import string
arr=string.ascii_letters

pli=input("please enter Decryption message :")
key =0
while key <= 26:
    iqe = ""
    for item in pli:
        if item.isalpha():
            iqe+=arr[(arr.index(item)-int(key))%26]
        else :
            iqe+=item
    print(iqe)
    key = key +1
