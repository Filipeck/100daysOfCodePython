def turn_right():
    turn_left()
    turn_left()
    turn_left()

# para esta solução, o que pensei foi "independente de onde o robô nascer, ele precisa encontrar o primeiro obstáculo"
# para isso ele irá verificar se há primeiro alguma parede na direita. Caso não haja ele seguirá até encontrar a primeira parede.
if right_is_clear():
    while front_is_clear():
        move()
# ao encontrar uma parede na frente, ele vira para a esquerda, desta forma a parede ficará na direita dele e com isso basta seguir
# o loop while abaixo, até chegar no objetivo.
turn_left()

while not at_goal():
        
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()