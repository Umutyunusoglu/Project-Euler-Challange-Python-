"""

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

"""

def bul(sayı):

    değer=str(sayı)

    iki=int(değer[-1])

    üç=0
    for i in değer:
        üç+=int(i)

    dört=int(değer[-2]+değer[-1])

    beş=int(değer[-1])

    yedibir=int(değer[-1])
    yedidiğer=int(değer[0:-1])
    yedibir=yedibir*2
    yedi=yedidiğer-yedibir

    sekiz=int(değer[-3]+değer[-2]+değer[-1])

    dokuz=üç

    onbirartı=0
    onbireksi=0
    sayma=1
    for i in range(1,len(değer)+1):
        if i%2!=0:
            onbirartı+=int(değer[-i])
        else:
            onbireksi+=int(değer[-i])
    onbir=onbirartı-onbireksi

    onüçbir=int(değer[-1])
    onüçdiğer=int(değer[0:-1])
    onüçbir=onüçbir*9
    onüç=onüçdiğer-onüçbir

    onyedib=int(değer[-1])
    onyedia=(int(değer)-onyedib)/10
    onyedi=abs(onyedia-(5*onyedib))

    ondokuzb=int(değer[-1])
    ondokuza=int(değer)-ondokuzb/10
    ondokuz=abs(ondokuza+(2*ondokuzb))



    if iki%2==0 and üç%3==0 and dört%4==0 and (beş==0 or beş==5) and yedi%7==0 and (sekiz==000 or sekiz%8==0) and (dokuz==0 or dokuz%9==0) and onbir%11==0 and onüç%13==0 and (onyedi==17 or onyedi%17==0) and (ondokuz==19 or ondokuz%19==0):
        return True
    else:
        return False

sayı=100

while True:
    if bul(sayı):
        sayı*=2
        break
    else:
        sayı+=1

print(sayı)