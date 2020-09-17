from animals import Penguin, PaintedDog
from habitats import Habitat, Aquarium

pingu = Penguin('pingu')
dog = PaintedDog('ralph')

ocean = Aquarium('ocean')

ocean.add_swimmer_type_check(pingu)
ocean.add_swimmer_type_check(dog)

for animal in ocean.animals:
  print(animal)

