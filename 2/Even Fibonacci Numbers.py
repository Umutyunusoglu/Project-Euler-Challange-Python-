a,b=1,2
toplam=0
while b<4000000:
    if b%2==0:
        toplam+=b

    a,b=b,(b+a)

print(toplam)