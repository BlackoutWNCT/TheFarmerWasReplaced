## Imports:
from grounds import fertilise

def plant_wood(timber):
    plant_tree = None
    plant_tree = check_tree_plantable(plant_tree)

    if plant_tree == True:
        plant(Entities.Tree)
    else:
        plant(Entities.Bush)
        fertilise()

def harvest_wood():
    harvest()

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