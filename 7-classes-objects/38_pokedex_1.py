# Pokédex 📟
# Codédex

# Class definition
class Pokemon:
  def __init__(self, entry, name, types, description, is_caught):
    self.entry = entry
    self.name = name
    self.types = types
    self.description = description
    self.is_caught = is_caught

  def speak(self):
    print(self.name + ', ' + self.name + '!')
  
  def display_details(self):
    print('Entry Number: ' + str(self.entry))
    print('Name: ' + self.name)

    if len(self.types) == 1:
      print('Type: ' + self.types[0])
    else:
      print('Type: ' + self.types[0] + '/' + self.types[1])
    
    print('Description: ' + self.description)

    if self.is_caught:
      print(self.name + ' has already been caught!')
    else:
      print(self.name + ' hasn\'t been caught yet.')

# Pokémon objects
pikachu = Pokemon(25, 'Pikachu', ['Electric'], 'It has small electric sacs on both its cheeks. If threatened, it looses electric charges from the sacs.', True)
charizard = Pokemon(3, 'Charizard', ['Fire', 'Flying'], 'It spits fire that is hot enough to melt boulders. It may cause forest fires by blowing flames.', False)
gyarados = Pokemon(130, 'Gyarados', ['Water', 'Flying'], 'It has an extremely aggressive nature. The HYPER BEAM it shoots from its mouth totally incinerates all targets.', False)
bulbasaur = Pokemon(1, 'Bulbasaur', ['Grass', 'Poison'], 'A strange seed was planted on its back at birth. The plant sprouts and grows with this Pokemon.', True)
squirtle = Pokemon(7, 'Squirtle', ['Water'], 'When it retracts its long neck into its shell, it squirts out water with vigorous force.', True)
dragonite = Pokemon(149, 'Dragonite', ['Dragon', 'Flying'], 'It can circle the globe in just 16 hours. A kindhearted Pokemon, it leads lost and foundering ships in a storm to the safety of land.', False)

pikachu.speak()
charizard.speak()
gyarados.speak()
bulbasaur.speak()
squirtle.speak()
dragonite.speak()
