class Cliente:
    def __init__(self, id=None, nome=None, sobrenome=None, desconto=None):
        self.id = id
        self.nome = nome
        self.sobrenome = sobrenome
        self.desconto = desconto

    def __str__(self):
        return (f'Id: {self.id}, Nome: {self.nome}, '
                f'Sobrenome: {self.sobrenome}, Desconto: {self.desconto}')
