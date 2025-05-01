import random
import maths


def mutate(a_list):
    b_list = []
    new_item = 0
    for item in a_list:
        new_item = item * 2
        new_item += random.randint(1, 3)
        new_item = maths.add(new_item, item)
        b_list.append(new_item) # neste desafio o erro estava nesta linha, só foi necessário identar para que cada item fosse adicionado após sua modificação.
    print(b_list)


mutate([1, 2, 3, 5, 8, 13])
