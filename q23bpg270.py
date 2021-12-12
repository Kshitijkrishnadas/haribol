x=int(input('x='))
n=int(input('n='))
sm=0
for i in range(1,n+1):
    sm+=(x**i)/i
print(sm)
