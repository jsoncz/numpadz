import sys, pygame
pygame.mixer.pre_init(44100, 16, 2, 2000)
pygame.init()

size = width, height = 320, 240
speed = [2, 2]
colour = 0, 0, 0

try:
    packs = []
    packs = [line.rstrip('\n') for line in open('wav/packlist.txt')]
    print ("NUMPADZ - Cycle through Packs with + / -")
    print (packs)

except:
    print ("could not open packlist, check you run from the current dir")


selectedPack = 0
p = packs[selectedPack]


screen = pygame.display.set_mode(size)

sounds = [pygame.mixer.Sound("wav/{}/{:04}.wav".format(p, i))
          for i in range(1, 10)]

KEYS = [pygame.K_KP1, pygame.K_KP2, pygame.K_KP3, pygame.K_KP4, pygame.K_KP5,
        pygame.K_KP6, pygame.K_KP7, pygame.K_KP8, pygame.K_KP9]

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        #choose pack
        if (event.type == pygame.KEYDOWN and
                event.key in (pygame.K_KP_PLUS, pygame.K_KP_MINUS)):
            colour
            if event.key == pygame.K_KP_PLUS:
                selectedPack += 1
            elif event.key == pygame.K_KP_MINUS:
                selectedPack -= 1

            try:
                p = packs[selectedPack]
            except IndexError:
                selectedPack = 0
                p = packs[selectedPack]
            print(p)

            sounds = [pygame.mixer.Sound("wav/{}/{:04}.wav".format(p, i))
                      for i in range(1, 10)]

        if event.type in (pygame.KEYDOWN, pygame.KEYUP):
            try:
                key_index = KEYS.index(event.key)
            except ValueError:
                # User didn't press a numpad key, ignore
                pass
            else:
                # User did press a numpad key, process it
                sound = sounds[key_index]
                if event.type == pygame.KEYDOWN:
                    sound.play()
                elif event.type == pygame.KEYUP:
                    sound.stop()

        screen.fill(colour)

        pygame.display.flip()
