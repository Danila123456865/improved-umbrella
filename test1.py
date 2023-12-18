a=int(input('Введите число'))
w=list(str(a))
e=len(w)
i=0 
for r in range(e):
    q=w[0]**e
    l=l+q
    i=i+1
c=list(l)
if c==w:
    print('это число армсторнга')