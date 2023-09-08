# Pokédex 📟
# Codédex

# Class definition
class Pokemon:
  def __init__(self, name, type, description, level, region, is_caught):
    self.name = name
    self.type = type
    self.description = description
    self.level = level
    self.region = region
    self.is_caught = is_caught

  def speak(self):
    print(self.name + ' made a sound!')
  
  def display_details(self):
    print('Name: ' + self.name)

    if len(self.type) == 1:
      print('Type: ' + self.type[0])
    else:
      print('Type: ' + self.type[0] + '/' + self.type[1])
    
    print('Lv. ' + str(self.level))
    print('Region: ' + self.region)
    print('Description: ' + self.description)

    if self.is_caught:
      print(self.name + ' has already been caught!')
    else:
      print(self.name + ' hasn\'t been caught yet.')

# Pokémon objects
pikachu = Pokemon('Pikachu', ['Electric'], 'It has small electric sacs on both its cheeks. If threatened, it looses electric charges from the sacs.', 25, 'Kanto', True)
charizard = Pokemon('Charizard', ['Fire', 'Flying'], 'It spits fire that is hot enough to melt boulders. It may cause forest fires by blowing flames.', 36, 'Kanto', False)
gyarados = Pokemon('Gyarados', ['Water', 'Flying'], 'It has an extremely aggressive nature. The HYPER BEAM it shoots from its mouth totally incinerates all targets.', 57, 'Kanto', False)
