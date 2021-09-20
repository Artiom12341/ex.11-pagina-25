# REZOLVĂ! De la tastatură se citesc elementele unui tablou unidimensional,
#format din n numere întregi, n<10. Elaboraţi un program care:
n=int(input("Dati numarul de elemente din tablou intre 5 si 10 ="))
y=[]
if ((n <10) and (n>=5)):
    for i in range (0,n):
        z=int(input("Dati elementele ="))
        y.append(z)
else:
    print("Respecta conditia!")
print(y)
print("a)	 afişează pe ecran componentele tabloului la un interval de 5 poziţii")
for i in range(0,5):
    print(y[i])
print("b)	 afişează pe ecran numerele în ordinea inversă a introducerii în calculator")
b=y.copy()
print(b[::-1])
print("c)	 sortează componentele tabloului în ordine descrescătoare")
c=y.copy()
c.sort(reverse=True)
print(c)
print("d)	 afişează pe ecran doar componentele pare")
d=y.copy()
for i in range(0,n):
    if d[i]%2==0:
        print(d[i])
print("e)	 afişează pe ecran media aritmetică a componentelor pare")
e=y
s=[]
r=0
for i in range(0,n):
    if e[i]%2==0:
        s.append(e[i])
        r=r+1
print(int(sum(s))/r)
print("f)	 afişează pe ecran doar componentele impare")
f=y.copy()
for i in range(0,n):
    if f[i]%2==1:
        print(f[i])
print("""g)	 afişează pe ecran doar componentele care sunt mai mari ca x şi nu sunt
divizibile cu y (valorile x şi y se citesc de la tastatură)""")
g=y.copy()
x=int(input("dati x="))
z=int(input("Dati z="))
for i in range(0,n):
    if ((x<g[i]) and (g[i]%z!=0)):
        print(g[i])
    else:
        continue
print(" ")
print("""h)	 afişează pe ecran doar componentele care sunt mai mari ca x şi mai mici
decât y (valorile x şi y se citesc de la tastatură)""")
h=y.copy()
w=int(input("dati w="))
q=int(input("Dati q="))
adevar=True
for i in range(0,n):
    if ((w<h[i]) and (h[i]<q)):
        print(h[i])
    else:
        continue
        adevar=False
print(" ")
if adevar==False:
    print("Astfel de componente nu sunt.")
print("i)	 afişează pe ecran poziţiile (indicii) componentelor impare negative")
v=y.copy()
for i in range(0,n):
    if ((v[i]%2==1) and (v[i]<0)):
        print(v.index(v[i]))
print("""j)	 afişează pe ecran poziţiile (indicii) componentelor ce conţin doar două cifre
semnificative""")
j=y.copy()
for i in range(0,n):
    if ((j[i]//10>=1) and (j[i]//100<1) or (j[i]//10<=-1) and (j[i]//100>-1)):
        print(j[i])
print("""k)	 înlocuieşte prima componentă a tabloului cu componenta de valoare minimă
din tabloul respectiv""")
k=y.copy()
k[0]=min(k)
print(k)
print("""l)	 înlocuieşte componenta de valoare minimă din tabloul respectiv cu prima
componentă a acestuia;""")
l=y.copy()
for i in range(0,n):
    l.insert(l.index(min(l)),l[0])
    l.pop(l.index(min(l)))
print(l)
print("""m)	creează un tablou nou, format doar din componentele pare ale tabloului
introdus de la tastatură""")
m=[]
a=y.copy()
for i in range(0,n):
    if a[i]%2==0:
        m.append(a[i])
print(m)
print("""n)	 creează un tablou nou, format doar din componentele divizibile cu 3 ale
tabloului introdus de la tastatură""")
nr=[]
t=y.copy()
for i in range(0,n):
    if t[i]%3==0:
        nr.append(t[i])
print(nr)
print("o)	 creează un tablou nou, format doar din acele componente ale tabloului introdus de la tastatură care au cel mult patru divizori.")