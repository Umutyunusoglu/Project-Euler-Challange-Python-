"""

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

"""

def asalmı(sayı):
    bölen=2
    while bölen<sayı:
        if sayı%bölen==0:
            return False
        else:
            bölen+=1
    return True

def asalgenerator(limit=100):
    sayı=2
    while sayı<limit+1:
        if asalmı(sayı):
            yield sayı
        sayı+=1
toplam=0
for i in asalgenerator(2000000):
    toplam+=i
    print("Sayı=",i)
    print("Toplam=",toplam)
    print("***************")
print(toplam)