aliens: list = []
new_alien: dict = {}

for alien_number in range(30):
    new_alien = {
        'color' : 'green',
        'points' : 5,
        'speed' : 'slow'
        }
    aliens.append(new_alien)

for alien in aliens[1]:
    print(alien)

print(f"total number of aliens : {len(aliens)}")