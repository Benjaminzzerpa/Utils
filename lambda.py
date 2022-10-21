
list = [
    ['p1', 7],
    ['p2', 13],
    ['p3', 14],
    ['p4', 11],
    ['p5', 50],
]
print(sorted(list, key=lambda i: i[0], reverse=True))
print(list)
