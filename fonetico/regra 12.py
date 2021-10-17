s = 'cheiro'
cons = ['r','j','x']
l = list(s)

i=0

while i<len(l)-2:
    if l[i]=='e' and l[i+1]=='i' and l[i+2] in cons:
        print("Regra 12-1")
    if l[i]=='e' and l[i+1] in cons:
        print("Regra 12-2")

    i+=1
    
r = "".join(l)
print(r)
