def converse(strng,reverse=""):
    for a in strng:
        reverse=a+reverse
    return reverse
strng=input("Enter a string :")
reverse=converse(strng)
if strng==reverse:
    print(strng, "is a palindrome.")
else:
    print(strng, "is not a palindrome.")
