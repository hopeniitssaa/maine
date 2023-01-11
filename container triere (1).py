v=int(input("Volumul container="))
n=int(input("Numarul de obiecte="))
obiecte={}
for i in range(n):
    pret=int(input("Pretul obiectului="))
    vol=int(input("Volumul obiectului="))
    obiecte[vol]=pret
print(obiecte)
#Gredy
x=(sorted(obiecte.items(),key=lambda item: item[1]/item[0]))[::-1]
vt=pt=0
con=[]
neinc=[]
for i in range(n):
    if vt<=v:
        if vt+x[i][0]<=v:
            con.append(x[i])
            vt+=x[i][0]
            pt+=x[i][1]
        else:
            if x[i][0]>(v-vt):
                neinc.append(x[i])
            break
print("Volumul ocupat din container=",vt,"costa=",pt)
print("Continutul containerului:")
for i in range(len(con)):
    print("In container este un obiect cu volunul=",con[i][0],"si pretul=",con[i][1])
if len(neinc)>0:
    print("Lucru care nu a incaput in container in intregime are volumul=",neinc[0][0],"si pretul=",neinc[0][1])
#Triere
x=(sorted(obiecte.items(),key=lambda item: item[1]))[::-1]
print("Lista ord-",x)
vt=0
pt=0
con=[]
def funluc(f):
    global vt
    if vt<=v:
        if vt+x[f][0]<=v:
            return True
        else:
            return False

def funpos(f):
    global vt,pt
    if funluc(f)==True:
        con.append(x[f])
        vt+=x[f][0] 
        pt+=x[f][1]
        return vt,pt, print(f"Obiectul cu pretul= {con[f][1]} si volumul= {con[f][0]} intra in container") 

for i in range(n):
    if funluc(i)==True:
        funpos(i)
print("Pretul total e",pt,"Volummul ocupat e",vt)
