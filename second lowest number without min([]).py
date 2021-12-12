small=smaller=0
limit=int(input('Enter the number of terms:'))
for i in range(limit):
    n=int(input('Enter number:'))
    if i==0 :
        small = n
    elif i==1 :
        if n <= small :
            smaller= n
        else :
            smaller = small
            small = n
    else :
        if n < smaller :
            small = smaller
            smaller = n
        elif n < small :
            small = n
print('The lowest number is : ',smaller)
print('The second lowest number is : ',small)
