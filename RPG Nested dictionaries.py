#RPG Nested Dictionaries WG
#This program will use nested dictionaries to
#describe locations, inventories, and characters.

#characters
"""
This defines the characters and sets them as values and then their traits are set
as values within the dictionary
"""
Characters = {
    'Dorian': {
        'Age': 27,
        'Profession': 'Smuggler',
        'History': 'Born a peasant in The Crows Nest,'
        'he worked his way to the top of the smugglers guild.'
        'He was then hired as a captain to run cargo for the Gold Imperial Fleet',
        'Height': '1.78m',
        'HP': 150
        },
    'Laika': {
        'Age': 22,
        'Profession': 'Marksman',
        'History': 'Born to a weathly family, Laika grew up in luxury,'
        'although that life was abrupt after her parents were killed by'
        'mercernaries, she swore to make a more peaceful world.'
        'She was hired by the Gold Imperial fleet to proctect shipments'
        'from pirates.',
        'Height': '1.59m',
        'HP': 200
        },
    'Ander': {
        'Age': 17,
        'Profession': 'Part of the Crew aboard "The Flying Whale"',
        'History': 'It is unknown where he came from, all that is known'
        'is that he was brought into the Gold Imperial fleet by Dorian. '
        'He is quite a enthusiastic person always ready for another mission',
        'Height': '1.32m',
        'HP': 100
        }
    }

"""
This will print out the characters and any descriptions about them.
"""
for character, chr_info in Characters.items():
    print(f"\nCharcter:{character}")
    age = f"{chr_info['Age']}"
    profession = f"{chr_info['Profession']}"
    history = f"{chr_info['History']}"
    height = f"{chr_info['Height']}"
    hp = f"{chr_info['HP']}"
    print(f"Age:{age}")
    print(f"Profession:{profession}")
    print(f"History:{history}")
    print(f"Height:{height}")
    print(f"HP:{hp}")
    
#Inventory
    
"""
This will set an inventory for the person who plays this tbg
and it will print it out into the console
"""
Inventory = {
    'Wrench': {
        'Details': 'A tool to fix things or a weapon',
        'Damage': 20
        },
    'Canned fruit': {
        'Details': 'Heals 30 hp',
        'Damage': 2
        },
    'Water Canteen': {
        'Details': 'Need it to survive',
        'Damage': 1
        },
    'Pistol': {
        'Details': 'Weapon to shoot, has 20 bullets, takes 3 seconds to reload',
        'Damage': 75
        },
    'Rifle': {
        'Details': 'Weapon to shoot, has 10 bullets, takes 10 seconds to reload',
        'Damage': 120
        },
    'Rapier': {
        'Details': 'A sword for close combat',
        'Damage': 45
        }
    }

for itm, i_info in Inventory.items():
    print(f"\nInventory:{itm}")
    detail = f"{i_info['Details']}"
    damage = f"{i_info['Damage']}"
    print(f"Detail:{detail}")
    print(f"Damage:{damage}")
       
    
"""
This will be the locations and any descriptions about them
"""
Locations = {
    'Iron Steam Island': {
        'details': 'This island is located within the middle of a'
                   'volcano in which there is a lake which creates a'
                   'of steam, it also is the capital of the Gold Imperial Fleet.'
        },
    "Crow's Nest": {
        'details': 'This island is within neutral territory meaning all'
                   'factions are at play here, it is a floating city, in which'
                   'There are many blackmarket deals, or illegal trading.'
        }
    }
for location, loc_info in Locations.items():
    print(f"\nLocation:{location}")
    detail = f"{loc_info['details']}"
    print(f"Details:{detail}")
        
    
    
   

    
        










