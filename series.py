'''import re
p=r"[aeiou]"
if re.search(p,"clue"):
 print("matchy vowel")'''
#consider the below series
#0,0,2,1,4,2,6,3,8,4,10,5,12,6,14,7,16,2,8
term=int(input("enter the term)"))
if term%2 ==0:
    term = term//2
    print(1*(term-1))
else:
    term= term//2
    print(2*(term))

    
 