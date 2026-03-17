while True:
    try:
        x = float(input("Unesite x koordinatu: "))
        break
    except ValueError:
        print("Pogrešan unos! Molimo unesite broj.")

while True:
    try:
        y = float(input("Unesite y koordinatu: "))
        break
    except ValueError:
        print("Pogrešan unos! Molimo unesite broj.")

print("f(x) =", x)

