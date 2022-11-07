lista1 = list()
lista = list()
matriz = dict()
media = 0
GERAL = 0

def mapa():
    for n in range(0, 3):
        for l in range(0, 1):
            matriz["Nome"] = str(input('Nome: '))
            for c in range(0, 1):
                matriz["NOTA1"] = int(input('Nota 1 : '))
                matriz["NOTA2"] = int(input('Nota 2 : '))
                lista.append(matriz.copy())



def me():
    for k, v in enumerate(lista):
        print(k,f'[{v["Nome"]}], [{v["NOTA1"]}], [{v["NOTA2"]}]')
        media = (v["NOTA1"] + v["NOTA2"]) / 2
        if k == 0:
            geral = media
        else:
            if media > geral:
                geral = media
        print(media)
    print(f'A maior media dentre os alunos é {geral}')




mapa()
me()
