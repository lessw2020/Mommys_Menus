import random
from collections import defaultdict

Alexa_dinners = [
    "pizza",
    "yummy mac",
    "cous cous",
    "mien mien",
    "salmon",
    "ribbeye steak",
    "ribs",
    "bulgolgi",
    "hamburger",
]

less_dinners = [
    "pizza",
    "steak",
    "beef and tomato",
    "pork and tofu",
    "lasagnia",
    "bulgolgi",
    "pork and cuccumber",
]

Christine_dinners = [
    "chicken salad",
    "hamburger",
    "steak",
    "bulgogi",
    "salmon",
    "carb balance burrito",
]

total_meals = [Alexa_dinners, less_dinners, Christine_dinners]
dinners = set()
for person in total_meals:
    for meals in person:
        dinners.add(meals.capitalize())

# dinners=set(total_meals)
# print(dinners)
dinner_selection = list(dinners)
print(f"The current menu selection has {len(dinners)} items.")

# menu=random.sample(dinner_selection, k=4)
# print(f'\n your dinners this week are:\n {menu}\n')
amount = 5
names = ["Less", "Christine", "Alexa"]
names_to_index = {names[0]: 0, names[1]: 1, names[2]: 2}

picks_less = random.sample(less_dinners, k=amount)
picks_Christine = random.sample(Christine_dinners, k=amount)
picks_Alexa = random.sample(Alexa_dinners, k=amount)


# for index,(a,b,c) in enumerate(zip(picks_less, picks_Christine, picks_Alexa)):
#    print(f'{index+1} -- less {a}, Christine {b}, Alexa {c}')

all_picks = [picks_less, picks_Christine, picks_Alexa]
linkage = defaultdict(list)
# print(f"review dict")
for i, selection in enumerate(all_picks):
    for item in selection:
        linkage[item].append(names[i])

# print(f"linkage dict = {linkage}")
# print(f"total duplication")


def get_shared_items(linkage):
    res = []
    for key, value in linkage.items():
        if len(value) > 1:
            # print(f"{key} selected by {value}")
            res.append((key, value))
    return res


def one_day_picks(names, linkage, *args):
    # first try to select duplicate items

    todays_menu = {names[0]: "", names[1]: "", names[2]: ""}
    shared_items = get_shared_items(linkage)
    key, value = None, None
    if shared_items:
        # remove from linkage as we are using it
        key, value = shared_items[0]
        del linkage[key]
        print(f"\n selected dupe item {key} by {value}\n")
        # we need to remove from random selection as well
        for index, person in enumerate(value):
            index_picks = names_to_index[person]
            curr = args[index_picks]
            curr.remove(key)
            # print(f"removed dupe - updated list: {args[index_picks]}")
            todays_menu[person] = key
    total_people = len(args)

    print(f"Todays selection for {total_people} people:")

    # we need to populate total menu for today
    for index, person in enumerate(todays_menu.keys()):
        if not todays_menu[person]:
            # if we did not get a menu item from the dupes, select a new item
            menu_item = random.sample(args[index], k=1)[0]
            # print(f"menu item = {menu_item} for list {index} =  {args[index]}")
            curr = args[index]
            curr.remove(menu_item)
            # print(f"curr list = {curr}")
            todays_menu[person] = menu_item

    # print todays menu:
    print(f"Today's menu = {todays_menu}")


for i in range(2):
    one_day_picks(names, linkage, picks_less, picks_Christine, picks_Alexa)
