s = 'caldo'
vogais = ['a','e','i','o','u']
l = list(s)

i=0
while i<len(l):
    if i==len(l)-1:
        if l[i]=='l' and l[i-1] in vogais:
            l[i] = '8'
    else:
        if l[i]=='l' and l[i-1] in vogais and l[i+1] not in vogais:
            l[i] = '8'
            
    if i==len(l)-1:
        if l[i]=='u' and l[i-1] in vogais:
            l[i] = '8'
    else:
        if l[i]=='u' and l[i-1] in vogais and l[i+1] not in vogais:
            l[i] = '8'            
    i+=1

r = "".join(l)
print(r)