n=int(input())
temp=n
print(n,'has following factors:')
for a in range(1,n+1):
    while temp%a==0:
        print(a)
        temp//=a
        if a==1:
            a+=1
