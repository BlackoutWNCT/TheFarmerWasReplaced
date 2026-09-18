## Imports:
from housekeeping import unlock_item, rts, advance, check_planted, get_resources

from hay import *
from wood import *
from carrot import *
from pumpkin import *
from sunflower import *

## Constants:
steps = get_world_size() * get_world_size()
petals_dict = {}
resources = {Items.Hay:0, Items.Wood:0, Items.Carrot:0, Items.Pumpkin:0}
power_up = None

## Functions:

## main:
while True:
    get_resources(resources)
    rts()
    for i in range(steps):
        if can_harvest():
            planted = check_planted()
            if planted == Entities.Sunflower:
                harvest_sunflower(petals_dict)
            elif planted == Entities.Tree:
                harvest_wood()
            elif planted in [Entities.Grass, Entities.Bush, Entities.Carrot, Entities.Pumpkin]:    
                harvest()
            last_harvest = planted
        if get_pos_y() != 0 and get_pos_y() != range(get_world_size())[-1] and get_pos_x() != 0 and get_pos_x() != range(get_world_size())[-1]:
            if resources[Items.Hay] > resources[Items.Wood] and resources[Items.Wood] >= get_cost(Entities.Carrot)[Items.Wood]:
                if resources[Items.Wood] > resources[Items.Carrot] and resources[Items.Wood] >= get_cost(Entities.Carrot)[Items.Wood]:
                    if resources[Items.Carrot] > resources[Items.Pumpkin] and resources[Items.Carrot] >= (get_cost(Entities.Pumpkin)[Items.Carrot] * steps) * 2:
                        max_pumpkin(steps, petals_dict)
                    else:
                        plant_carrot()
                else:
                    plant_wood()
            else:
                plant_hay()
        else:
            if len(petals_dict) == (get_world_size() * 4) - 4:
                power_up = False
            elif len(petals_dict) < 1:
                power_up = True
            plant_sunflower(petals_dict, power_up)
        advance()

    unlock_item(Unlocks.Grass)
    unlock_item(Unlocks.Carrots)
    unlock_item(Unlocks.Trees)
    unlock_item(Unlocks.Pumpkins)