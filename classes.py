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

# Criando um jogador
player1 = JogadorValorant('bru', '#1910')
print(player1)
player2 = JogadorValorant('exemplo', '#teste')
print(player2)

# Escolhendo Partida
player1.escolher_partida('ranked')
player2.escolher_partida('classic')