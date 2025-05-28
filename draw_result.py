import pygame.display
import pygame.time
from answer import right_way
from create_lab import result, size
import pygame

pygame.init()
screen = pygame.display.set_mode(((size + 2) * 25, size * 25 + 60))
done = True

font = pygame.font.SysFont('couriernew', 20)
text = font.render(str('press Enter for result'), True, (255, 255, 255))
screen.blit(text, (20, 20))
clock = pygame.time.Clock()

while done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            for position in right_way[-1::-1]:
                x = position[1] * 21 + 21
                y = position[0] * 21 + 61
                pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(x, y, 19, 19))
                pygame.display.update()
                clock.tick(20)

    pygame.display.flip()
    y = 40
    for line in result:
        x = 0
        y += 21
        for pixel in line:
            x += 21
            if pixel == '#':
                pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(x, y, 19, 19))
