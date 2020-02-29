class Cliente:

    def __init__(self,cod_cliente,nome,telefone):
        self.cod_cliente = cod_cliente
        self.nome = nome
        self.telefone = telefone

class Cliente_Registrado_Online(Cliente):

    def __init__(self,cod_cliente,nome,telefone,email,senha):
        super().__init__(cod_cliente,nome,telefone)
        self.email = email
        self.senha = senha

class Animal:

    def __init__(self,cod_animal,nome,especie,dat_nascimento,cliente):
        self.cod_animal = cod_animal 
        self.nome = nome
        self.especie = especie
        self.dat_nascimento = dat_nascimento
        self.cliente = cliente

class Produto:

    def __init__(self,cod_produto,nome,preco):
        self.cod_produto = cod_produto
        self.nome = nome
        self.preco = preco

if __name__ == "__main__":

    cliente1=Cliente(1, "Tiago", 76453534523)
    cliente2=Cliente_Registrado_Online(200, "Tiago Chato", 6476565765, "jdhfjhjfghjkh@gmail.com", "476576")
    animal=Animal(1, "Lady", "cachorro", "05/01/2010", cliente2)
    produto=Produto(1, "Shampoo", 30)

    print(cliente1.nome, cliente1.cod_cliente, cliente1.telefone)
    print(cliente2.nome, cliente2.cod_cliente, cliente2.telefone, cliente2.email, cliente2.senha)
    print(produto.nome, produto.cod_produto, produto.preco)
    print(animal.nome, animal.cod_animal, animal.especie, animal.dat_nascimento, animal.cliente.nome)
    