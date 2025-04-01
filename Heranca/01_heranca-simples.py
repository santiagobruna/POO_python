class Veiculo:
    def __init__(self, cor, placa, numero_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas

    def liga_motor(self):
        return("Ligando o motor")

    def __str__(self):
        return f'Cor: {self.cor} | Placa: {self.placa}  | QtdRodas: {self.numero_rodas}'

class Motocicleta(Veiculo):
    pass
class Caminhao(Veiculo):
    def __init__(self, cor, placa, numero_rodas, carregado): # iniciando um novo construtor adicionando um novo atributo
        super().__init__(cor, placa, numero_rodas) # chama o construtor da classe Pai(somente)
        self.carregado = carregado # Novo atributo exclusivo da classe Caminhao
    def esta_carregado(self):
        return "Está carregado" if self.carregado else "Não está carregado"
    def __str__(self):
        return f"{super().__str__()} | {'Carregado' if self.carregado else 'Não carregado'}"
class Carro(Veiculo):
    pass

# moto = Motocicleta('roxo', '123fr', 2)
# print(moto)
# print(moto.liga_motor())

# carro = Carro('branco', '2345f', 4)
# print(carro)
# print(carro.liga_motor())

caminhao = Caminhao('preto', '5345fb', 6, True)
print(caminhao)
print(caminhao.liga_motor())
print(caminhao.esta_carregado()) 