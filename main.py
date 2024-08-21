import pygame
import math
import random

width, height = 800, 600
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

pygame.display.set_caption("Procedural Animation")
pygame.init()



def distance_constraint(r, nodes):
    # distance constraint
    for node in range(len(nodes)):
        if node != len(nodes) - 1:
            angle = math.atan2(nodes[node + 1][1] - nodes[node][1],
                               nodes[node + 1][0] - nodes[node][0])
            constrained_pos = (nodes[node][0] + r * math.cos(angle), nodes[node][1] + r * math.sin(angle))
            nodes[node + 1] = constrained_pos


nodes = []
for n in range(100):
    nodes.append((random.randint(0, 800), random.randint(0, 600)))

choice = input("""
Which type of procedural animation would you like to run? 
(Pick a number)
1. Distance Constraint Snake
>> """)

while True:

    mouse_pos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    nodes[0] = mouse_pos

    screen.fill((0, 0, 0))
    if choice == "1":
        distance_constraint(5, nodes)
    for node in nodes:
        if nodes.index(node) == 0:
            pygame.draw.circle(screen, (0, 255, 0), node, 5, 2)
        else:
            pygame.draw.circle(screen, (255, 0, 0), node, 5, 2)
    pygame.display.update()
    clock.tick(60)
