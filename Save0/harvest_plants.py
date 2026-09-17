## Imports:
from plants import check_petals
from plant_plants import plant_sunflower

## Functions:
def harvest_sunflower(petals_dict):
    if len(petals_dict) <= (get_world_size() * 4) - 4 and len(petals_dict) >= 10:
        x, y, petals = check_petals(petals_dict)
        petals_count = []
        for key in petals_dict:
            petals_count.append(petals_dict[key])
        if petals == 15 or petals >= max(petals_count):
            harvest()
            petals_dict.pop((x,y))
#    else:
#        till()
#        plant_sunflower(petals_dict)
        
def harvest_tree():
    harvest()