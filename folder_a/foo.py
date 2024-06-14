"""
Placeholder for real work
"""

pets = ["Magnus", "Beau", "Chicken Nugget"]
pet_types = ["rabbit", "rabbit", "cat"]

pet_structs = [{"name": item[0], "type": item[1]} for item in zip(pets, pet_types)]

print(pet_structs)

