def fact(i):
    if i<0:
        raise ValueError
    elif i==0 or i==1:
        return i
    else:
        return i*fact(i-1)
print(fact(5))
