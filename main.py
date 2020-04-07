from random import uniform

print (
'''
 __             _                                            
/ _\_ __   __ _| | _____ _ __ ___   __ _ _ __   ___ ___ _ __ 
\ \| '_ \ / _` | |/ / _ \ '_ ` _ \ / _` | '_ \ / __/ _ \ '__|
_\ \ | | | (_| |   <  __/ | | | | | (_| | | | | (_|  __/ |   
\__/_| |_|\__,_|_|\_\___|_| |_| |_|\__,_|_| |_|\___\___|_|   
'''
)

class Snakemancer:
  def __init__(self, snakes):
    self.snakes = snakes

  def add_snake(self, snake):
      self.snakes = self.snakes.append(snake)

user = Snakemancer([])

class Store:
  pass

class Snake:
  def __init__(self, name: str, venomous: bool, size: int):
        self.name = name
        self.venomous = venomous
        self.size = size

class Mission:
  def __init__(self, difficulty: int):
    self.difficulty = difficulty

  def attempt(self, snake: Snake):
    skill = max(100 - snake.size, 0)
    luck = uniform(-20,20)
    return 'success' if skill > (self.difficulty + luck) else 'failure'


print('Assemble Your Snake')
print('Is it venomous?')
venom = input()
print('How big is it (in centimeters)?')
size = int(input())
# Probably should replace with just checking the first letter
venomous = venom.lower() in ['true', 'tru', 'truuu', '1', 't', 'y', 'yes', 'yeah', 'yeah buddy', 'fa sho', 'yup']
print_venom = '' if venomous else 'not '
print(f'Your snake is {print_venom}venomous and {size} centimeters')
print('What would you like to name your snake?')
name = input()
snake = Snake(name, venomous, size)
user.add_snake(snake)

difficulty = 0
failure = False
while (difficulty < 101 and failure != True):
  mission = Mission(difficulty)
  print(f'You must infiltrate the building. It has a difficulty of {mission.difficulty}')
  result = mission.attempt(snake)
  print(f'Mission is a {result}')
  if result == 'failure':
    failure = True
  difficulty += 10

if failure:
  print('Your snake failed the mission, try again later with a better snake')
# print(user.snakes)

                                                             
                                                    