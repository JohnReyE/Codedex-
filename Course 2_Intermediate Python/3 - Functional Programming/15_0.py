import random
from functools import reduce

prefixes = ['Mystic', 'Golden', 'Dark', 'Shadow', 'Silver']
suffixes = ['storm', 'song', 'fire', 'blade', 'whisper']


def capitalize_suffix(name):
    return name.capitalize()

capped_suffix = list(map(capitalize_suffix, suffixes))

def create_fantasy_name(list_1, list_2):
  return random.choice(list_1) + ' ' + random.choice(list_2)

random_names = [
    create_fantasy_name(prefixes, capped_suffix) for name in range(10) 
]

def fire_in_name(name):
    return 'Fire' in name
filtered_names = list(filter(fire_in_name, random_names))

def concatenate_names(name_1, name_2):
    return name_1 + ', ' + name_2

reduced_names = reduce(concatenate_names, filtered_names)

def display_name_info():
    print("Fantasy Names:")
    for name in random_names:
        print(name)
    print()
    print(f"Filtered names with 'Fire': {filtered_names}")
    print(f"Concatenated names: {reduced_names}")

display_name_info()