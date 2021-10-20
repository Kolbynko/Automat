cena=int(input('Zadaj cenu:'))
mince={500:5,200:10,100:10,50:10,20:10,10:10,5:15,2:15,1:15,}

for minca in mince:
    pocet=int(cena/minca)
    if(pocet!=0):
        cena=cena-pocet*minca
        print(minca,pocet)
