Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:20:19) [MSC v.1925 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> f=open(r"c:\pyjunk\another1.txt")
>>> f.read()
'I wanna be alone\nAlone with you, does that make sense?\nI wanna steal your soul\n and keep you in my treasure chest.'
>>> f.close()
>>> f=open(r"c:\pyjunk\another1.txt","w")
>>> f.write("abcd efgh ijkl mnop qrst uvwx yzab")
34
>>> f.close()
>>> f=open(r"c:\pyjunk\another1.txt",'r+')
>>> f.read(4)
'abcd'
>>> f.write(" hare")
5
>>> f.flush()
>>> f.read()
''
>>> f.close()
>>> f=open(r"c:\pyjunk\another1.txt")
>>> f.read()
'abcd efgh ijkl mnop qrst uvwx yzab hare'
>>> f.close()
>>> f=open(r"c:\pyjunk\another1.txt","r+")
>>> f.write(" krsna")
6
>>> f.read(4)
'abcd'
>>> f.write(" mahamantra")
11
>>> f.read()
''
>>> f.close()
>>> f=open(r"c:\pyjunk\another1.txt",'a+')
>>> f.read(4)
''
>>> f.write(" japa")
5
>>> f..read()
SyntaxError: invalid syntax
>>> f.read()
''
>>> f.close()
>>> f=open(r"c:\pyjunk\another1.txt",'w+')
>>> f.read(4)
''
>>> "PYAPPEARSTOBEJUNK"
'PYAPPEARSTOBEJUNK'
>>> f.close()
>>> 