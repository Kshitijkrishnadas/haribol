x=0
n=int(input("Enter a number : "))
temp=n
while temp!=0:
    x=x*10+temp%10
    temp//=10
print("The reverse of", n, "is", x)
if x==n:
    print(n, "is a palindrome.")
else:
    print(n, "is not a palindrome.")
