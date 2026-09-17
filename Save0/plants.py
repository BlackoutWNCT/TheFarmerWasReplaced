## Functions:
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
        if plant_tree == False:
            break
        else:
            plant_tree = True
    return plant_tree
    