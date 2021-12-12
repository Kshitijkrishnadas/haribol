lst0=[]
lst1=eval(input("Enter a list:"))
for a in lst1:
    if a==0:
        lst0.insert(0,a)
    else:
        lst0.append(a)
print("The modified list is",lst0)
