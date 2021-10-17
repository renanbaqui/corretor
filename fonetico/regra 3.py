#print("Regra 3")
s = 'faxina'

l = list(s)

vogais = ['a','e','i','o','u',]

i=0
ultima = s[i]

for letra in l[1:]:
    if ultima == 'x' and letra in vogais:
        l[i]='3'
    i+=1
    ultima = s[i]
    

r = "".join(l)
print(r)