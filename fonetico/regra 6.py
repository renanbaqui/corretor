s = 'incontinentis'

l = list(s)

if l[len(s)-1]=='e' or l[len(s)-1]=='i':
    l[len(s)-1] = '6'
    print("Regra 6-1")
    
elif l[len(s)-2]=='e' and l[len(s)-1]=='s' or l[len(s)-2]=='i' and l[len(s)-1]=='s':
    l[len(s)-2] = '6'
    print("Regra 6-2")    
    

r = "".join(l)
print(r)