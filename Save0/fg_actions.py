## Imports:
from plant_plants import plant_pumpkin
from housekeeping import rts, advance

## Functions:
def reset_grid(steps):
    for i in range(steps):
        harvest()
        if get_ground_type() == Grounds.Soil:
            till()
        move()
    rts()
        
def max_pumpkin(steps):
    biggy_p = False
    while biggy_p == False:
        dead_pumpkin = False
        for i in range(steps):
            if get_entity_type() != Entities.Pumpkin:
                harvest()
                plant_pumpkin()
                dead_pumpkin = True
            advance()
        if dead_pumpkin == False:
            biggy_p = True
            rts()
            harvest()
