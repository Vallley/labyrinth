import pygame.display
from create_lab import result, size
import pygame

pygame.init()
screen = pygame.display.set_mode((size * 25, size * 25))
done = True
while done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False
    pygame.display.flip()
    y = 0
    for line in result:
        x = 0
        y += 21
        for pixel in line:
            x += 21
            if pixel == '#':
                pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(x, y, 20, 20))
