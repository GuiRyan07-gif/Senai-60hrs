# Estrutura do e-commerce usando dicionários
produtos = {
    "livros": 50.00,
    "tablets": 1200.00,
    "fones": 150.00
}

carrinho = []


def comprar(item):
    if item in produtos:
        carrinho.append(produtos[item])
        print(f"{item.capitalize()} adicionado ao carrinho!")
    else:
        print("Produto não encontrado.")


def pagar():
    total = sum(carrinho)
    print(f"Valor total da compra: R$ {total:.2f}")


