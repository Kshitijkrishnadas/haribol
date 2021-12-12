def fun(lim):
    for i in range(2,lim+1):
        for j in range(2,i+1):
            if i!=j and i%j==0:
                break
            elif j==i:
                print(i)
fun(10)
