A = type(
    'A',
    (),
    {
        'attr': 'ola, mundo'
    }
)

a = A()
print(a.attr)