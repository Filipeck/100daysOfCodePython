def turn_right():
    turn_left()
    turn_left()
    turn_left()

def search_right():
    for i in range(4):        
        if wall_on_right():
            break
        turn_left()

while not at_goal():
    
    if right is clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()