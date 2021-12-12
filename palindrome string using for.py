strng=input("Enter a string : ")
reverse=""
for a in strng:
    reverse=a+reverse
print("Reverse of", strng, "is", reverse)
if strng==reverse:
    print(strng, "is a palindrome.")
else:
    print(strng, "is not a palindrome.")
