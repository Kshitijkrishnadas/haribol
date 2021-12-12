def fun(a):
    sm=0
    for i in range(1,a):
        if a%i==0:
            sm+=i
    if sm==a:
        return True
    else:
        return False
print(fun(6))
