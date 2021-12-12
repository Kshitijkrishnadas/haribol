lst=eval(input())
for i in range(len(lst)):
    for j in range(i+1,len(lst)):
        if lst[i]>lst[j]:
            temp=lst[j]
            lst[j]=lst[i]
            lst[i]=temp
            print(lst)
