from math import trunc


def txt_to_list(path):
    with open(path, "r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]

def add_with_wrap(value, increment):
    return (value+increment)%100

def sub_with_wrap(value, increment):
    return (value-increment)%100


liste = txt_to_list("input.txt")


def rotation():
    init = 50
    count = 0

    for elem in liste:
        direction = elem[0]
        valeur = int(elem[1:])

        if direction == 'R':
            init = add_with_wrap(init, valeur)
        elif direction == 'L':
            init = sub_with_wrap(init, valeur)
        if init == 0:
            count += 1
    return count

print('Le mot de passe est ' + str(rotation()))

