"""If the numbers 1 to 5 are written out in words: 
one, two, three, four, five, then there are 
3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) 
inclusive were written out in words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 
342 (three hundred and forty-two) contains 23 letters and
115 (one hundred and fifteen) contains 20 letters. 
The use of "and" when writing out numbers is in 
compliance with British usage.
"""

birler=["","one","two","three","four","five","six","seven","eight","nine"]
onlar=["","ten","twenty","thirty","fourty","fifty","sixty","seventy","eighty","ninety"]
özel={11:"eleven",12:"twelve",13:"thirteen",14:"fourteen",15:"fifteen",16:"sixteen",17:"seventeen",18:"eighteen",19:"nineteen"}
yüzler=["","onehundred","twohundred","threehundred","fourhundred","fivehundred","sixhundred","sevenhundred","eighthundred","ninehundred"]

def read(number):
    if(number==1000):
        return "onethousand"
    if(len(str(number))==1):
        return birler[number]
    
    if (number>10 and number<20):
        return özel.get(number)
    
    if(len(str(number))==2):
        reading=""
        reading+=onlar[int((str(number))[0])]
        reading+=birler[int((str(number))[1])]
        return reading
    
    if(len(str(number))==3):
        reading=""
        if(str(number)[1::]=="00"):
            return yüzler[int(str(number)[0])]
        
        reading+=yüzler[int(str(number)[0])]
        reading+="and"
        if(int(str(number)[1::])<20 and int(str(number)[1::])>10):
            reading+=özel.get(int(str(number)[1::]))
            return reading
        
        reading+=onlar[int(str(number)[1])]
        reading+=birler[int(str(number)[-1])]
        return reading

result=0

for i in range(1,1001):
    result+=len(read(i))
print(result)