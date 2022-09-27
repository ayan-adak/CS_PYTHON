import cmath

a = float(input('Enter First Number: '))
b = float(input('Enter Second Number: '))
c = float(input('Enter Third Number: '))

d = (b**2) - (4*a*c)


sol1 = (-b-cmath.sqrt(d))/(2*a)
sol2 = (-b+cmath.sqrt(d))/(2*a)

print ('The Solution are {0} and {1}' .format(sol1,sol2))
