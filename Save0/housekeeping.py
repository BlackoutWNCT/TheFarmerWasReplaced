## Imports:

## Functions:
def unlock_item(unlockable):
    if num_unlocked(unlockable) > 0:
        cost = get_cost(unlockable)
        for key in cost:
            if num_items(key) > cost[key]:
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

def check_petals(petals_dict):
    x, y = get_pos_x(), get_pos_y()
    count = measure()
    petals_dict[(x,y)] = count
    return x, y, count
    
def check_planted():
    return get_entity_type()
    
def check_tree_plantable(plant_tree):
    directions = {East:West, North:South, South:North, West:East}
    for key in directions:
        move(directions[key])
        if get_entity_type() == Entities.Tree:
            plant_tree = False
            move(key)
            break
        else:
            plant_tree = True
        move(key)
    return plant_tree

def get_resources(resources):
    for key in resources:
        resources[key] = num_items(key)

def reset_grid(steps):
    for i in range(steps):
        harvest()
        if get_ground_type() == Grounds.Soil:
            till()
        advance()
    rts()