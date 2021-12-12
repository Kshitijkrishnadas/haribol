myfile = open(r"c:\pyjunk\file.txt")
content = myfile.read()
myfile.close()
vowel = lower = upper = blank = 0
for char in content:
    if char in "AEIOUaeiou":
        vowel += 1
    if char.isupper():
        upper += 1
    if char.islower():
        lower += 1
    if char == " " :
        blank += 1
print("No. of upper case:", upper)
print("No. of lower case:", lower)
print("No. of vowels:", vowel)
print("No. of blank spaces:", blank)
