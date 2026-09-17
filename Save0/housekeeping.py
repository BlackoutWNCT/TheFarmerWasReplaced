## Functions:
def unlock_item(unlockable):
    if num_unlocked(unlockable) > 0:
        info = get_cost(unlockable)
        for key in info:
            item = key
            cost = info[key]
        if num_items(key) > cost:
            unlock(unlockable)
            print(unlockable, " has been unlocked")

def rts():
    for x in range(get_pos_x()):
        move(West)
    for y in range(get_pos_y()):
        move(South)

def advance():
    if get_pos_y() == get_world_size() - 1:
        move(East)
        move(North)
    else:
        move(North)