import random
import sys
import pygame


pygame.mixer.pre_init(44100, 16, 4, 2048)
pygame.init()

SIZE = WIDTH, HEIGHT = 320, 240

try:
    PACKS = []
    PACKS = [line.rstrip('\n') for line in open('wav/packlist.txt')]
    print("NUMPADZ - Cycle through PACKS with + / -")
    print(PACKS)
except IOError:
    print("could not open packlist, check you run from the current dir")
    sys.exit()

# GIFLIST
try:
    GIFPACKS = []
    GIFPACKS = [line.rstrip('\n') for line in open('gif/giflist.txt')]
    print("NUMPADZ - Cycle through GIFS with / and * -")
    print(GIFPACKS)
except IOError:
    print("could not open giflist, check you run from the current dir")

# PACK VARIABLES
SELECTEDPACK = 0
SELECTEDGIFPACK = 0
P = PACKS[SELECTEDPACK]
P = PACKS[SELECTEDPACK]
GP = GIFPACKS[SELECTEDGIFPACK]

# WINDOW
SCREEN = pygame.display.set_mode(SIZE)
pygame.display.set_caption('NumPADZ')

# FILES
SOUNDS = [pygame.mixer.Sound("wav/{}/{:04}.wav".format(P, i))
          for i in range(1, 10)]
GIFS = [pygame.image.load("gif/{}/{:04}.gif".format(GP, i))
        for i in range(1, 10)]

KEYS = [pygame.K_KP1, pygame.K_KP2, pygame.K_KP3, pygame.K_KP4, pygame.K_KP5,
        pygame.K_KP6, pygame.K_KP7, pygame.K_KP8, pygame.K_KP9]


def image(gif):
    SCREEN.blit(gif, (1, 0))


def getsamplelen():
    # GET SAMPLE LENGTHS
    for i in SOUNDS:
        samplelength = round(i.get_length(), 1)
        print("Num", SOUNDS.index(i) + 1, "-", samplelength)

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.KEYDOWN:

            # STOP ALL SOUNDS IF ZERO PRESSED
            if event.key == pygame.K_KP0:
                print("stopping all SOUNDS with Num Zero")
                pygame.mixer.stop()

            # SELECT GIFPACK WITH * AND /
            if event.key == pygame.K_KP_MULTIPLY:
                SELECTEDGIFPACK += 1
                try:
                    GP = GIFPACKS[SELECTEDGIFPACK]
                except IndexError:
                    SELECTEDGIFPACK = 0
                    GP = GIFPACKS[SELECTEDGIFPACK]
                print(GP)

                GIFS = [pygame.image.load("gif/{}/{:04}.gif".format(GP, i))
                        for i in range(1, 10)]

            if event.key == pygame.K_KP_DIVIDE:
                SELECTEDGIFPACK -= 1
                try:
                    GP = GIFPACKS[SELECTEDGIFPACK]
                except IndexError:
                    SELECTEDGIFPACK = 0
                    GP = GIFPACKS[SELECTEDGIFPACK]
                print(GP)
                GIFS = [pygame.image.load("gif/{}/{:04}.gif".format(GP, i))
                        for i in range(1, 10)]
        # CHOOSE SAMPLEPACK
        if (event.type == pygame.KEYDOWN and
                event.key in (pygame.K_KP_PLUS, pygame.K_KP_MINUS)):

            if event.key == pygame.K_KP_PLUS:
                SELECTEDPACK += 1
                try:
                    P = PACKS[SELECTEDPACK]
                except IndexError:
                    SELECTEDPACK = 0
                    P = PACKS[SELECTEDPACK]
                print(P)
                SOUNDS = [pygame.mixer.Sound("wav/{}/{:04}.wav".format(P, i))
                          for i in range(1, 10)]

            elif event.key == pygame.K_KP_MINUS:
                SELECTEDPACK -= 1
                try:
                    P = PACKS[SELECTEDPACK]
                except IndexError:
                    SELECTEDPACK = 0
                    P = PACKS[SELECTEDPACK]
                    print(P)
                SOUNDS = [pygame.mixer.Sound("wav/{}/{:04}.wav".format(P, i))
                          for i in range(1, 10)]

            getsamplelen()

        if event.type in (pygame.KEYDOWN, pygame.KEYUP):
            try:
                key_index = KEYS.index(event.key)
            except ValueError:
                # User didn't press a numpad key, ignore
                pass
            else:
                # User did press a numpad key, process it
                sound = SOUNDS[key_index]
                gifSel = GIFS[key_index]
                if event.type == pygame.KEYDOWN:
                    sound.play(-1)
                    image(gifSel)
                elif event.type == pygame.KEYUP:
                    sound.stop()
                    colour = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
                    SCREEN.fill(colour)
        pygame.display.flip()
