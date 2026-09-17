def unlock_item(unlockable):
    if num_unlocked(unlockable) > 0:
        info = get_cost(unlockable)
        for key in info:
            item = key
            cost = info[key]
        if num_items(key) > cost:
            unlock(unlockable)
            print(unlockable, " has been unlocked")
        else:
            print("Not enough ", key, " to unlock", unlockable, ". Need ", cost, " Have: ", num_items(key))
    else:
        print(unlockable, "Is not yet unlocked")