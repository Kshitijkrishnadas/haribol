#SAMPLE RUNS:
#RESTART: C:\Users\GOPAL\AppData\Local\Programs\Python\Python37-32\mean median mode of a list.py 
#Enter a list :[1,4,5,8,5,8,5,8]
#The list after sorting is :
#[1, 4, 5, 5, 5, 8, 8, 8]
#Mean of the list is 5.5
#Median of the list is 5.0
#Mode of the list is (5, 8)
#>>> 
#RESTART: C:\Users\GOPAL\AppData\Local\Programs\Python\Python37-32\mean median mode of a list.py 
#Enter a list :[6,7,4,5,6,7,6,6,7,6,6]
#The list after sorting is :
#[4, 5, 6, 6, 6, 6, 6, 6, 7, 7, 7]
#Mean of the list is 6.0
#Median of the list is 6
#Mode of the list is (6)
sumnum=0
mean=median=0
mode=[]
nums=[]
freq_nums=[]
lst=eval(input("Enter a list :"))
length=len(lst)
#sorting the list in ascending order using insertion sort method:
for i in range(length):
    for j in range(i,length):
        if lst[i]>lst[j]:
            temp=lst[j]
            lst[j]=lst[i]
            lst[i]=temp
print("The list after sorting is :\n", lst)
#FOR MEAN
for m in lst:
    sumnum+=m
mean=sumnum/length
print("Mean of the list is", mean)
#FOR MEDIAN
if length%2==0:                         #checking whether the number of values are even or odd
    n=length//2
    median=(lst[n-1]+lst[n])/2
    """for 2n number of values, median=[(n)th term + (n+1)th term]/2, but we subtract 1 bcz index start from 0 and we count from 1
    so according to us the middle term is nth and n+1th term but according to indexing that term is n-1th nd nth term"""
else:
    n=(length+1)//2                           #for '2n-1' number of values, median = [{(2n-1)+1}/2]th term
    median=lst[n-1]
print("Median of the list is", median)
#FOR MODE
for a in lst:
    if a not in nums:
        nums.append(a)                        #storing unique numbers in list "nums"
        freq_nums.append(lst.count(a))        #storing frequency of unique numbers in list "freq_nums"
maxfreq=max(freq_nums)
len_freq=len(freq_nums)
for x in range(len_freq):               #loop iterating over the whole range of frequencies
    if freq_nums[x]==maxfreq:                 #if the frequency with index 'x' has same value as maximum frequency,
        mode.append(nums[x])                       #the number in the list "nums" corresponding to the same index as the index with the max. frequency is added to list "mode"
print("Mode of the list is", tuple(mode))
