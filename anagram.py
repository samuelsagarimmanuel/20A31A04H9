# write a program to check wheather the given input is satisfing the condition of anagram
#input1:yaswanth
#input2:silent
#output:true

a="yaswanth"
b="listen"
n=len(a)
m=len(b)
sorta=sorted(a)
sortb=sorted(b)
if n==m:
    if sorta==sortb:
        print("anagram")
    else:
        print("not a anagram")
else:
    print("not is not matching")