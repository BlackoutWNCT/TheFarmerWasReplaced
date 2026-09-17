## Imports:
from grounds import make_grassland, make_soil, make_wet, fertilise
from plants import check_petals

def plant_grass():
    make_grassland()
    plant(Entities.Grass)

def plant_bush():
    make_grassland()
    plant(Entities.Bush)
    
def plant_carrot():
    make_soil()
    make_wet()
    plant(Entities.Carrot)
    
def plant_pumpkin():
    make_soil()
    make_wet()
    plant(Entities.Pumpkin)
    
def plant_wood(tree_locations):
    current_pos = [get_pos_x(),get_pos_y()]
    illegal_pos = []
    illegal_pos.append([current_pos[0] + 1, current_pos[1]])
    illegal_pos.append([current_pos[0] - 1, current_pos[1]])
    illegal_pos.append([current_pos[0], current_pos[1] - 1])
    illegal_pos.append([current_pos[0], current_pos[1] + 1])
    tree_planted = False
    if len(tree_locations) == 0:
        plant(Entities.Tree)
        tree_planted = True
    else:
        plant_tree = True
        for i in illegal_pos:
            if i in tree_locations:
                plant_tree = False
        if plant_tree == True:
            make_wet()
            plant(Entities.Tree)
            tree_planted = True
        else:
            plant(Entities.Bush)
            fertilise()
                
    if tree_planted == True:
        current_pos = [get_pos_x(),get_pos_y()]
        tree_locations.append(current_pos)
        return tree_locations


        
def plant_sunflower(petals_dict):
    make_soil()
    make_wet()
    plant(Entities.Sunflower)
    check_petals(petals_dict)