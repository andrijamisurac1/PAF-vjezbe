x1,y1=(input("Unesite koordinate prve tocke: ")).split(",")
x2,y2=(input("Unesite koordinate druge tocke: ")).split(",")

k=(float(y2)-float(y1))/(float(x2)-float(x1))
b=float(y1)-k*float(x1)

print("f(x) =", k, "* x +", b)