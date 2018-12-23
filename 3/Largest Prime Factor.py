"""

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

"""

def asalmı(sayı):
    bölen=2
    while bölen<sayı:
        if sayı%bölen==0:
            return False
        elif sayı==1:
            return False
        elif sayı==2:
            return True
        elif sayı<=0:
            return False
        bölen+=1


    return True
liste=list()
bölen=2
sayı=600851475143
while bölen<sayı:
    if sayı%bölen==0 and asalmı(bölen):
        print(bölen)
        bölen+=1
    else:bölen+=1