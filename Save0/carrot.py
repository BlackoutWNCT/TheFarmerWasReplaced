## Imports:
from grounds import make_soil, make_wet, fertilise
from wood import plant_wood
from hay import plant_hay

def plant_carrot():
    if num_items(Items.Wood) < get_cost(Entities.Carrot)[Items.Wood]:
        plant_wood()
        while can_harvest() == False:
            fertilise()
            make_wet()
            do_a_flip()
        harvest()
    elif num_items(Items.Hay) < get_cost(Entities.Carrot)[Items.Hay]:
        plant_hay()
        while can_harvest() == False:
            fertilise()
            make_wet()
            do_a_flip()
        harvest()
    make_soil()
    plant(Entities.Carrot)

def harvest_carrot():
    harvest()
