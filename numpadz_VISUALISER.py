import random
import sys, time
import pygame
import asyncio
import threading

from scipy.io.wavfile import read
from numpy import fft

pygame.mixer.pre_init(44100, 16, 4, 2048)
pygame.init()

SIZE = WIDTH, HEIGHT = 320, 240
CENTER = [WIDTH/2, HEIGHT/2]
print (CENTER)
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
WAVFILES = ["wav/{}/{:04}.wav".format(P, i)
            for i in range(1, 10)]
SOUNDS = [pygame.mixer.Sound("wav/{}/{:04}.wav".format(P, i))
          for i in range(1, 10)]
GIFS = [pygame.image.load("gif/{}/{:04}.gif".format(GP, i))
        for i in range(1, 10)]

KEYS = [pygame.K_KP1, pygame.K_KP2, pygame.K_KP3, pygame.K_KP4, pygame.K_KP5,
        pygame.K_KP6, pygame.K_KP7, pygame.K_KP8, pygame.K_KP9]

def get_sounds(PACK):
    return [pygame.mixer.Sound("wav/{}/{:04}.wav".format(PACK, i))
            for i in range(1, 10)]   

# DISPLAY GIF
def image(gif):
    SCREEN.blit(gif, (1, 0))

# GET SAMPLE LENGTHS
def getsamplelen():
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
                get_sounds(P)

            getsamplelen()

        if event.type in (pygame.KEYDOWN, pygame.KEYUP):
            try:
                key_index = KEYS.index(event.key)
            except ValueError:
                # User didn't press a numpad key, ignore
                pass
            else:
                # User did press a numpad key, process it
                WAVFILE = WAVFILES[key_index]
                sound = SOUNDS[key_index]
                gifSel = GIFS[key_index]
                if event.type == pygame.KEYDOWN:
                    sound.play(-1)
                    
                    now = time.time() 
                    frame_rate, amplitude = read(WAVFILE)
                    frame_skip = 96
                    amplitude = amplitude[:,0] + amplitude[:,1]
                    amplitude = amplitude[::frame_skip]
                    frequency = list(abs(fft.fft(amplitude)))
                    print(WAVFILE)
                    # scale the amplitude to 1/4th of the frame HEIGHT and translate it to HEIGHT/2(central line)
                    max_amplitude = max(amplitude)
                    for i in range(len(amplitude)):
                        amplitude[i] = float(amplitude[i])/max_amplitude*HEIGHT/4 + HEIGHT/2
                    amplitude = [int(HEIGHT/2)]*WIDTH + list(amplitude)

                    # visualizer animation starts here
                    for i in range(len(amplitude[WIDTH:])):

                        SCREEN.fill([0, 0, 0])
                        image(gifSel)
                        #circular animation: radius of circle depends on magnitude amplitude and color of circle depends on frequency
                        try:
                            pygame.draw.circle(SCREEN, [(frequency[i]*2)%255, (frequency[i]*3)%255, (frequency[i]*5)%255], [120, 160], amplitude[i], 1)
                        except ValueError:
                            pass
                        # the amplitude graph is being translated from both left and right creating a mirror effect
                        prev_x, prev_y = 0, amplitude[i]
                       
                        #the amplitude graph is being translated from both left and right creating a mirror effect
                        prev_x, prev_y = 0, amplitude[i]
                        for x, y in enumerate(amplitude[i+1:i+1+WIDTH][::5]):
                            pygame.draw.line(SCREEN, [0, 255, 0], [prev_x*5, prev_y], [x*5, y], 1)
                            pygame.draw.line(SCREEN, [0, 255, 0], [(prev_x*5-WIDTH/2)*-1+WIDTH/2, prev_y], [(x*5-WIDTH/2)*-1+WIDTH/2, y], 1)
                            prev_x, prev_y = x, y
                        # time delay to control frame refresh rate
                        frame_rate*frame_skip
                        time.sleep(.00000000001)
                        now = time.time()

                        pygame.display.flip()
                        
                elif event.type == pygame.KEYUP:
                    sound.stop()
                    rc = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
                    SCREEN.fill(rc)
        pygame.display.flip()
