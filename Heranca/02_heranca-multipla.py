class Animal:
    def __init__(self, numero_patas):
        self.numero_patas = numero_patas
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"
class Ave(Animal):
    def __init__(self, cor_bico, **kw):
        self.cor_bico = cor_bico
        super().__init__(**kw)
class Mamifero(Animal):
    def __init__(self, cor_pelo, **kw):
        self.cor_pelo = cor_pelo
        super().__init__(**kw)
class Cachorro(Mamifero):
    pass

class Ornitorrinco(Mamifero, Ave):
    def __init__(self, cor_pelo, cor_bico, numero_patas):
        super().__init__(cor_pelo=cor_pelo, cor_bico=cor_bico, numero_patas=numero_patas)

cachorro = Cachorro(numero_patas=4, cor_pelo='branco')
print(cachorro)

ornitorrinco = Ornitorrinco(numero_patas=2, cor_pelo='preto', cor_bico='vermelho')
print(ornitorrinco)