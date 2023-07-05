import random

family = ['Justin/Canada', 'Nicholas', 'Emma', 'Nora', 'Alexander']

choice = random.randint(0, len(family) - 1)

dish_washer = family[choice]

print("{} will wash dishes tonight.".format(dish_washer))

