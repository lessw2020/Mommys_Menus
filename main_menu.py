import random

Alexa_dinners=['pizza','yummy mac','cous cous', 'mien mien','salmon',
'ribbeye steak','ribs','bulgolgi','hamburger']

less_dinners=['pizza', 'steak','beef and tomato','pork and tofu','lasagnia','bulgogi', 'pork and cuccumber']

Christine_dinners=['chicken salad','hamburger','steak','bulgogi','salmon','carb balance burrito']

total_meals=[Alexa_dinners, less_dinners, Christine_dinners]
dinners=set()
for person in total_meals:
    for meals in person:
        dinners.add(meals)
#dinners=set(total_meals)
#print(dinners)
dinner_selection=list(dinners)
print(f'The current menu selection has {len(dinners)} items.')

#menu=random.sample(dinner_selection, k=4)
#print(f'\n your dinners this week are:\n {menu}\n')
amount=4
picks_less=random.sample(less_dinners, k=amount)
picks_Christine=random.sample(Christine_dinners, k=amount)
picks_Alexa=random.sample(Alexa_dinners, k=amount)

for index,(a,b,c) in enumerate(zip(picks_less, picks_Christine, picks_Alexa)):
    print(f'{index+1} -- less {a}, Christine {b}, Alexa {c}')

