# Definição dos dicionários
filmes = [
    {
        'id': '1',
        'nome': 'Senhor dos Anéis',
        'genero': 'Fantasia',
        'preco': 45
    },
    {
        'id': '2',
        'nome': 'As Branquelas',
        'genero': 'Comédia',
        'preco': 55
    },
    {
        'id': '3',
        'nome': 'Velozes e Furiosos 7',
        'genero': 'Ação',
        'preco': 100
    },
    {
        'id': '4',
        'nome': 'Velozes e Furiosos 6',
        'genero': 'Ação',
        'preco': 55
    },
    {
        'id': '5',
        'nome': 'The Scapegoat',
        'genero': 'Drama',
        'preco': 100
    },
    {
        'id': '6',
        'nome': 'Meu Malvado Favorito',
        'genero': 'Animação',
        'preco': 200
    }
]

# Inicialização das variáveis globais
carrinho = []


def adicionafilme():

    # Seleção dos filmes para inclusão no carrinho
    selecao = None

    while selecao != 'X':
        selecao = input(f'Qual é o código do filme que deseja dicionar (x para finalizar)? ')
        if selecao.upper() == 'X':
            break
        if validaselecao(selecao):
            carrinho.append(selecao)
        else:
            print(f'Valor inválido. Selecione um código existente no catálogo')

    # Exibe carrinho atual
    carrinhoatual()


def removefilme():

    if carrinhocheio():
        selecao = int(input(f'Qual item deseja remover? '))
        del(carrinho[selecao - 1])
    carrinhoatual()


def validaselecao(selecao):

    for item in filmes:
        if item['id'] == selecao:
            return True
    return False


def buscafilmeporid(id):

    for filme in filmes:
        if filme['id'] == id:
            return filme
    return None


def finalizacompra():

    if carrinhocheio():
        totaldacompra = 0
        for id in carrinho:
            filme = buscafilmeporid(id)
            totaldacompra += filme['preco']

        print(f'\nTotal do Carrinho: {totaldacompra:.2f}')

        # Aplica desconto no total da compra
        descontoadic = descontoadicional()
        totaldacompradesc = aplicadesconto(totaldacompra, descontoadic)

        print(f'Desconto concedido: {round((1 - (totaldacompradesc / totaldacompra)) * 100):.2f}%')
        print(f'Total com desconto: {totaldacompradesc:.2f}')


def aplicadesconto(totaldacompra, descontoadicional):

    if totaldacompra >= 100 and totaldacompra < 200:
        totaldacompra *= 0.9 - descontoadicional
    elif totaldacompra >= 200 and totaldacompra < 300:
        totaldacompra *= 0.8 - descontoadicional
    elif totaldacompra >= 300 and totaldacompra < 400:
        totaldacompra *= 0.75 - descontoadicional
    elif totaldacompra >= 400:
        totaldacompra *= 0.7 - descontoadicional
    return totaldacompra


def descontoadicional():

    for id in carrinho:
        filme = buscafilmeporid(id)
        if filme['genero'] == 'Ação':
            return 0.05
    return 0


def carrinhoatual():

    i = 1
    print(f'\n{" Seu Carrinho ":-^60}\n')
    for id in carrinho:
        filme = buscafilmeporid(id)
        print(f"Item: {i:<5} {filme['nome']:<23} Preço: {filme['preco']:.2f}")
        i += 1
    print(f'\n{"-":-^60}\n')

    menuprincipal()
    return True


def menuprincipal():

    print(f'\n{" Menu Principal ":-^40}')
    print(f'{"A: Adicionar filmes":^40}')
    print(f'{"R: Remover filmes":^40}')
    print(f'{"F: Finalizar compra":^40}')
    print(f'{"-":-^40}\n')

    while True:
        opcao = input(f'Sua opção: ')

        if opcao.upper() == 'A':
            adicionafilme()
            break
        elif opcao.upper() == 'R':
            removefilme()
            break
        elif opcao.upper() == 'F':
            finalizacompra()
            break
        else:
            print(f'Opção {opcao.upper()} inválida!')


def carrinhocheio():
    if len(carrinho) <= 0:
        print(f'Não há itens no seu carrinho.')
        menuprincipal()
        return False
    return True

# Lista Filmes Disponíveis
print(f'{" Catálogo de Filmes ":-^80}\n')
for filme in filmes:
    print(f"Código: {filme['id']:<5} Nome: {filme['nome']:<23} Gênero:{filme['genero']:<10} Preço: {filme['preco']:.2f}")

menuprincipal()
