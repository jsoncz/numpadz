import sys, pygame, random, time
from scipy.io.wavfile import read
from numpy import fft
pygame.mixer.pre_init(44100, 16, 2, 2048)
pygame.init()
pygame.font.init() 

now = time.time()
    
#window 
size = width, height = 320, 240
pygame.display.set_caption('NumPADZ')
screen = pygame.display.set_mode(size)


#font and timer
font = pygame.font.SysFont(None, 25)
textsurface = font.render("smp time:",True, (50, 50, 50))

#colours and shapes
speed = [2, 2]
colour = random.randint(0,255),random.randint(0,255),random.randint(0,255)
colour2 = random.randint(0,255),random.randint(0,255),random.randint(0,255)
rectS = 0


#load packfile
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

selectedPack = 0
selectedGifPack = 0
p = packs[selectedPack]
gp = gifpacks[selectedGifPack]

a = pygame.mixer.Sound("wav/"+p+"/0001.wav")
b = pygame.mixer.Sound("wav/"+p+"/0002.wav")
c = pygame.mixer.Sound("wav/"+p+"/0003.wav")
d = pygame.mixer.Sound("wav/"+p+"/0004.wav")
e = pygame.mixer.Sound("wav/"+p+"/0005.wav")
f = pygame.mixer.Sound("wav/"+p+"/0006.wav")
g = pygame.mixer.Sound("wav/"+p+"/0007.wav")
h = pygame.mixer.Sound("wav/"+p+"/0008.wav")
i = pygame.mixer.Sound("wav/"+p+"/0009.wav")

#GIFS
gifa = pygame.image.load("gif/"+gp+"/0001.gif")
gifb = pygame.image.load("gif/"+gp+"/0002.gif")
gifc = pygame.image.load("gif/"+gp+"/0003.gif")
gifd = pygame.image.load("gif/"+gp+"/0004.gif")
gife = pygame.image.load("gif/"+gp+"/0005.gif")
giff = pygame.image.load("gif/"+gp+"/0006.gif")
gifg = pygame.image.load("gif/"+gp+"/0007.gif")
gifh = pygame.image.load("gif/"+gp+"/0008.gif")
gifi = pygame.image.load("gif/"+gp+"/0009.gif")

print(gp)
#files
files = [("wav/{}/{:04}.wav".format(p, j))
for j in range(1, 10)]

#display gif
def image(gif):
	image_rect = gif.get_rect().center


	screen.blit(gif,(1,1))
	


while 1:
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit()
		#choose pack
		if event.type == pygame.KEYDOWN:
			colour = random.randint(0,255),random.randint(0,255),random.randint(0,255)
			colour2 = random.randint(0,255),random.randint(0,255),random.randint(0,255)
			
			if event.key == pygame.K_KP_MULTIPLY:
				try:
					selectedGifPack += 1
					gp = gifpacks[selectedGifPack]
					print(gp)
				except (ValueError,IndexError) as e:
					selectedGifPack = 0
					gp = gifpacks[selectedGifPack]
					print(gp)

				gifa = pygame.image.load("gif/"+gp+"/0001.gif")
				gifb = pygame.image.load("gif/"+gp+"/0002.gif")
				gifc = pygame.image.load("gif/"+gp+"/0003.gif")
				gifd = pygame.image.load("gif/"+gp+"/0004.gif")
				gife = pygame.image.load("gif/"+gp+"/0005.gif")
				giff = pygame.image.load("gif/"+gp+"/0006.gif")
				gifg = pygame.image.load("gif/"+gp+"/0007.gif")
				gifh = pygame.image.load("gif/"+gp+"/0008.gif")
				gifi = pygame.image.load("gif/"+gp+"/0009.gif")

			elif event.key == pygame.K_KP_DIVIDE:
				try:
					selectedGifPack -= 1
					gp = gifpacks[selectedGifPack]
					print(gp)
				except (ValueError,IndexError) as e:
					selectedGifPack = 0
					gp = gifpacks[selectedGifPack]
					print(gp)

			#GIFS
				gifa = pygame.image.load("gif/"+gp+"/0001.gif")
				gifb = pygame.image.load("gif/"+gp+"/0002.gif")
				gifc = pygame.image.load("gif/"+gp+"/0003.gif")
				gifd = pygame.image.load("gif/"+gp+"/0004.gif")
				gife = pygame.image.load("gif/"+gp+"/0005.gif")
				giff = pygame.image.load("gif/"+gp+"/0006.gif")
				gifg = pygame.image.load("gif/"+gp+"/0007.gif")
				gifh = pygame.image.load("gif/"+gp+"/0008.gif")
				gifi = pygame.image.load("gif/"+gp+"/0009.gif")




			if event.key == pygame.K_KP_PLUS:
				try:
					selectedPack += 1
					p = packs[selectedPack]
					print(p)
				except IndexError:
					selectedPack = 0
					p = packs[selectedPack]
					print(p)

				a = pygame.mixer.Sound("wav/"+p+"/0001.wav")
				b = pygame.mixer.Sound("wav/"+p+"/0002.wav")
				c = pygame.mixer.Sound("wav/"+p+"/0003.wav")
				d = pygame.mixer.Sound("wav/"+p+"/0004.wav")
				e = pygame.mixer.Sound("wav/"+p+"/0005.wav")
				f = pygame.mixer.Sound("wav/"+p+"/0006.wav")
				g = pygame.mixer.Sound("wav/"+p+"/0007.wav")
				h = pygame.mixer.Sound("wav/"+p+"/0008.wav")
				i = pygame.mixer.Sound("wav/"+p+"/0009.wav")
				#get sample lengths
				samples=[a,b,c,d,e,f,g,h,i]
				x = 10
				for i in samples:
					count = 0
					smpLen = round(i.get_length(),1)
					print ("Num",samples.index(i)+1,"-",smpLen)	
										

			elif event.key == pygame.K_KP_MINUS:
				try:
					selectedPack -= 1
					p = packs[selectedPack]
					print(p)
				except IndexError:
					selectedPack = 0
					p = packs[selectedPack]
					print(p)

				a = pygame.mixer.Sound("wav/"+p+"/0001.wav")
				b = pygame.mixer.Sound("wav/"+p+"/0002.wav")
				c = pygame.mixer.Sound("wav/"+p+"/0003.wav")
				d = pygame.mixer.Sound("wav/"+p+"/0004.wav")
				e = pygame.mixer.Sound("wav/"+p+"/0005.wav")
				f = pygame.mixer.Sound("wav/"+p+"/0006.wav")
				g = pygame.mixer.Sound("wav/"+p+"/0007.wav")
				h = pygame.mixer.Sound("wav/"+p+"/0008.wav")
				i = pygame.mixer.Sound("wav/"+p+"/0009.wav")
				#get sample lengths
				samples=[a,b,c,d,e,f,g,h,i]
				for i in samples:
					count = 0
					smpLen = round(i.get_length(),1)
					print ("Num",samples.index(i)+1,"-",smpLen)	
					
		try:
			#numpad input
			if event.type == pygame.KEYDOWN:
				pygame.draw.polygon(screen, colour2, [[random.randint(0,100), 100], [random.randint(0,100), 400],[400, 300]], 2)	
				#change rect size
				rectS += random.randint(0,50)
				pygame.draw.rect(screen, colour2, [rectS * 2, 50, rectS, rectS])
				if event.key == pygame.K_KP1:
					#play sound
					a.play()
					image(gifa)
					
					
					
						
			elif event.type == pygame.KEYUP:
				screen.fill(colour)	
				rectS = 0
				if event.key == pygame.K_KP1:
			
					#stop sound on keyup
					a.stop()


			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_KP2:
					b.play()
					image(gifb)
					
			elif event.type == pygame.KEYUP:
				if event.key == pygame.K_KP2:
					b.stop()

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_KP3:
					c.play()
					image(gifc)
			elif event.type == pygame.KEYUP:
				if event.key == pygame.K_KP3:
					c.stop()
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_KP4:
					d.play()
					image(gifd)
			elif event.type == pygame.KEYUP:
				if event.key == pygame.K_KP4:
					d.stop()
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_KP5:
					e.play()
					image(gife)
			elif event.type == pygame.KEYUP:
				if event.key == pygame.K_KP5:
					e.stop()
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_KP6:
					f.play()
					image(giff)
			elif event.type == pygame.KEYUP:
				if event.key == pygame.K_KP6:
					f.stop()
							
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_KP7:
					g.play()
					image(gifg)
			elif event.type == pygame.KEYUP:
				if event.key == pygame.K_KP7:
					g.stop()
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_KP8:
					h.play()
					image(gifh)
			elif event.type == pygame.KEYUP:
				if event.key == pygame.K_KP8:
					h.stop()
					
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_KP9:
					i.play()
					image(gifi)
			elif event.type == pygame.KEYUP:
				if event.key == pygame.K_KP9:
					i.stop()
		except NameError:
			pass
	pygame.display.flip()
