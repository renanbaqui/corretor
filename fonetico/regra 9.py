s = 'tenrro'
vogais = ['a','e','i','o','u']
l = list(s)

i=1

while i<len(l)-1:
    if l[i]=='r' and l[i+1] in vogais:
        print("Regra 9-1")
    if l[i]=='r' and l[i+1]=='r':
        print("Regra 9-2")
    i+=1
    
r = "".join(l)
print(r)
