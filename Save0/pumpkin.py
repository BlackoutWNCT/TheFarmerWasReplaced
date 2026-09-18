## Imports:
from grounds import make_soil, make_wet, fertilise
from carrot import plant_carrot
from housekeeping import rts, advance
from sunflower import harvest_sunflower

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

def harvest_pumpkin():
    harvest()

def max_pumpkin(steps, petals_dict):
    biggy_p = False
    dead_pumpkin = None
    while biggy_p == False:
        for i in range(steps):
            if get_entity_type() != Entities.Pumpkin:
                if get_entity_type() == Entities.Sunflower:
                    harvest_sunflower(petals_dict)
                else:
                    harvest()
                plant_pumpkin()
                dead_pumpkin = True
            advance()
        if dead_pumpkin != True:
            biggy_p = True
            rts()
            harvest()