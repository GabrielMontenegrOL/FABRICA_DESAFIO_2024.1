#Placa, memoria ram, placa de video
    #deixe uma class sempre dinamica, colocando os parametros dentro di __init__

class Computador:
    def __init__(self, marca, memoria_ram, placa_de_video):
        self.marca = marca 
        self.memoria_ram = memoria_ram
        self.placa_de_video = placa_de_video
   
    def Ligar(self):
        print("ESTOU LIGANDO")

    def Desligar(self):
        print("Estou desligando")

    def ExibirInfosPC(self):
        print(self.marca, self.memoria_ram, self.placa_de_video)

computador1 = Computador("Dell", "16gb", "Nvidea")
computador1.Ligar()
computador1.Desligar()
computador1.ExibirInfosPC()