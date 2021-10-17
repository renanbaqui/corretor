#print("Regra 7")

s = 'queiju'

l = list(s)

if l[len(s)-1]=='o' or l[len(s)-1]=='u':
    l[len(s)-1] = '7'
    print("Regra 7-1")
    
elif l[len(s)-2]=='o' and l[len(s)-1]=='s' or l[len(s)-2]=='u' and l[len(s)-1]=='s':
    l[len(s)-2] = '7'
    print("Regra 7-2")    
    

r = "".join(l)
print(r)