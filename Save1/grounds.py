def check_ground():
    return get_ground_type()

def check_water():
    return get_water()

def make_grassland():
    if check_ground() != Grounds.Grassland:
        till()        

def make_soil():
    if check_ground() != Grounds.Soil:
        till()
        
def make_wet():
    if check_water() < 1:
        if num_items(Items.water) > 0:
            use_item(Items.Water)

def fertilise():
    if num_items(Items.Fertilizer) > 0:
        use_item(Items.Fertilizer)