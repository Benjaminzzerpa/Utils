def func(parametro):
    if parametro % 5 == 0 and parametro % 3 == 0:
        return f'fizzbuzz, {parametro} divisivel por 3 e 5.'
    if parametro % 5 == 0:
        return f'fizz, {parametro} divisivel por 5.'
    if parametro % 3 == 0:
        return f'buzz, {parametro} divisivel por 3.'
    return parametro

from random import randint

for i in range(100):
    aleatorio = randint(0, 100)
    print(func(aleatorio))
