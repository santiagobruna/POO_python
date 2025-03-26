class JogadorValorant:
    def __init__(self, name, tagName):
        self.name = name
        self.tagName = tagName
    def escolher_partida(self, tipo_partida):
        if tipo_partida.lower() == 'ranked':
            print(f'{self.name}{self.tagName} Partida ranked encontrada!')
        elif tipo_partida.lower() == 'classic': 
            print(f'{self.name}{self.tagName} Partida clássica encontrada!')
        else: 
            print('Método não existente.')
    def __str__(self):
        return f'Jogador: {self.name} | TagName: {self.tagName}'

nome = input("Digite o nome do Jogador:")
tag = input("Digite a tag do Jogador:")

# Criando um jogador
player1 = JogadorValorant(nome, tag)
print(player1)

# Escolhendo Partida
modo = input("Escolha o modo de jogo: (ranked/classic)")
player1.escolher_partida(modo)