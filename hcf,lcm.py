def fun(a,b):
    if a>b:
        big,small=a,b
    elif b>a:
        big,small=b,a
    for i in range(1,small+1):
        if a%i==0 and b%i==0:
            hcf=i
    j=big
    while(True):
        if j%i==0 and j%big==0:
            lcm=j
            break
        j+=1
    return hcf,lcm
print(fun(15,20))
