import random
import sys
import pygame
import time

pygame.mixer.pre_init(44100, 16, 16, 1024)
pygame.mixer.init()

start = time.time()

SIZE = WIDTH, HEIGHT = 320, 300
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 185, 55)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

speed = 5

POS = 1
lastpos = []
key_indexs = []
recpack = []
reclen = []
reckey = []
record = False
play = True
clock = pygame.time.Clock()


try:
    PACKS = []
    PACKS = [line.rstrip('\n') for line in open('wav/packlist.txt')]
    print("NUMPADZ - Cycle through PACKS with + / -")
    print(PACKS)
except IOError:
    print("could not open packlist, check you run from the current dir")
    sys.exit()

# PACK VARIABLES
SELECTEDPACK = 0
SELECTEDGIFPACK = 0
P = PACKS[SELECTEDPACK]
P = PACKS[SELECTEDPACK]

# WINDOW
SCREEN = pygame.display.set_mode(SIZE)
pygame.display.set_caption('NumPADZ')
SCREEN.set_alpha(None)
logo = pygame.image.load("logo.png").get_rect()
logosurface = pygame.Surface((logo.width, logo.height))
logosurface.blit(pygame.image.load("logo.png"), logo)


# FILES
SOUNDS = [pygame.mixer.Sound("wav/{}/{:04}.wav".format(P, i))
          for i in range(1, 10)]

KEYS = [pygame.K_KP1, pygame.K_KP2, pygame.K_KP3, pygame.K_KP4, pygame.K_KP5,
        pygame.K_KP6, pygame.K_KP7, pygame.K_KP8, pygame.K_KP9]
key_index = 0

def get_sounds(P):
    return [pygame.mixer.Sound("wav/{}/{:04}.wav".format(P, i))
            for i in range(1, 10)]

def getsamplelen():
    # GET SAMPLE LENGTHS
    for i in SOUNDS:
        samplelength = round(i.get_length(), 1)
        print("Num", SOUNDS.index(i) + 1, "-", samplelength)

def grid():
    W=int(18-speed)
    H=20
    MARGIN=15-speed
    SCREEN.fill(BLACK)
    for column in range(5+MARGIN,300,W+MARGIN):
        pygame.draw.rect(SCREEN,WHITE, [column,0+MARGIN,W,H])
        for row in range(0+MARGIN,150,W+MARGIN):
            pygame.draw.rect(SCREEN,WHITE,[column,row,W,H])

def drawsound(key_index):
    if record or play:
        for i in range(len(lastpos)):
            keypos = key_indexs[i]*20
            try:
                soundrect = pygame.draw.rect(SCREEN,COLOUR,[lastpos[i],keypos,reclen[i]*(speed*30),10])
            except IndexError:
                pass

def get_rect(self):
    return pygame.Rect(self.x, self.y, self.width, self.height)

def playrecording():
    for i in range(len(recpack)):
        try:
            recsnd = pygame.mixer.Sound("wav/{}/{:04}.wav".format(recpack[i], reckey[i]))
            if POS == lastpos[i]:
                ms = int(reclen[i]*1000)
                recsnd.play(-1,maxtime=ms)
        except IndexError:
            pass

while 1:
    if record:
        COLOUR = RED
    else:
        COLOUR = GREEN
    POS+=speed
    clock.tick(25)


    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.KEYDOWN:
            # SET RECORD ON/OFF
            if event.key == pygame.K_NUMLOCK:
                if record:
                    record = False
                    print ("STOPPED RECORDING")
                    pygame.mixer.stop()
                else:
                    record = True
                    play = True
                    print ("STARTED RECORDING")


            # STOP ALL SOUNDS IF ZERO PRESSED
            if event.key == pygame.K_KP0:
                print("stopping all SOUNDS with Num Zero")
                pygame.mixer.quit()
                pygame.mixer.pre_init(44100, 16, 16, 1024)
                pygame.mixer.init()

            if event.key == pygame.K_KP_MULTIPLY:
                try:
                    del lastpos[-1]
                    del key_indexs[-1]
                    del recpack[-1]
                    del reclen[-1]
                    del reckey[-1]
                except IndexError:
                    pass

            #SPEED CONTROL
            if event.key == pygame.K_PAGEUP:
                if speed <= 5:
                    speed+=1                   
                else:
                    print("Speed is at maximum:",speed)
                print("Speed:",speed)
            if event.key == pygame.K_PAGEDOWN:
                if speed >= 3:
                    speed-=1
                else:
                    print("Speed is at minimum:",speed)
                print("Speed:",speed)

            #SAMPLE HOLD
            if event.key == pygame.K_KP_ENTER:
                SOUNDS = get_sounds(P)

            #CLEAR RECORDING
            if event.key == pygame.K_KP_PERIOD:
                try:
                    lastpos = []
                    key_indexs = []
                    recpack = []
                    reclen = []
                    reckey = []
                except IndexError:
                    pass
            #PLAYBACK MODE
            if event.key == pygame.K_KP_DIVIDE:
                if play:
                    play = False
                else:
                    play = True
                    record = False
                print("Playback Mode:",play)
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
                SOUNDS = get_sounds(P)
            elif event.key == pygame.K_KP_MINUS:
                SELECTEDPACK -= 1
                try:
                    P = PACKS[SELECTEDPACK]
                except IndexError:
                    SELECTEDPACK = 0
                    P = PACKS[SELECTEDPACK]
                SOUNDS = get_sounds(P)
            print(P)
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
                if event.type == pygame.KEYDOWN:
                    curpos = POS
                    if record:
                        lastpos.append(curpos)
                        key_indexs.append(key_index)
                        smptimepos = time.time()
                        smpstarted = smptimepos - start
                    sound.play(-1)
                    smpstart = time.time()

                if event.type == pygame.KEYUP:
                    sound.stop()
                    smpstop = time.time()
                    if record:
                        recpack.append(P)
                        reclen.append(round(smpstop - smpstart,2))
                        reckey.append(key_index+1)
    pygame.event.pump()
    grid()
    if POS <= WIDTH:
        curpos = POS
        pygame.draw.rect(SCREEN, COLOUR, [curpos,3,5,180])
    else:
        POS = 0
    drawsound(key_indexs)
    if play:
        playrecording()
    #SCREEN.blit(logo, (1,170))
    SCREEN.blit(logosurface, (2,170))
    pygame.display.flip()
