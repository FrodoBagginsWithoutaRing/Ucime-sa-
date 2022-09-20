a=float(input("Zadaj stranu a trojuholnika "))
b=float(input("Zadaj stranu b trojuholnika "))
c=float(input("Zadaj stranu c trojuholnika "))
if a + b > c and a + c > b and c + b > a:
    if a == b or a==c or c==b:
        print("Tvoj trojuholnik je rovnoramenny")
        if a==b==c:
            print("Tvoj trojuholnik je rovnostranny.")
    if a**2+b**2 == c**2 or b**2+c**2 == a**2 or a**2+c**2 == b**2:
        print("Tvoj trojuholnik je pravouhly.")
else:
    print("Tvoj trojuholnik nie je trojuholnik jelito.")
