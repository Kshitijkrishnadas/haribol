v=c=0
a=input()
for i in a:
	if i.isalpha():
		if i in'AaEeIiOoUu':
			v+=1
		else:
			c+=1
print(v,c)
