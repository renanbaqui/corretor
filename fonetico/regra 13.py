s = 'iguinição'
vogais = ['a','e','i','o','u']
l = list(s)

i=0

while i<len(l)-3:
    if l[i]=='g' and l[i+1] not in vogais:
        print("Regra 13-1")
    if l[i]=='g' and l[i+1]=='u' and l[i+2]=='i':
        print("Regra 13-2")

    i+=1
    
r = "".join(l)
print(r)
