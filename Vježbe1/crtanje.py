import matplotlib.pyplot as plt

x1,y1=(input("Unesite koordinate prve tocke: ")).split(",")
x2,y2=(input("Unesite koordinate druge tocke: ")).split(",")

k=(float(y2)-float(y1))/(float(x2)-float(x1))
b=float(y1)-k*float(x1)

print("f(x) =", k, "* x +", b)

x_values = [float(x1), float(x2)]
y_values = [float(y1), float(y2)]
plt.plot(x_values, y_values, label=f'y = {k}x + {b}')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Crtanje pravca')
plt.legend()
plt.grid(True)

print("\nOdaberite opciju:")
print("1 - Prikaži graf na ekranu")
print("2 - Spremi graf kao PDF")

opcija = input("Unesite broj opcije (1 ili 2): ")

if opcija == "1":
    plt.show()
elif opcija == "2":
    naziv = input("Unesite naziv PDF datoteke (bez .pdf nastavka): ")
    if naziv:
        plt.savefig(f"{naziv}.pdf")
        print(f"Graf je spremljen kao '{naziv}.pdf'")
    else:
        print("Naziv nije unesen!")
else:
    print("Neispravna opcija!")

