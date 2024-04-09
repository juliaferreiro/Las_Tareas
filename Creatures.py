import random

class Personaje:
    def __init__(self, nombre, vida, ataque):
        self.nombre = nombre
        self.vida = vida
        self.poder_ataque = ataque
#constructor

    def atacar(self, personajeAtacado):
        danio = random.randint(0, self.poder_ataque)
        #personajeAtacado.vida -= danio
        print(self.nombre, "atacó a" ,personajeAtacado.nombre, "y le causó ", danio, "de daño.")
        personajeAtacado.recibir_danio(danio)
        
        

#Metodo atacar, indica que el daño va a ser igual a un random, dps el personaje recibe ese daño y hace un print a la acción
    def recibir_danio(self, danio):
        self.vida -= danio
        print("A " , self.nombre, " Le queda" , self.vida)
            
    def defender (self, personaje_Atacante):
        self.vida += 0.5 * personaje_Atacante.poder_ataque
        print(self.nombre, "Se defendió del ataque")
            
class Bruja(Personaje):
    def __init__(self, nombre, vida = 130, ataque = 15):
        super().__init__ (nombre, vida, ataque)
        
    def pocion(self):
        self.vida += random.randint(10, 20)
        print(self.nombre, " se tomó una pocion y su vida aumentó a", self.vida)


class Guerrero(Personaje):
    def __init__(self, nombre, vida = 120, ataque = 20):
        super().__init__ ( nombre, vida, ataque)
        
    def espinas(self, personajeAtacante):
        personajeAtacante.vida -= 5
        print(self.nombre, " usó sus espinas y le quitó vida a su oponente")


class Orco(Personaje):
    def __init__(self, nombre, vida = 150, ataque = 10):
            super().__init__ (nombre, vida, ataque)
            
    def enojarse(self):
        self.ataque += random.randint(10, 20)
        print(self.nombre, " se enojó y su ataque aumentó a", self.ataque)
                