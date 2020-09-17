from animals import Penguin
from habitats import Habitat

pingu = Penguin('pingu')

ocean = Habitat('ocean')

ocean.add_animal(pingu)

for animal in ocean.animals:
  print(animal)


print(ocean)