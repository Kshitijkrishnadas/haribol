a,b,c = -1,1,0
n=int(input('Enter number of terms: '))
for i in range(n):
    c=a+b
    print(c)
    a=b
    b=c
import time
time.sleep(5)
