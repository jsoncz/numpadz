import sys, pygame, random
pygame.mixer.pre_init(44100, 16, 4, 2048)
pygame.init()

size = width, height = 320, 240
speed = [2, 2]
colour = 0,0,0
colour2 = 0,0,0

try:
    packs = []
    packs = [line.rstrip('\n') for line in open('wav/packlist.txt')]
    print ("NUMPADZ - Cycle through Packs with + / -")
    print (packs)

except:
    print ("could not open packlist, check you run from the current dir")

#giflist
try:
    gifpacks = []
    gifpacks = [line.rstrip('\n') for line in open('gif/giflist.txt')]
    print ("NUMPADZ - Cycle through GIFS with / and * -")
    print (gifpacks)

except:
    print ("could not open giflist, check you run from the current dir")

#PACK VARIABLES
selectedPack = 0
selectedGifPack = 0
p = packs[selectedPack]
p = packs[selectedPack]
gp = gifpacks[selectedGifPack]

#WINDOW
screen = pygame.display.set_mode(size)
pygame.display.set_caption('NumPADZ')

#FILES
sounds = [pygame.mixer.Sound("wav/{}/{:04}.wav".format(p, i))
          for i in range(1, 10)]
gifs = [pygame.image.load("gif/{}/{:04}.gif".format(gp, i))
          for i in range(1, 10)]

KEYS = [pygame.K_KP1, pygame.K_KP2, pygame.K_KP3, pygame.K_KP4, pygame.K_KP5,
        pygame.K_KP6, pygame.K_KP7, pygame.K_KP8, pygame.K_KP9]


def image(gif):
    image_rect = gif.get_rect().center
    screen.blit(gif,(1,1))

def getSampleLen():
#get sample lengths
    
    for i in sounds:
        smpLen = round(i.get_length(),1)
        print ("Num",sounds.index(i)+1,"-",smpLen) 

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.KEYDOWN:

            #STOP ALL SOUNDS IF ZERO PRESSED
            if event.key == pygame.K_KP0:
                    print("stopping all sounds with Num Zero")
                    pygame.mixer.stop()

            #SELECT GIFPACK WITH * AND /
            if event.key == pygame.K_KP_MULTIPLY:
                try:
                    selectedGifPack += 1
                    gp = gifpacks[selectedGifPack]
                    print(gp)
                except (IndexError):
                    selectedGifPack = 0
                    gp = gifpacks[selectedGifPack]
                    print(gp)
                gifs = [pygame.image.load("gif/{}/{:04}.gif".format(gp, i))
                        for i in range(1, 10)]


            if event.key == pygame.K_KP_DIVIDE:
                try:
                    selectedGifPack -= 1
                    gp = gifpacks[selectedGifPack]
                    print(gp)
                except (IndexError):
                    selectedGifPack = 0
                    gp = gifpacks[selectedGifPack]
                    print(gp)
                gifs = [pygame.image.load("gif/{}/{:04}.gif".format(gp, i))
                        for i in range(1, 10)]
                
        #CHOOSE SAMPLEPACK
        if (event.type == pygame.KEYDOWN and
                event.key in (pygame.K_KP_PLUS, pygame.K_KP_MINUS)):

            if event.key == pygame.K_KP_PLUS:
                try:
                    selectedPack += 1
                    p = packs[selectedPack]
                    print(p)
                except IndexError:
                    selectedPack = 0
                    p = packs[selectedPack]
                    print(p)
                sounds = [pygame.mixer.Sound("wav/{}/{:04}.wav".format(p, i))
                      for i in range(1, 10)]
               

            elif event.key == pygame.K_KP_MINUS:
                try:
                    selectedPack -= 1
                    p = packs[selectedPack]
                    print(p)
                except IndexError:
                    selectedPack = 0
                    p = packs[selectedPack]
                    print(p)
                sounds = [pygame.mixer.Sound("wav/{}/{:04}.wav".format(p, i))
                      for i in range(1, 10)]
           
            
            getSampleLen()

        if event.type in (pygame.KEYDOWN, pygame.KEYUP):
            try:
                key_index = KEYS.index(event.key)
            except ValueError:
                # User didn't press a numpad key, ignore
                pass
            else:
                # User did press a numpad key, process it
                sound = sounds[key_index]
                gifSel = gifs[key_index]
                if event.type == pygame.KEYDOWN:
                    sound.play(-1)
                    image(gifSel)
                                  
               
                elif event.type == pygame.KEYUP:
                    sound.stop()
                    colour = random.randint(0,255),random.randint(0,255),random.randint(0,255)
                    screen.fill(colour) 

                    
                
        pygame.display.flip()

   