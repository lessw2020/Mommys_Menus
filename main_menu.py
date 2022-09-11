import random

items=['pizza','yummy mac','cous cous', 'mien mien','salmon',
'ribbeye steak','beef and tomato','ribs','pork and tofu','bulgolgi']

dinners=set(items)

print(f'The current menu selection has {len(dinners)} items.')

menu=random.sample(dinners,k=7)
print(f'your dinners this week are:\n {menu}')