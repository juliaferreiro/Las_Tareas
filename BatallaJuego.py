import random

from Creatures import Personaje, Bruja, Guerrero, Orco


#Metodo recibir daño, le saca el daño a la vida y le dice cuanto tiene, lo comenté porque me funciona mal
def jugar_batalla(personajeA, personajeB):
    while personajeA.vida > 0 and personajeB.vida > 0:
        if type(personajeA) == Bruja:
            opcion = int(input("Indique que quiere hacer el primer personaje, 1 atacar, 2 defender, 3 usar pocion que te sube la vida " ))
            if opcion == 1:
                personajeA.atacar(personajeB)
            if opcion == 2:
                personajeA.defender(personajeB)
            if opcion == 3:
                personajeA.pocion()
                
                
        if type(personajeA) == Guerrero:
            opcion = int(input("Indique que quiere hacer el primer personaje, 1 atacar, 2 defender, 3 usar espinas y daniar a tu enemigo si te ataca "))
            if opcion == 1:
                personajeA.atacar(personajeB)
            if opcion == 2:
                personajeA.defender(personajeB)
            if opcion == 3:
                personajeA.espinas(personajeB)
                
                
        if type(personajeA) == Orco:
            opcion = int(input("Indique que quiere hacer el primer personaje, 1 atacar, 2 defender, 3 enojarse para aumentar tu danio "))
            if opcion == 1:
                personajeA.atacar(personajeB)
            if opcion == 2:
                personajeA.defender(personajeB)
            if opcion == 3:
                personajeA.enojarse()
                
                
        if personajeB.vida <= 0:
            print(personajeA.nombre, "ganó la batalla! :D")
            break

#Jugar batalla, mientras la vida de los personajes sea mayor a 0 el primer personaje ataca al otro con el método atacar, y si le queda 0 dice que ganó el otro
        if type(personajeB) == Bruja:
            opcion = int(input("Indique que quiere hacer el segundo personaje, 1 atacar, 2 defender, 3 usar pocion que te sube la vida "))
            if opcion == 1:
                personajeB.atacar(personajeA)
            if opcion == 2:
                personajeB.defender(personajeA)
            if opcion == 3:
                personajeB.pocion()
                
        if type(personajeB) == Guerrero:
            opcion = int(input("Indique que quiere hacer el segundo personaje, 1 atacar, 2 defender, 3 usar espinas y daniar a tu enemigo si te ataca "))
            if opcion == 1:
                personajeB.atacar(personajeA)
            if opcion == 2:
                personajeB.defender(personajeA)
            if opcion == 3:
                personajeB.espinas(personajeA)
                
        if type(personajeB) == Orco:
            opcion = int(input("Indique que quiere hacer el segundo personaje, 1 atacar, 2 defender, 3 enojarse para aumentar tu danio "))
            if opcion == 1:
                personajeB.atacar(personajeA)
            if opcion == 2:
                personajeB.defender(personajeA)
            if opcion == 3:
                personajeB.enojarse()
                
        if personajeB.vida <= 0:
            print(personajeB.nombre, "ganó la batalla! :D")
            break
#Si este sobrevive ataca el otro, y así hasta que uno queda sin vida

def main():
    personaje1 = Bruja("")
    personaje2 = Bruja("")
    nombre1 = str(input("Ingresá el nombre del primer personaje "))
    opcion = str(input("Indique el personaje con el que quiere jugar, 1 para bruja, 2 para guerrero y 3 para orco "))
    if opcion == '1':
        personaje1 = Bruja(nombre1)
    if opcion == '2':
        personaje1 = Guerrero(nombre1)
    if opcion == '3':
        personaje1 = Orco(nombre1)
    
    nombre2 = str(input("Ingresá el nombre del segundo personaje "))
    
    opcion = str(input("Indique el personaje con el que quiere jugar, 1 para bruja, 2 para guerrero y 3 para orco "))
    if opcion == '1':
        personaje2 = Bruja(nombre2)
    if opcion == '2':
        personaje2 = Guerrero(nombre2)
    if opcion == '3':
        personaje2 = Orco(nombre2)


    print("Que empiece la batalla!!!")
    jugar_batalla(personaje1, personaje2)
main()
#Llamamos al main que pregunta el nombre y llama al metodo jugar batalla con los dos personajes