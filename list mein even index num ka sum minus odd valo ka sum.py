evesum=oddsum=0.0
lst=eval(input("Enter a list :"))
length=len(lst)
for a in range(length):
    if a%2==0:
        evesum+=lst[a]
    else:
        oddsum+=lst[a]
result=evesum-oddsum
print("The required result is", result)
