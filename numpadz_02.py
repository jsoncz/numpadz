"""
NumpadZ is written and maintained by Jason Byers aka jsoncz / smjase.

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

import sys
import pygame
import time
from threading import Thread

pygame.mixer.pre_init(44100, 16, 16, 2048)
pygame.mixer.init()

start = time.time()

SIZE = WIDTH, HEIGHT = 320, 300
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 185, 55)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

#OPTIONS
speed = 10
quantize = True


POS = 1
startloop = 0
lastpos = []
key_indexs = []
recpack = []
reclen = []
reckey = []
record = False
play = True
playbackrun = True
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
try:
    logosurface.blit(pygame.image.load("logo.png"), logo)
except pygame.error:
    pass
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
    W=18
    H=14
    MARGIN=8
    SCREEN.fill(BLACK)
    for column in range(startloop+MARGIN,WIDTH+MARGIN,W+MARGIN):
        pygame.draw.rect(SCREEN,WHITE, [column,MARGIN,W,H])
        for row in range(MARGIN,165,W+2):
            pygame.draw.rect(SCREEN,WHITE,[column,row,W,H])

def drawsound(key_index):
    if play:
        for i in range(len(lastpos)):
            

            try:
                 #keypos is which row to draw on
                keypos = key_indexs[i]*20
                soundrect = pygame.draw.rect(SCREEN,COLOUR,[lastpos[i],keypos,reclen[i]*(speed*30),10])
            except IndexError:
                pass

def get_rect(self):
    return pygame.Rect(self.x, self.y, self.width, self.height)

def playrecording():
    if play and playbackrun:
        for i in range(len(recpack)):
            try:
                recsnd = pygame.mixer.Sound("wav/{}/{:04}.wav".format(recpack[i], reckey[i]))
                if POS == lastpos[i]:
                    ms = int(reclen[i]*1000)
                    recsnd.play(-1,maxtime=ms)
            except IndexError:
                pass

def round_down(num, divisor):
    return num - (num%divisor)

def stopsounds():
    pygame.mixer.quit()
    pygame.mixer.pre_init(44100, 16, 16, 2048)
    pygame.mixer.init()

while 1:
    if record:
        COLOUR = RED
    else:
        COLOUR = GREEN
    if playbackrun:
        POS+=speed
    clock.tick(30)


    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.KEYDOWN:
            # SET RECORD ON/OFF
            if event.key == pygame.K_NUMLOCK:
                if record:
                    record = False

                    print ("STOPPED RECORDING")

                else:
                    record = True
                    play = True
                    print ("STARTED RECORDING")

            #PLAYBACK RUNNING / SCROBBLE
            if event.key == pygame.K_LEFT:
                if not playbackrun:
                    POS-=speed
                    if POS <= 1:
                        POS = WIDTH
            if event.key == pygame.K_RIGHT:
                if not playbackrun:
                    POS+=speed
                    if POS >= WIDTH:
                        POS = 0



            if event.key == pygame.K_HOME:
                if playbackrun:
                    playbackrun = False
                    stopsounds()
                else:
                    playbackrun = True
                print("Playback running:", playbackrun)


            # STOP ALL SOUNDS IF ZERO PRESSED
            if event.key == pygame.K_KP0:
                print("Stopping all SOUNDS with Num Zero")
                stopsounds()

            if event.key == pygame.K_KP_MULTIPLY:
                try:
                    del lastpos[-1]
                    del key_indexs[-1]
                    del recpack[-1]
                    del reclen[-1]
                    del reckey[-1]
                except IndexError:
                    pass

            #SPEED CONTROL / EXPERIMENTAL STARTLOOP
            if event.key == pygame.K_PAGEUP:
                if startloop <= 100:
                    startloop+=10
                    print("StartLoop set:",startloop)
           
            if event.key == pygame.K_PAGEDOWN:
                if startloop >= 10:
                    startloop-=10
                    print("StartLoop set:",startloop)
               
            if event.key == pygame.K_INSERT:
                if speed <= 20:
                    speed+=5
                else:
                    print("Speed is at maximum:",speed)

            if event.key == pygame.K_DELETE:
                if speed >= 10:
                    speed-=5
                else:
                    print("Speed is at minimum:",speed)

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
                    record = False
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
                        
                        #QUANTIZE But I don't know what I'm thinking...
                        #if curpos is not a multiple of speed then shift the stored position to nearest multiple of speed.
                        if quantize:
                            print(curpos)
                            print(curpos%speed)
                            if not curpos%speed:
                                print(curpos)
                                #in quantize mode, if you hit a sample right near the end, shift it to beginning
                                if curpos >= 309:
                                    curpos = startloop
                                qpos = round_down(curpos,speed)
                                print("position rounded down:", qpos)
                                lastpos.append(qpos)
                                print("position added:",lastpos[-1])
                            
                            else:
                                lastpos.append(curpos)
                        else:
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
    t1 = Thread(target=grid())
    t1.start()
    if POS <= WIDTH:
        curpos = POS
        rects = pygame.draw.rect(SCREEN, COLOUR, [curpos,3,5,180])
    else:
        POS = startloop
    drawsound(key_indexs)
    t = Thread(target=playrecording())
    t.start()
    #SCREEN.blit(logo, (1,170))
    SCREEN.blit(logosurface, (2,170))
    pygame.display.update()
