conceito = ""
m = 0
def media(a, b):
    m = (a + b)/2
    if m <= 4.9:
        conceito = "D"
    elif m <= 6.9:
        conceito = "C"
    elif m <= 8.9:
        conceito = "B"
    elif m <= 10:
        conceito = "A"
        print(f"Sua media é {m} e você está no conceito {conceito}")



media(a=int(input('Nota 1: ')), b=int(input('Nota 1: ')))




