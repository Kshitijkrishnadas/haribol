large=0.0
list_num=eval(input("Enter a list of numbers :"))
list_even=[]
for a in list_num:
    if a%2==0:
        list_even.append(a)
length=len(list_even)
for i in range(length):
    if i==0:
        large=list_even[i]
    else:
        if list_even[i]>large:
            large=list_even[i]
print("Largest even number is", large)
