class Personaje:
    #atributos
    especie = "humano"
    nombre = "panchito"
    altura=2.70

    #metodos

    def correr(self,chance):
        if(chance):
            print("el personaje" + self.nombre + "esta corriendo")
        else:
            print("el personaje" + self.nombre + "se detuvo")
    
    def granada(self):
        print("el personale"+ self.nombre + "lanzo la granada")

    def recargaararlma(self,municion):
        cargador=10
        cargador= cargador+municion
        print("el arma recargada tiene " + cargador + "balas")