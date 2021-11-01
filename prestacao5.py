def prestacao(valor):
    for i in range(1,25):
        print(f'{i}x R$ {valor/i:6.2f}')


preco  = float(input("Digite o calor do produto:"))

prestacao(preco)