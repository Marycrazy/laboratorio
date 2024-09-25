# Documentação Técnica: Sistema de Reservas de Restaurante

## 1. Visão Geral da Arquitetura

O sistema de reservas de restaurante é uma aplicação Python que gere reservas, clientes, mesas e inventário. A arquitetura é composta por várias classes que interagem entre si:

### 1.1. Componentes Principais

1. **Cliente**: Representa um cliente do restaurante.
2. **Mesa**: Representa uma mesa no restaurante.
3. **Reserva**: Representa uma reserva feita por um cliente.
4. **Produto**: Representa um item no inventário do restaurante.
5. **Gestor**: Gere todas as operações do sistema.

### 1.2. Fluxos de Dados

1. Cliente -> Gestor: O cliente fornece informações para fazer uma reserva.
2. Gestor -> Mesa: O gestor verifica a disponibilidade e reserva uma mesa.
3. Gestor -> Reserva: O gestor cria uma nova reserva.
4. Gestor -> Produto: O gestor atualiza o inventário ao adicionar ou consumir produtos.

### 1.3. Interações Principais

1. **Fazer Reserva**:
   - O cliente solicita uma reserva.
   - O gestor verifica a disponibilidade de mesas.
   - Se houver uma mesa disponível, cria-se uma nova reserva.

2. **Cancelar Reserva**:
   - O cliente solicita o cancelamento.
   - O gestor remove a reserva e liberta a mesa.

3. **Gerir Inventário**:
   - O gestor adiciona produtos ao inventário.
   - O gestor regista o consumo de produtos.

## 2. Descrição Detalhada dos Componentes

### 2.1. Cliente
- Atributos: nome, email, reservas
- Métodos: adicionarReserva, listarReservasCliente
- Descrição:
    - `adicionarReserva:` Anexa um Objeto do tipo Reserva à lista de reservas do cliente.
    - `listarReservasCliente` Verifica se existem reservas associadas ao cliente. Caso não existam, imprime uma mensagem informativa e sai do método. Caso existam, percorre a lista de reservas e imprime as informações de cada reserva.

### 2.2. Mesa
- Atributos: numero_mesa, capacidade_mesa, reservada
- Métodos: reservar, libertarMesa
- Descrição:
    - `reservar:` Verifica se a mesa está reservada. Caso esteja, levanta uma exceção e informa o utilizador que a mesa já está reservada. Caso contrário, atualiza o estado da mesa para reservada.
    - `libertarMesa:` Atualiza o estado da mesa para livre.

### 2.3. Reserva
- Atributos: cliente, num_pessoas, data_reserva, mesa

### 2.4. Produto
- Atributos: nome_produto, quantidade_produto
- Métodos: consumoCliente
- Descrição:
    - `consumoCliente:` Verifica se a quantidade de produtos disponíveis é suficiente para o consumo. Caso não seja, levanta uma exceção e informa o utilizador que não existem produtos suficientes. Caso contrário, atualiza a quantidade de produtos disponíveis no inventário.

### 2.5. Gestor
- Atributos: lista_reservas, inventario, mesas
- Métodos: adicionarReserva, encontrarMesa, verificarReserva, cancelarReserva, adicionarProduto, consumirProduto, verificarInventario
- Descrição:
    - `adicionarReserva:` Chama o método encontrarMesa para verificar a disponibilidade de mesas. Se não houver mesas disponíveis, imprime uma mensagem informativa e sai do método. Caso contrário, cria um Objeto do tipo Reserva e associa-lhe um Objeto do tipo Cliente, um número de pessoas, uma data e um Objeto do tipo Mesa. Adiciona a reserva à lista de reservas. Depois, chama o método adicionarReserva do Objeto do tipo Cliente para anexar a reserva à lista de reservas do cliente. Por fim, chama o método reservar do Objeto do tipo Mesa para atualizar o estado da mesa para reservada. Antes de sair do método, anexa a reserva à lista de reservas associada ao Gestor e imprime uma mensagem a informar que a reserva foi efetuada com sucesso.
    - `encontrarMesa:` Percorre a lista de mesas e verifica se exite uma mesa não reservada, com capacidade suficiente para o número de pessoas da reserva. Caso encontre uma mesa, retorna a mesa. Caso contrário, retorna None.
    - `verificarReserva:` Percorre a lista de reservas do Gestor e compara os nomes dos clientes com o nome do cliente fornecido. Caso encontre uma reserva associada ao cliente, imprime uma mensagem informativa e retorna a reserva. Caso contrário, apresenta uma mensagem informativa e retorna None.
    - `cancelarReserva:` Percorre a lista de reservas do Gestor e compara os Objetos do tipo Cliente e a data associados à reserva com o cliente e a data fornecidos. Caso encontre uma reserva associada, chama o método libertarMesa do Objeto do tipo Mesa para atualizar o estado da mesa para livre. Depois, remove a reserva da lista de reservas associada ao Gestor e remove a reserva da lista de reservas associada ao Cliente. Por fim, imprime uma mensagem informativa a informar que a reserva foi cancelada com sucesso e sai do método. Caso não encontre uma reserva associada, imprime uma mensagem informativa e sai do método.
    - `adicionarProduto:` Verifica se o nome do produto fornecido existe no dicionário de inventário. Caso exista, soma a quantidade fornecida à quantidade existente. Caso contrário, cria um novo Objeto do tipo Produto e associa-lhe um nome e uma quantidade. Adiciona o produto ao dicionário de inventário. Por fim, imprime uma mensagem informativa a informar que a quantidade de produtos foi atualizada com sucesso.
    - `consumirProduto:` Verifica se o nome do produto fornecido existe no dicionário de inventário. Caso não exista, imprime uma mensagem informativa e sai do método. Caso exista, chama o método consumoCliente do Objeto do tipo Produto para verificar se a quantidade de produtos disponíveis é suficiente para o consumo. Caso não seja, lança uma exceção e informa o utilizador que houve um erro no consumo do produto. Caso contrário, atualiza a quantidade de produtos disponíveis no inventário e imprime uma mensagem informativa a informar que o produto foi consumido com sucesso.
    - `verificarInventario:` Verfica se o nome do produto fornecido existe no dicionário de inventário. Caso não exista, imprime uma mensagem informativa e retorna 0. Caso exista, imprime a quantidade de produtos disponíveis e retorna a quantidade.


## 3. Fluxos de Dados Detalhado
1. O cliente fornece informações para uma reserva (nome, número de pessoas, data).
2. O gestor verifica a disponibilidade de mesas através do método `encontrarMesa`.
3. Se uma mesa estiver disponível, o gestor cria uma nova reserva e associa-a ao cliente e à mesa.
4. O gestor atualiza o estado da mesa para reservada.
5. Quando um produto é consumido, o gestor atualiza o inventário.

## 4. Considerações de Implementação

- O sistema utiliza a biblioteca `datetime` para gerir datas de reservas.
- As mesas são inicializadas com uma capacidade padrão de 4 pessoas.
- O inventário é gerido através de um dicionário para acesso rápido aos produtos.
- A documentação do código segue o padrão Doxygen para facilitar a geração automática de documentação.
