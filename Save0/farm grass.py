## This file is used to idle farm grass while I'm
## working on resolving issues in main

## This can be later expanded to plant and harvest other
## plants, but grass is free

while True:
    if get_pos_y() == 0:
        move(East)
    harvest()
    if get_ground_type() == Grounds.Soil:
        till()
    move(North)