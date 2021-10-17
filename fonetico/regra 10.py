s = 'peneu'
vogais = ['a','e','i','o','u']
l = list(s)

i=0

while i<len(l)-2:
    if l[i]=='p' and l[i+1]=='i' and l[i+2] not in vogais:
        print("Regra 10-1")
    if l[i]=='p' and l[i+1] not in vogais:
        print("Regra 10-2")
    if l[i]=='p' and l[i+1]=='e' and l[i+2] not in vogais:        
        print("Regra 10-3")
    i+=1
    
r = "".join(l)
print(r)
