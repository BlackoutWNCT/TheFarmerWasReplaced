## Imports:
from plant_plants import plant_grass, plant_bush, plant_carrot, plant_pumpkin, plant_wood, plant_sunflower
from harvest_plants import harvest_sunflower, harvest_tree
from plants import check_planted
from housekeeping import unlock_item

## Constants:
steps = get_world_size() * get_world_size()
petals_dict = {}
tree_locations = []

## Functions:

while True:
    if get_pos_y() == 0:
        move(East)
    if can_harvest():
        planted = check_planted()
        if planted == Entities.Sunflower:
            harvest_sunflower(petals_dict)
        elif planted == Entities.Tree:
            harvest_tree(tree_locations)
        elif planted in [Entities.Grass, Entities.Bush, Entities.Carrot, Entities.Pumpkin]:    
            harvest()
    if get_pos_y() != 0 and get_pos_y() != range(get_world_size())[-1] and get_pos_x() != 0 and get_pos_x() != range(get_world_size())[-1]:
        if num_items(Items.Hay) >= 1000 * 200 and num_items(Items.Wood) >= 1000 * 200:
            if num_items(Items.Carrot) > num_items(Items.Pumpkin):
                plant_pumpkin()
            else:
                plant_carrot()
        else:
            if num_items(Items.Hay) > num_items(Items.Wood):
                plant_wood(tree_locations)
            else: 
                plant_grass()
    else:
        plant_sunflower(petals_dict)
    move(North)
    if get_pos_x() == 0 and get_pos_y() == 0:
        unlock_item(Unlocks.Expand)
        