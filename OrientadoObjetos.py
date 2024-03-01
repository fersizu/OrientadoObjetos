class equipo:
    integrante1 = ""
    integrante2 = ""
    integrante3 = ""
    def __init__(self, self_integrante1, self_integrante2, self_integrante3):
        self.integrante1 = self_integrante1
        self.integrante2 = self_integrante2
        self.integrante3 = self_integrante3

    def __str__(self):
        return f"{self.integrante1}\n{self.integrante2}\n{self.integrante3}\n"



losPolystation = equipo("Erick Fernando Siqueiros Zúñiga","Paulina Ixchel Arreguin Ruiz","")
webHeros = equipo("Jesus Manuel Arellano Merendon","Axel Felipe Reyes Valadez","Luis Daniel Delgado Enriquez")
los3Mosqueteros = equipo("Dania Denisse Benavides Figueroa","Erick Lozano Duarte","Ana Cristina Valenzuela Ruiz")
pinguinosGalacticos = equipo("Yahir Antonio Monje Ochoa","Yesica Cristina Rodriguez Renteria","")
toyotaLegacy = equipo("Israel Chacon Rojo","Dilan Mauricio Garcia Hernandez","Jesus Elias Sierra Ruizs")
losUwu = equipo("Leonardo Alberto Gonzáles Carmona","Norma Graciela Mendoza Ruiz","Jonathan Durán Mendoza")

class FS3:
    def __init__(self, equipo1, equipo2, equipo3, equipo4, equipo5, equipo6):
        self.equipo1 = equipo1
        self.equipo2 = equipo2
        self.equipo3 = equipo3
        self.equipo4 = equipo4
        self.equipo5 = equipo5
        self.equipo6 = equipo6




    def __str__(self):
        return f"{self.equipo1}\n{self.equipo2}\n{self.equipo3}\n{self.equipo4}\n{self.equipo5}\n{self.equipo6}\n"

fs3 = FS3(losPolystation, webHeros, los3Mosqueteros, pinguinosGalacticos, toyotaLegacy, losUwu)

print(fs3)


