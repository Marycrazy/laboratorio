##@file lab02
# @brief Este ficheiro contém um exemplo de aplicação de um sistema de reservas de restaurante.

from datetime import datetime, timedelta

## @class Cliente
#  @brief Esta classe representa um cliente do restaurante.
#  @details Possui os métodos adicionarReserva e listarReservasCliente.
class Cliente:
    ## @brief Construtor da classe Cliente.
    #  @param nome Nome do cliente.
    #  @param email Email do cliente.
    def __init__(self, nome, email):
        ## @var nome
        #  @brief Nome do cliente.
        self.nome = nome
        ## @var email
        #  @brief Email do cliente.
        self.email = email
        ## @var reservas
        #  @brief Lista de reservas do cliente.
        self.reservas = []

    ## @brief Método adicionarReserva.
    #  @details Anexa uma reserva ao cliente.
    #  @param reserva Objeto do tipo Reserva.
    def adicionarReserva(self, reserva):
        self.reservas.append(reserva)

    ## @brief Método listarReservasCliente.
    #  @details Lista as reservas de um dado cliente.
    def listarReservasCliente(self):
        if not self.reservas:
            print(f"{self.nome} não tem reservas.")
            return
        print(f"Reservas de {self.nome}:")
        for reserva in self.reservas:
            print(f"- {reserva.num_pessoas} pessoas no dia {reserva.data_reserva}, mesa {reserva.mesa.numero_mesa}")

## @class Mesa
#  @brief Esta classe representa uma mesa do restaurante.
#  @details Possui os métodos reservar e libertarMesa.
class Mesa:
    ## @brief Construtor da classe Mesa.
    #  @param numero_mesa Número da mesa.
    #  @param capacidade_mesa Capacidade da mesa.
    def __init__(self, numero_mesa, capacidade_mesa):
        ## @var numero_mesa
        #  @brief Número da mesa.
        self.numero_mesa = numero_mesa
        ## @var capacidade_mesa
        #  @brief Capacidade da mesa.
        self.capacidade_mesa = capacidade_mesa
        ## @var reservada
        #  @brief Estado de reserva da mesa.
        self.reservada = False

    ## @brief Método reservar.
    #  @details Reserva a mesa se estiver disponível.
    #  @throws Exception Se a mesa já estiver reservada.
    def reservar(self):
        if self.reservada:
            raise Exception(f"A mesa {self.numero_mesa} já está reservada!")
        self.reservada = True

    ## @brief Método libertarMesa.
    #  @details Define a mesa como não reservada.
    def libertarMesa(self):
        self.reservada = False

## @class Reserva
#  @brief Esta classe representa uma reserva de um cliente.
#  @details Possui os atributos cliente, num_pessoas, data_reserva e mesa.
class Reserva:
    ## @brief Construtor da classe Reserva.
    #  @param cliente Objeto do tipo Cliente.
    #  @param num_pessoas Número de pessoas.
    #  @param data_reserva Data da reserva.
    #  @param mesa Objeto do tipo Mesa.
    def __init__(self, cliente, num_pessoas, data_reserva, mesa):
        ## @var cliente
        #  @brief Cliente que fez a reserva.
        self.cliente = cliente
        ## @var num_pessoas
        #  @brief Número de pessoas para a reserva.
        self.num_pessoas = num_pessoas
        ## @var data_reserva
        #  @brief Data da reserva.
        self.data_reserva = data_reserva
        ## @var mesa
        #  @brief Mesa reservada.
        self.mesa = mesa

## @class Produto
#  @brief Esta classe representa um produto do inventário.
#  @details Possui os atributos nome_produto e quantidade_produto.
class Produto:
    ## @brief Construtor da classe Produto.
    #  @param nome_produto Nome do produto.
    #  @param quantidade_produto Quantidade do produto.
    def __init__(self, nome_produto, quantidade_produto):
        ## @var nome_produto
        #  @brief Nome do produto.
        self.nome_produto = nome_produto
        ## @var quantidade_produto
        #  @brief Quantidade do produto.
        self.quantidade_produto = quantidade_produto

    ## @brief Método consumoCliente.
    #  @details Diminui a quantidade do produto após o consumo.
    #  @param quantidade Quantidade consumida.
    #  @throws Exception Se a quantidade consumida for superior à quantidade disponível.
    def consumoCliente(self, quantidade):
        if quantidade > self.quantidade_produto:
            raise Exception(f"Quantidade insuficiente de {self.nome_produto}!")
        self.quantidade_produto -= quantidade

## @class Gestor
#  @brief Esta classe representa o gestor do restaurante.
#  @details Possui os atributos lista_reservas, inventario e mesas.
class Gestor:
    ## @brief Construtor da classe Gestor.
    #  Inicializa a lista de reservas, o inventário e as mesas.
    #  Cria 10 mesas de 4 pessoas.
    def __init__(self):
        ## @var lista_reservas
        #  @brief Lista de todas as reservas.
        self.lista_reservas = []
        ## @var inventario
        #  @brief Dicionário com o inventário de produtos.
        self.inventario = {}
        ## @var mesas
        #  @brief Lista de mesas do restaurante.
        self.mesas = [Mesa(i, 4) for i in range(1, 11)]

    ## @brief Método adicionarReserva.
    #  @details Adiciona uma reserva para um cliente.
    #  @param cliente Objeto do tipo Cliente.
    #  @param num_pessoas Número de pessoas.
    #  @param data Data da reserva.
    def adicionarReserva(self, cliente, num_pessoas, data):
        mesa = self.encontrarMesa(num_pessoas)
        if not mesa:
            print("Não há mesas disponíveis.")
            return

        reserva = Reserva(cliente, num_pessoas, data, mesa)
        cliente.adicionarReserva(reserva)
        mesa.reservar()
        self.lista_reservas.append(reserva)
        print(f"Reserva feita para {cliente.nome}: {num_pessoas} pessoas no dia {data}, mesa {mesa.numero_mesa}.")

    ## @brief Método encontrarMesa.
    #  @details Encontra uma mesa disponível para um dado número de pessoas.
    #  @param num_pessoas Número de pessoas.
    #  @return Mesa Primeira mesa disponível com capacidade suficiente, ou None se não houver mesa disponível.
    def encontrarMesa(self, num_pessoas):
        for mesa in self.mesas:
            if not mesa.reservada and mesa.capacidade_mesa >= num_pessoas:
                return mesa
        return None

    ## @brief Método verificarReserva.
    #  @details Verifica se existe uma reserva para um dado cliente.
    #  @param nome_cliente Nome do cliente.
    #  @return Reserva Reserva do cliente, caso exista, ou None caso contrário.
    def verificarReserva(self, nome_cliente):
        for reserva in self.lista_reservas:
            if reserva.cliente.nome == nome_cliente:
                print(f"Reserva encontrada para {nome_cliente}: {reserva.num_pessoas} pessoas no dia {reserva.data_reserva}, mesa {reserva.mesa.numero_mesa}.")
                return reserva
        print(f"Nenhuma reserva encontrada para {nome_cliente}.")
        return None

    ## @brief Método cancelarReserva.
    #  @details Cancela uma reserva para um dado cliente.
    #  @param cliente Objeto do tipo Cliente.
    #  @param data Data da reserva.
    def cancelarReserva(self, cliente, data):
        for reserva in self.lista_reservas:
            if reserva.cliente == cliente and reserva.data_reserva == data:
                reserva.mesa.libertarMesa()
                self.lista_reservas.remove(reserva)
                cliente.reservas.remove(reserva)
                print(f"Reserva de {cliente.nome} no dia {data} foi cancelada.")
                return
        print(f"Nenhuma reserva encontrada para {cliente.nome} no dia {data}.")

    ## @brief Método adicionarProduto.
    #  @details Adiciona um produto ao inventário.
    #  @param nome_produto Nome do produto.
    #  @param quantidade Quantidade do produto.
    def adicionarProduto(self, nome_produto, quantidade):
        if nome_produto in self.inventario:
            self.inventario[nome_produto].quantidade_produto += quantidade
        else:
            produto = Produto(nome_produto, quantidade)
            self.inventario[nome_produto] = produto
        print(f"{quantidade} unidades de {nome_produto} adicionadas ao inventário.")

    ## @brief Método consumirProduto.
    #  @details Consome um produto do inventário.
    #  @param nome_produto Nome do produto.
    #  @param quantidade Quantidade do produto.
    #  @throws Exception Se o produto não existir ou se não houver quantidade suficiente.
    def consumirProduto(self, nome_produto, quantidade):
        if nome_produto in self.inventario:
            try:
                self.inventario[nome_produto].consumoCliente(quantidade)
                print(f"{quantidade} unidades de {nome_produto} consumidas.")
            except Exception as e:
                print(f"Erro ao consumir {nome_produto}: {str(e)}")
        else:
            print(f"Produto {nome_produto} não encontrado.")

    ## @brief Método verificarInventario.
    #  @details Verifica a quantidade de um dado produto no inventário.
    #  @param nome_produto Nome do produto.
    #  @return int Quantidade do produto no inventário, ou 0 se o produto não existir.
    def verificarInventario(self, nome_produto):
        if nome_produto in self.inventario:
            quantidade = self.inventario[nome_produto].quantidade_produto
            print(f"{quantidade} unidades de {nome_produto} disponíveis.")
            return quantidade
        else:
            print(f"Produto {nome_produto} não encontrado no inventário.")
            return 0

## @brief Função principal.
#  @details Demonstra o funcionamento do sistema de reservas de restaurante.
def main():
    # Criação do gestor
    gestor = Gestor()

    # Criação de clientes
    cliente1 = Cliente("João", "joao@email.com")
    cliente2 = Cliente("Maria", "maria@email.com")

    # Adição de reservas
    data1 = datetime.now() + timedelta(days=1)
    data2 = datetime.now() + timedelta(days=2)
    gestor.adicionarReserva(cliente1, 4, data1)
    gestor.adicionarReserva(cliente2, 3, data2)

    # Verificação de reservas
    gestor.verificarReserva("João")
    gestor.verificarReserva("Maria")

    # Adição de produtos ao inventário
    gestor.adicionarProduto("Arroz", 50)
    gestor.adicionarProduto("Massa", 30)

    # Consumo de produtos
    gestor.consumirProduto("Arroz", 10)
    gestor.consumirProduto("Massa", 5)

    # Verificação do inventário
    gestor.verificarInventario("Arroz")
    gestor.verificarInventario("Massa")
    gestor.verificarInventario("Feijão")

    # Listagem de reservas dos clientes
    cliente1.listarReservasCliente()
    cliente2.listarReservasCliente()

    # Cancelamento de reserva
    gestor.cancelarReserva(cliente1, data1)

    # Verificação de reserva após cancelamento
    gestor.verificarReserva("João")

if __name__ == "__main__":
    main()