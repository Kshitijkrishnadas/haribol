numstr=''
sumnum=0
strng=input('Enter a string:')
for a in strng:
    if a.isdigit():
        numstr+=a
        sumnum+=int(a)
if sumnum==0:
    print(strng,'has no digits.')
else:
    print(strng,'has digits',numstr,'that sum to',sumnum)
