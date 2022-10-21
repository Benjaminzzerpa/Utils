while True:
    cpf = input('Digite o CPF: ')
    novo_cpf = cpf[:-2]
    reverse = 10
    total = 0
    for index in range(19):
        if index > 8:
            index -= 9

        total += int(novo_cpf[index]) * reverse

        reverse -= 1
        if reverse < 2:
            reverse = 11
            d = 11 - (total % 11)

            if d > 9:
                d = 0
            total = 0
            novo_cpf += str(d)

    sequence = novo_cpf == str(novo_cpf[0]) * len(cpf)

    if cpf == novo_cpf:
        print('Valido.')
    else:
        print('Invalido.')
