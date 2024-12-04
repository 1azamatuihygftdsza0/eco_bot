
a=int(input("a sonini kiriting = "))
b=int(input("b sonini kiriting = "))
for i in range(b,a-1,-1):
    son.append(i)
    print(i)
print(len(son))

son=[]
a=int(input("a sonini kiriting = "))
b=int(input("b sonini kiriting = "))
for i in range(b-1,a,-1):
    son.append(i)
    print(i)
print(len(son))

k=int(input("k narxni kiriting = "))
for i in range(1,11):
    i*=k
    print(i)

k=int(input("k narxni kiriting = "))
for i in range(1,11):
    s=k*i/10
    print(s)

k=int(input("k narxni kiriting = "))
for i in range(12,21):
    s=k*i/10
    vazn=i/10
    print(f"{vazn} kg konfetning narxi {s}")
 -------------------------------------------------------------
sonlar=[]
a=int(input("a sonini kiriting = "))
b=int(input("b sonini kiriting = "))
for i in range(b,a,-1):
        sonlar.append(i)
print(sum(sonlar))
------------------------------------------------------------------------
sonlar=[]
a=int(input("a sonini kiriting = "))
b=int(input("b sonini kiriting = "))
for i in range(b,a,-1):
    sonlar.append(i)


a=int(input('a sonni kiriting: '))
b=int(input('b sonni kiriting: '))

s=1
for i in range(a,b):
    s*=i
    print(i)

print(s)








