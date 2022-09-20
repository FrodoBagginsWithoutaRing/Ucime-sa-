a=int (input("Zadaj začiatok intervalu: "))
b=int (input("Zadaj koniec intervalu: "))
c=float (input("Zadaj čislo ktore chces zistit či patrí do intervalu: "))
l = list(range(a, b,1 ))
if c in l:
    print("tvoje čislo je súčasťou intervalu")
else:
    print("tvoje čislo nie je sučasťou intervalu")
