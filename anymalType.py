animal = str(input())

animalType = {
    'dog': 'mammal',
    'crocodile': "reptile",
    'tortoise': "reptile",
    'snake': "reptile",
}

print(animalType.get(animal, "unknown"))
