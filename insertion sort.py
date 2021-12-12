temp=0
list1=eval(input())
print("Original list: ", list1)
lnth=len(list1)
for i in range(1,lnth):
    key=list1[i]
    j=i-1
    while j>=0 and key<list1[j]:
        temp=list1[j+1]
        list1[j+1]=list1[j]
        list1[j]=temp
        j=j-1
print("List after sorting is", list1)
