fact=1
n=int(input("enter a number:"))
for i in range (1,n+1):
    if i<0:
        print("invalid input")
        break
    fact*=i
print(fact)
