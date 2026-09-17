## Imports:
from grounds import make_soil, make_wet, fertilise
from carrot import plant_carrot

def plant_sunflower(petals_dict, power_up):
    if power_up == True:
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
            harvest()
            plant(Entities.Sunflower)
    else:
        plant_carrot()
    if get_entity_type() == Entities.Sunflower:
        check_petals(petals_dict)

def harvest_sunflower(petals_dict):
    x, y, petals = check_petals(petals_dict)
    petals_count = []
    for key in petals_dict:
        petals_count.append(petals_dict[key])
    if petals == 15 or petals >= max(petals_count):
        harvest()
        petals_dict.pop((x,y))

def check_petals(petals_dict):
    x, y = get_pos_x(), get_pos_y()
    count = measure()
    petals_dict[(x,y)] = count
    return x, y, count