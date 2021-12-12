D =0.0
a = float(input("Enter coefficient of 'x^2': "))
b = float(input("Enter coefficient of 'x': "))
c = float(input("Enter constant term: "))
D = b**2 - 4*a*c
if D < 0:
    print('Imaginary roots')
else:
    d=sqrt(D)
    alpha = ( -b + d)/2
    beeta = ( -b - d)/2
    print('Roots are', alpha, 'and', beeta )
