import random
palabras=[]
with open('words.txt','r') as archivo:
    for linea in archivo:
        palabras.append(linea.strip())
random.shuffle(palabras)
intentos=1
puntaje=0
for palabra in palabras:
    bueno=False
    while bueno==False:
        print(f'Puntaje: {puntaje}\nIntento {intentos}: {palabra}')
        nuevaPalabra=input("Ingrese Palabra: ")
        if nuevaPalabra!=palabra:
            print('Fallaste')
            intentos+=1
            if intentos==4:
                break
        else:
            print('Correcto')
            puntaje+=1
            break
    if intentos==4:
        print(f'Game Over\nPuntaje Final: {puntaje}')
        break