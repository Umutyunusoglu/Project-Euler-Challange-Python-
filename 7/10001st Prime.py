"""

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?

"""

def asal(sayı):
    bölen=2
    while bölen<sayı:
        if sayı==2:
            return True
        if sayı%bölen==0:
            return False
        bölen+=1
    return True

def asalgenarator():
    sıra=1
    sayı=2
    while sıra<10002:
        if asal(sayı):
            sıra+=1
            yield (sayı)
        sayı+=1
for i in asalgenarator():
    print(i)