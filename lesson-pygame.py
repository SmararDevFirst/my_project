import pygame
import math
import random

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption(' ')
'''
player = {'x': 400.0, 'y': 300.0, 'radius': 30, 'speed': 4.0}
enemy = {'x': 600.0, 'y': 450.0, 'radius': 30, 'speed': 2.0}

clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    dx, dy = 0, 0

    if keys[pygame.K_LEFT]:
        dx -= 1
    if keys[pygame.K_RIGHT]:
        dx += 1
    if keys[pygame.K_UP]:
        dy -= 1
    if keys[pygame.K_DOWN]:
        dy += 1

    if dx != 0 or dy != 0:
        dist = math.hypot(dx, dy)
        player['x'] += (dx / dist) * player['speed']
        player['y'] += (dy / dist) * player['speed']

    if player['x'] < -player['radius']:
        player['x'] = 800 + player['radius']
    elif player['x'] > 800 + player['radius']:
        player['x'] = -player['radius']

    if player['y'] < -player['radius']:
        player['y'] = 600 + player['radius']
    elif player['y'] > 600 + player['radius']:
        player['y'] = -player['radius']

    distance_x = player['x'] - enemy['x']
    distance_y = player['y'] - enemy['y']
    distance_to_player = math.hypot(distance_x, distance_y)

    if distance_to_player > 0:
        enemy['x'] += (distance_x / distance_to_player) * enemy['speed']
        enemy['y'] += (distance_y / distance_to_player) * enemy['speed']

    if distance_to_player <= player['radius'] + enemy['radius']:
        running = False
        print('Поймал!')

    screen.fill((0, 0, 0))

    pygame.draw.circle(screen, (255, 0, 0), (int(player['x']), int(player['y'])), player['radius'])
    pygame.draw.circle(screen, (0, 0, 255), (int(enemy['x']), int(enemy['y'])), enemy['radius'])

    pygame.display.flip()
    clock.tick(60)

pygame.quit()

clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))

    seconds_need = pygame.time.get_ticks() // 1000 % 6

    pygame.draw.circle(screen, (100, 0, 0), (400, 200), 35)
    pygame.draw.circle(screen, (100, 100, 0), (400, 300), 35)
    pygame.draw.circle(screen, (0, 100, 0), (400, 400), 35)

    if seconds_need < 3:
        pygame.draw.circle(screen, (255, 0, 0), (400, 200), 50)
    elif seconds_need < 5:
        pygame.draw.circle(screen, (255, 255, 0), (400, 300), 50)
    else:
        pygame.draw.circle(screen, (0, 255, 0), (400, 400), 50)

    pygame.display.flip()
    clock.tick(60)
'''
a = []
for _ in range(100):
    a.append(
        {'x': random.randint(0, 800),
              'r': random.randint(10, 40),
              's': random.randint(1, 8),
              'y': random.randint(0, 600)}
    )



clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))

    for i in a:
        pygame.draw.circle(screen, (255, 255, 255), (i['x'], i['y']), i['r'])
        i['y'] += i['s']
        if i['y'] > 600 + i['r']:
            i['y'] = -i['r']
            i['x'] = random.randint(0, 800)

    pygame.display.flip()
    clock.tick(60)