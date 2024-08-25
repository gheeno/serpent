import logging 

logging.basicConfig(level=logging.INFO)

x_increment: int
alien_0: dict = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}

logging.info(f"Initial dictionary : \n {alien_0}")

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else : 
    x_increment = 3

alien_0['x_position'] = alien_0['x_position'] + x_increment
logging.info(f"Updated dictionary : \n {alien_0}")

del alien_0['speed']
logging.info(alien_0)

for keys in alien_0.keys():
    print(keys)


print(list(alien_0.keys())[0])
