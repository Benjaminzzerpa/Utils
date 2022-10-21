carrinho = []

carrinho.append(('produto 1', 10.34))
carrinho.append(('produto 2', 20))
carrinho.append(('produto 3', 30.99))
carrinho.append(('produto 4', 40))
carrinho.append(('produto 5', 55.90))

total = sum([float((produto[1])) for produto in carrinho])
print(total)
