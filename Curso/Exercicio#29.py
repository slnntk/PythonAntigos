km = int(input('Digite a quantos km você passou do radar: '))
multa = (km - 80) * 7
if km > 80:
    print(f'Você foi multado por que estava a {km}km/h em uma via de 80km/h e sua multa é de {multa}')