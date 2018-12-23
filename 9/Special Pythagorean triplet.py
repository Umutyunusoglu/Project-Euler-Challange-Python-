"""

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

"""
a=0
b=0
c=0
for i in range(1,1000):
    for k in range(1,1000):
        a=i
        b=k
        c=((a**2)+(b**2))**0.5


        if (a<b<c) and a+b+c==1000:
            print("A=",a,"B=",b,"C=",c)
            print(a*b*c)
            break