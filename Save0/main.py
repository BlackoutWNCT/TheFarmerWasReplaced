## Imports:
from plant_plants import plant_grass, plant_bush, plant_carrot, plant_pumpkin, plant_wood, plant_sunflower
from harvest_plants import harvest_sunflower, harvest_tree
from plants import check_planted
from housekeeping import unlock_item, rts, advance
from fg_actions import max_pumpkin

## Constants:
steps = get_world_size() * get_world_size()
petals_dict = {}

## Functions:

## main:
while True:
    rts()
    for i in range(steps * 10):
        if can_harvest():
            planted = check_planted()
            if planted == Entities.Sunflower:
                harvest_sunflower(petals_dict)
            elif planted == Entities.Tree:
                harvest_tree()
            elif planted in [Entities.Grass, Entities.Bush, Entities.Carrot, Entities.Pumpkin]:    
                harvest()
        if get_pos_y() != 0 and get_pos_y() != range(get_world_size())[-1] and get_pos_x() != 0 and get_pos_x() != range(get_world_size())[-1]:
            if num_items(Items.Hay) >= 2500 ** 2 and num_items(Items.Wood) >= 2500 ** 2:
                if num_items(Items.Carrot) > num_items(Items.Pumpkin):
                    plant_pumpkin()
                else:
                    plant_carrot()
            else:
                if num_items(Items.Hay) > num_items(Items.Wood):
                    plant_wood()
                else:
                    plant_grass()
        else:
            plant_sunflower(petals_dict)
        advance()
    max_pumpkin(steps)

    unlock_item(Unlocks.Grass)
    unlock_item(Unlocks.Carrots)
    unlock_item(Unlocks.Trees)
    unlock_item(Unlocks.Pumpkins)
        