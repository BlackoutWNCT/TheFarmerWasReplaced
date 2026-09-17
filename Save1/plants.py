def check_petals(petals_dict):
    x, y = get_pos_x(), get_pos_y()
    count = measure()
    petals_dict[(x,y)] = count
    return x, y, count
    
def check_planted():
    return get_entity_type()