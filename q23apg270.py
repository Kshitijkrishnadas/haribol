x=int(input())
a=sm=0.0
fact=temp=1
for i in range(1,7):
    fact*=i
    a=(-1)**(i+1)
    temp*=x
    sm+= (a*temp)/fact
print(sm)
