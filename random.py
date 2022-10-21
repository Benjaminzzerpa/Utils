import random
import string

# inteiro = random.randint(10, 20)
# inteiro = random.randrange(900, 1000, 10)
# flutuante = random.uniform(10, 20)
# flutuante = random.random()
lista = ['luiz', 'benjamin', 'yosely', 'francisco', 'rebeca', 'mateus', 'ronaldo', 'rubia']
# sorteio = random.choice(lista)
# sorteio = random.choices(lista, k=2)
# sorteio = random.sample(lista, 2)

#random.shuffle(lista)

# gerar senha aleatoria:
letras = string.ascii_letters
digitos = string.digits
caracteres = '!@#$%&*'
geral = letras + digitos + caracteres
senha = "".join(random.choices(geral, k=20))

print(senha)
