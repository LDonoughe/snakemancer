print (
'''
 __             _                                            
/ _\_ __   __ _| | _____ _ __ ___   __ _ _ __   ___ ___ _ __ 
\ \| '_ \ / _` | |/ / _ \ '_ ` _ \ / _` | '_ \ / __/ _ \ '__|
_\ \ | | | (_| |   <  __/ | | | | | (_| | | | | (_|  __/ |   
\__/_| |_|\__,_|_|\_\___|_| |_| |_|\__,_|_| |_|\___\___|_|   
'''
)

class Snake:
  def __init__(self, name: str, venomous: bool, size: int):
        self.name = name
        self.venomous = venomous
        self.size = size

print('Assemble Your Snake')
print('Is it venomous?')
venom = input()
print('How big is it (in centimeters)?')
size = int(input())
# Probably should replace with just checking the first letter
venomous = venom.lower() in ['true', 'tru', 'truuu', '1', 't', 'y', 'yes', 'yeah', 'yeah buddy', 'fa sho', 'yup']
print_venom = '' if venomous else 'not '
print(f'Your snake is {print_venom}venomous and {size} meters')
print('What would you like to name your snake?')
name = input()
snake = Snake(name, venomous, size)
print(f'{name}\'s reference is {snake}')



class Store:
  pass



class Snakemancer:
  pass
                                                             
class Mission:
  pass                                                        