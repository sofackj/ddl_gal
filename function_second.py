from random import choice

def random_items_from_list(nb, target_list):
    new_list = []
    for i in range(nb):
        # Choose a random item
        random_item = choice(target_list)
        # Add the random item to the list
        new_list.append(random_item)
        # Remove the item from the first list
        target_list.remove(random_item)
    # Return the first list modified with the new list
    return target_list, new_list