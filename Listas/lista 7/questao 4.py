def data(a, b, c):
    if 0 < c <= 2022:
        if b in (1, 3, 5, 7, 8, 10, 12):
            if a > 0 < 31:
                if b >= 10:
                    print(f"Data valida, data dita foi {a}/{b}/{c}")
                else:
                    print(f"Data valida, data dita foi {a}/0{b}/{c}")
    else:
        if b >= 10:
            print(f"Data invalida, data dita foi {a}/{b}/{c}")
        else:
            print(f"Data invalida, data dita foi {a}/0{b}/{c}")

data(a=int(input("Dia: ")), b=int(input("Mes: ")), c=int(input("Ano: ")))
