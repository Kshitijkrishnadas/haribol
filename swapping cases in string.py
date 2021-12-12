nwstr=''
strng=input('Enter a string:')
for a in strng:
    if a.isupper():
        a=chr(ord(a)+32)
    elif a.islower():
        a=chr(ord(a)-32)
    nwstr+=a
print('The string with swapped cases is:',nwstr)
