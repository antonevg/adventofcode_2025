from math import trunc


def txt_to_list(path):
    with open(path, "r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]

def add_with_wrap(value, increment):
    return (value+increment)%100, (value+increment)//100

def sub_with_wrap(value, increment):
    return (value-increment)%100, abs((value-increment)//100)


liste = txt_to_list("input_test.txt")


def rotation(): #do not work
    init = 50
    count = 0

    for elem in liste:
        direction = elem[0]
        valeur = int(elem[1:])

        if direction == 'R':
            count += add_with_wrap(init, valeur)[1]
            init = add_with_wrap(init, valeur)[0]
        elif direction == 'L':
            count += sub_with_wrap(init, valeur)[1]
            init = sub_with_wrap(init, valeur)[0]
        print(init)
        print(count)
    return count

print('Le mot de passe est ' + str(rotation()))
