from datetime import datetime, timedelta

class Cliente:
    def __init__(self, nome, e):
        self.nome = nome
        self.e = e
        self.reserva = []  # A lista de reservas (isto poderia ser útil mais tarde)

    def addReserva(self, reserva): # Adiciona uma reserva ao cliente
        self.reserva.append(reserva) # Adiciona à lista de reservas

    def listarReservaCliente(self): # Lista todas as reservas de um cliente
        if not self.reserva: # Se não houver reservas
            print(f"{self.nome} não tem reservas.") # Imprime que o cliente não tem reservas
            return # Sai da função
        print(f"Reservas de {self.nome}:") # Imprime o nome do cliente
        for i in self.reserva: # Para cada reserva na lista de reservas
            print(f"- {i.num_pessoas} pessoas no dia {i.data_reserva}, mesa {i.mesa.numMesa}") # Imprime os detalhes da reserva

class Mesa:
    def __init__(self, numMesa, capacidadeMesa):
        self.numMesa = numMesa
        self.capacidadeMesa = capacidadeMesa
        self.reservada = False # Indica se a mesa está reservada ou não

    def reservar(self): # Função para reservar uma mesa
        if self.reservada: # Se a mesa já estiver reservada
            raise Exception(f"A mesa {self.numMesa} já está reservada!") # Levanta uma exceção
        self.reservada = True # Reserva a mesa

    def libertarMesa(self): # Função para libertar uma mesa
        self.reservada = False # Define a reserva como falsa

class Reserva:
    def __init__(self, cliente, num_pessoas, data_reserva, mesa):
        self.cliente = cliente # Cliente
        self.num_pessoas = num_pessoas # Número de pessoas
        self.data_reserva = data_reserva # Data da reserva
        self.mesa = mesa # Mesa reservada

class Produto: # Produto
    def __init__(self, nomeProduto, quatiProduto):
        self.nomeProduto = nomeProduto # Nome do produto
        self.quatiProduto = quatiProduto # Quantidade do produto

    def consumoCliente(self, quantidade):
        if quantidade > self.quatiProduto: # Verifica se há quantidade suficiente
            raise Exception(f"Quantidade insuficiente de {self.nomeProduto}!") # Levanta exceção
        self.quatiProduto -= quantidade # Subtrai a quantidade consumida

class Gestor: # Classe que representa o gestor do restaurante
    def __init__(self):
        self.listaReservas = [] # Lista de reservas
        self.inventario = {} # Dicionário de inventário
        self.mesa = [Mesa(i, 4) for i in range(1, 11)] # 10 mesas de 4 pessoas

    def adicionarReserva(self, cliente, numPessoas, data): # Função para adicionar uma reserva
        mesa = self.encontrarMesa(numPessoas) # Encontra uma mesa disponível
        if not mesa: # Se não houver mesa disponível
            print("Não há mesas disponíveis.") # Informa que não há mesas
            return # Sai da função

        reserva = Reserva(cliente, numPessoas, data, mesa) # Cria uma nova reserva
        cliente.addReserva(reserva) # Adiciona a reserva ao cliente
        mesa.reservar() # Reserva a mesa
        self.listaReservas.append(reserva) # Adiciona a reserva à lista
        print(f"Reserva feita para {cliente.nome}: {numPessoas} pessoas no dia {data}, mesa {mesa.numMesa}.") # Confirma a reserva

    def encontrarMesa(self, numPessoas): # Função para encontrar uma mesa
        for i in self.mesa: # Para cada mesa
            if not i.reservada and i.capacidadeMesa >= numPessoas: # Se a mesa não estiver reservada e tiver capacidade suficiente
                return i # Retorna a mesa disponível
        return None # Se não encontrar mesa, retorna None

    def verificarReserva(self, nomeCliente): # Função para verificar reserva de cliente
        for i in self.listaReservas: # Para cada reserva na lista
            if i.cliente.nome == nomeCliente: # Se o nome do cliente corresponder
                print(f"Reserva encontrada para {nomeCliente}: {i.num_pessoas} pessoas no dia {i.data_reserva}, mesa {i.mesa.numMesa}.") # Detalhes da reserva
                return i # Retorna a reserva encontrada
        print(f"Nenhuma reserva encontrada para {nomeCliente}.") # Se não encontrar reserva, informa
        return None # Retorna None se não encontrar nada

    def cancelarReserva(self, cliente, data): # Função para cancelar reserva
        for i in self.listaReservas: # Para cada reserva
            if i.cliente == cliente and i.data_reserva == data: # Se encontrar a reserva
                i.mesa.libertarMesa() # Liberta a mesa
                self.listaReservas.remove(i) # Remove a reserva da lista
                cliente.reserva.remove(i) # Remove a reserva da lista do cliente
                print(f"Reserva de {cliente.nome} no dia {data} foi cancelada.") # Confirma o cancelamento
                return # Sai da função
        print(f"Nenhuma reserva encontrada para {cliente.nome} no dia {data}.") # Se não encontrar, informa

    def addProduto(self, nomeProduto, quantidade): # Função para adicionar produto ao inventário
        if nomeProduto in self.inventario: # Se o produto já existir
            self.inventario[nomeProduto].quatiProduto += quantidade # Atualiza a quantidade do produto
        else: # Caso contrário
            p = Produto(nomeProduto, quantidade) # Cria um novo produto
            self.inventario[nomeProduto] = p # Adiciona ao inventário
        print(f"{quantidade} unidades de {nomeProduto} adicionadas ao inventário.") # Informa o usuário

    def consumirProduto(self, nomeProduto, quantidade): # Função para consumir produto do inventário
        if nomeProduto in self.inventario: # Se o produto estiver no inventário
            self.inventario[nomeProduto].consumoCliente(quantidade) # Consome a quantidade
            print(f"{quantidade} unidades de {nomeProduto} consumidas.") # Informa que a quantidade foi consumida
        else: # Se o produto não estiver no inventário
            print(f"Produto {nomeProduto} não encontrado.") # Informa que o produto não foi encontrado

    def verificarInventario(self, nomeProduto): # Função para verificar inventário
        if nomeProduto in self.inventario: # Se o produto estiver no inventário
            print(f"{self.inventario[nomeProduto].quatiProduto} unidades de {nomeProduto} disponíveis.") # Informa a quantidade disponível
            return self.inventario[nomeProduto].quatiProduto # Retorna a quantidade
        else: # Se o produto não estiver no inventário
            print(f"Produto {nomeProduto} não encontrado no inventário.") # Informa que o produto não foi encontrado
            return 0 # Retorna 0

# Exemplo de uso da aplicação
def main():
    g = Gestor() # Inicializa o gestor do restaurante

    # Cria dois clientes
    c1 = Cliente("João", "joao@email.com")
    c2 = Cliente("Maria", "maria@email.com")

    # Adiciona duas reservas para os clientes
    d1 = datetime.now() + timedelta(days=1)
    d2 = datetime.now() + timedelta(days=2)
    g.adicionarReserva(c1, 4, d1)
    g.adicionarReserva(c2, 3, d2)

    # Verifica as reservas
    g.verificarReserva("João")
    g.verificarReserva("Maria")

    # Adiciona produtos ao inventário
    g.addProduto("Arroz", 50)
    g.addProduto("Massa", 30)

    # Consome produtos do inventário
    g.consumirProduto("Arroz", 10)
    g.consumirProduto("Massa", 5)

    # Verifica inventário
    g.verificarInventario("Arroz")
    g.verificarInventario("Massa")
    g.verificarInventario("Feijão")

    # Lista as reservas dos clientes
    c1.listarReservaCliente()
    c2.listarReservaCliente()

    # Cancela uma reserva
    g.cancelarReserva(c1, d1)

    # Verifica a reserva de João após o cancelamento
    g.verificarReserva("João")

if __name__ == "__main__":
    main()
