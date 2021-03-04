from alphabot import *
import time
import re

def esegui_percorso(percorso):
    sec_per_grado=0.0078
    def avanti(Alphabot,val):
        ora = time.time()
        while(time.time()< ora + val):
            Alphabot.forward()
        Alphabot.stop()
        time.sleep()

    def sinistra(Alphabot,val):
        ora = time.time()
        tempo = sec_per_grado * val

        while(time.time()< ora+ tempo):
            Alphabot.left()
        Alphabot.stop()
        time.sleep()


    def destra(Alphabot,val):
        ora = time.time()
        tempo = sec_per_grado * val

        while(time.time()< ora+ tempo):
            Alphabot.right()
        Alphabot.stop()
        time.sleep()

    def indietro(Alphabot,val):
        ora = time.time()
        while(time.time()< ora + val):
            Alphabot.backward()
        Alphabot.stop()
        time.sleep()
    Pippo = Alphabot()

    # ragex-------------------------------------------


    #______numeri__________-
    lista_valori = re.split(r"\D", percorso)
    lista_valori.pop(0)
    print(f"lista numeri : {lista_valori}")

    #for l in range (0,len(lista_valori)):
    #    lista_valori[l] = int(lista_valori[l])
    
    lista_valori = [int(lista_valori[l]) for l in range(0,len(lista_valori))]


    #__________direzioni__________
    direzioni = re.split(r"\d", percorso)

    for a in range (0,2):
        c = 0
        for a in direzioni:
            if a == '':
                direzioni.pop(c)
            
            c = c + 1
    print(f"lista direzioni : {direzioni}")


    for a,val in zip(direzioni,lista_valori):
        if a == 'L':
            sinistra(Pippo,val)
        elif a == 'F':
            avanti(Pippo,val)
        elif a == 'B':
           indietro(Pippo,val)
        elif a == 'R':
            destra(Pippo,val)
        #cont = cont + 1
    



