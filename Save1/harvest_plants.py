from plants import check_petals
from plant_plants import plant_sunflower

def harvest_sunflower(petals_dict):
    x, y, petals = check_petals(petals_dict)
    petals_list = []
    for key in petals_dict:
        petals_list.append(petals_dict[key])
    if petals == 15 or petals >= max(petals_list):
        harvest()
        petals_dict.pop((x,y))
    else:
        till()
        plant_sunflower(petals_dict)
        
def harvest_tree(tree_locations):
    current_pos = [get_pos_x(),get_pos_y()]
    harvest()
    tree_locations.remove((current_pos))