s = 'canjica'
vogais = ['e','i']
l = list(s)

i=0
while i<len(l)-1:
    if l[i]=='g' or l[i]=='j' and l[i+1] in vogais:
        l[i] = '5'
    i+=1
    

r = "".join(l)
print(r)