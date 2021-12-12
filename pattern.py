for i in range(1,8):
    if i<=4:
        k=i
    else:
        k=8-i
    for j in range(k):
        if j==0 or j==k-1:
            print('*',end='')
        print(' ',end='')
    print()
