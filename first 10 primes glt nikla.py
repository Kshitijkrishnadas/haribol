def prime_num(n,prime):
    while(True):
        for a in range(2,n):
            if n%a==0:
                n+=1
                prime_num(n,prime);
            else:
                print(n)
                prime.append(n)
        if len(prime)==10:
            break
n=2
prime=[]
prime_num(n,prime);
