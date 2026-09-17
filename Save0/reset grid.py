steps = get_world_size() * get_world_size()


for i in range(steps):
    if get_pos_y() == 0:
        move(East)
    harvest()
    if get_ground_type() == Grounds.Soil:
        till()
    move(North)
for x in range(get_pos_x()):
    move(West)
for y in range(get_pos_y()):
    move(South)