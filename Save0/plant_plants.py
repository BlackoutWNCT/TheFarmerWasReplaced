## Imports:
from grounds import make_grassland, make_soil, make_wet, fertilise
from plants import check_petals, check_tree_plantable

def plant_grass():
    make_grassland()

def plant_bush():
    make_grassland()
    plant(Entities.Bush)
    
def plant_carrot():
    if num_items(Items.Wood) <= 128:
        plant_wood()
        while can_harvest() == False:
            fertilise()
            make_wet()
            do_a_flip()
        harvest()
    elif num_items(Items.Hay) <= 128:
        plant_grass()
        while can_harvest() == False:
            fertilise()
            make_wet()
            do_a_flip()
        harvest()
    make_soil()
    plant(Entities.Carrot)
    
def plant_pumpkin():
    if num_items(Items.Carrot) <= 64:
        plant_carrot()
        while can_harvest() == False:
            fertilise()
            make_wet()
            do_a_flip()
        harvest()
    make_soil()
    plant(Entities.Pumpkin)
    
def plant_wood():
    plant_tree = None
    plant_tree = check_tree_plantable(plant_tree)

    if plant_tree == True:
        plant(Entities.Tree)
    else:
        plant(Entities.Bush)
        fertilise()
        
def plant_sunflower(petals_dict):
    if len(petals_dict) < (get_world_size() * 4) - 4:
        make_soil()
        if num_items(Items.Carrot) <= 1:
            till()
            plant_carrot()
            while can_harvest() == False:
                fertilise()
                make_wet()
                do_a_flip()
            harvest()
        if get_entity_type() != Entities.Sunflower:
            plant(Entities.Sunflower)
    if get_entity_type() == Entities.Sunflower:
        check_petals(petals_dict)