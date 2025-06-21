s=input()

L1=list(s)
odd=[]
upp=[]
low=[]
even=[]
for x in L1:
    if x in "13579":
        odd.append(x)
    elif x in "02468":
        even.append(x)
    elif x.isupper():
        upp.append(x)
    else:
        low.append(x)

s1="".join(sorted(odd))
s2="".join(sorted(upp))
s3="".join(sorted(low))
s4="".join(sorted(even))
print(s3+s2+s1+s4)





