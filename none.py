strng='jjfhfioGJHGKHGggu'
nws=''
for a in strng:
    if a.islower():
            a=a.upper()
    elif a.isupper():
            a=a.lower()
    nws+=a
    print(nws)
