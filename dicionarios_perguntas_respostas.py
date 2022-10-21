
print()
respostas_certas = 0
perguntas = {
    'pergunta 1': {
        'pergunta': 'Quanto é 2+2 ?',
        'respostas': {'a': '1', 'b': '4', 'c': '5', },
        'resposta_certa': 'b',
    },
    'pergunta 2': {
        'pergunta': 'Quanto é 3*2 ?',
        'respostas': {'a': '4', 'b': '10', 'c': '6', },
        'resposta_certa': 'c',
    },
    'pergunta 3': {
        'pergunta': 'Quanto é 9/3 ?',
        'respostas': {'a': '4', 'b': '10', 'c': '3', },
        'resposta_certa': 'c',
    },
    'pergunta 4': {
        'pergunta': 'Quanto é 10/5 ?',
        'respostas': {'a': '2', 'b': '10', 'c': '6', },
        'resposta_certa': 'a',
    },
}

for pk, pv in perguntas.items():
    print(f'{pk}: {pv["pergunta"]}')

    print('Respostas: ')
    for rk, rv in pv['respostas'].items():
        print(f'[{rk}]: {rv}')

    resposta_us = input('Resposta: ')

    if resposta_us == pv['resposta_certa']:
        print('Voce acertou!!!')
        respostas_certas += 1
    else:
        print('Voce errou!!!')

    print()

qtd_perguntas = len(perguntas)
porcentagem_acerto = respostas_certas / qtd_perguntas * 100

print(f'Voce acertou {respostas_certas} respostas.')
print(f'Sua porcentagem de acertou foi de {porcentagem_acerto}%.')
