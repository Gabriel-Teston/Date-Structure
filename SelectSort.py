import pygame
import random
import sys

"""Global variables"""

collor = ((255, 255, 255), (0, 0, 0))

"""Screen setup"""

resolution = (1300, 700)
windowSurface = pygame.display.set_mode(resolution, 0, 32)
pygame.display.set_caption("Waiting...")
windowSurface.fill(collor[0])

""""Screen update function"""


def update():
    windowSurface.fill(collor[0])
    for h in range(len(vetor)):
        d = resolution[1] / max(vetor)
        x0 = ((resolution[0] - 5) / (len(vetor) * 1.0)) * h + 2
        x1 = ((resolution[0] - 5) / (len(vetor) * 1.0)) * (h + 1)
        y0 = (resolution[1] - vetor[h] * d)
        y1 = (resolution[1] - 1)
        pygame.draw.polygon(windowSurface, collor[1], ((x0, y0), (x1, y0), (x1, y1), (x0, y1)))
    pygame.display.update()


""""Execution loop"""

while 1:
    vetor = []
    temp = []
    ready = 0
    repeat = 0
    windowSurface.fill(collor[0])
    pygame.display.update()
    while ready == 0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_0:
                    temp.append('0')
                elif event.key == pygame.K_1:
                    temp.append('1')
                elif event.key == pygame.K_2:
                    temp.append('2')
                elif event.key == pygame.K_3:
                    temp.append('3')
                elif event.key == pygame.K_4:
                    temp.append('4')
                elif event.key == pygame.K_5:
                    temp.append('5')
                elif event.key == pygame.K_6:
                    temp.append('6')
                elif event.key == pygame.K_7:
                    temp.append('7')
                elif event.key == pygame.K_8:
                    temp.append('8')
                elif event.key == pygame.K_9:
                    temp.append('9')
                elif event.key == pygame.K_SPACE:
                    vetor.append(int("".join(temp)))
                    temp = []
                elif event.key == pygame.K_RETURN:
                    ready = 1
                elif event.key == pygame.K_r:
                    vetor = range(200)
                    random.shuffle(vetor)
                    ready = 1
    pygame.display.set_caption("Sorting...")
    update()
    for i in xrange(len(vetor)):
        m = vetor[i]
        pos = i
        for j in xrange(i + 1, len(vetor)):
            if vetor[j] < m:
                m = vetor[j]
                pos = j
        vetor[pos] = vetor[i]
        vetor[i] = m
        update()
    pygame.display.set_caption("Done!")
    while repeat == 0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    repeat = 1
