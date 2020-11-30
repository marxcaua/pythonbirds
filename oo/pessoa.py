class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome=None, idade=17):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':
    marx = Pessoa(nome='marx')
    carlos = Pessoa(marx, nome='carlos')
    print(Pessoa.cumprimentar(carlos))
    print(id(carlos))
    print(carlos.cumprimentar())
    print(carlos.nome)
    print(carlos.idade)
    for filho in carlos.filhos:
        print(filho.nome)
    carlos.sobrenome ='alberto'
    del carlos.filhos
    carlos.olhos= 1
    del carlos.olhos
    print(carlos.__dict__)
    print(marx.__dict__)
    Pessoa.olhos=3
    print(Pessoa.olhos)
    print(carlos.olhos)
    print(marx.olhos)
    print(id(Pessoa.olhos), id(carlos.olhos), id(marx.olhos))

