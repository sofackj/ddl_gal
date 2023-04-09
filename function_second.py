from check_functions import test_requests
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

#
def pages_list(url, back_url=''):
    list_url_pages = []
    #
    n = 1
    #
    while True:
        url_page = f"{url}{n}{back_url}"
        if test_requests(url_page):
            list_url_pages.append(url_page)
            # print(url_page)
            n += 1
        else:
            break
    return list_url_pages
