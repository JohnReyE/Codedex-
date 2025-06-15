class Pokemon:
  def __init__(self, entry, name, types, description, is_caught):
    self.entry = entry
    self.name = name
    self.types = types
    self.description = description
    self.is_caught = is_caught

  def speak(self):
    print(f"{self.name}, {self.name}")
  
  def display_details(self):
    print(f"Entry No.: {self.entry}")
    print(f"Name: {self.name}")
    print(f"Types: {self.types}")   
    print(f"Description: {self.description}")
    
    if self.is_caught:
      print(f"{self.name} has already been caught!")
    else:
      print(f"{self.name} hasn't been caught yet.")

charizard = Pokemon(6, "Charizard", "Fire / Flying", "Charizard flies around the sky in search of powerful opponents. It breathes intense flames that can melt anything and is known for its fierce battle spirit and loyalty to strong trainers.", True)
gyarados = Pokemon(130, "Gyarados", "Water / Flying", "Once a weak Magikarp, Gyarados undergoes a dramatic transformation and becomes a ferocious sea serpent. Its rage knows no bounds, and it's feared for its destructive rampages during storms.", False)
lucario = Pokemon(448, "Lucario", "Fighting / Steel", "Lucario can sense and manipulate aura, a form of life energy. It’s highly intelligent and often regarded as a noble warrior Pokémon that understands human speech and emotions.", True)

charizard.speak()
gyarados.speak()
lucario.speak()

charizard.display_details()