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

a = pygame.mixer.Sound("wav/"+p+"/0001.wav")
b = pygame.mixer.Sound("wav/"+p+"/0002.wav")
c = pygame.mixer.Sound("wav/"+p+"/0003.wav")
d = pygame.mixer.Sound("wav/"+p+"/0004.wav")
e = pygame.mixer.Sound("wav/"+p+"/0005.wav")
f = pygame.mixer.Sound("wav/"+p+"/0006.wav")
g = pygame.mixer.Sound("wav/"+p+"/0007.wav")
h = pygame.mixer.Sound("wav/"+p+"/0008.wav")
i = pygame.mixer.Sound("wav/"+p+"/0009.wav")
while 1:
	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit()
		#choose pack
		if event.type == pygame.KEYDOWN:
			colour
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
		#numpad input
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_KP1:
				a.play()
		elif event.type == pygame.KEYUP:
			if event.key == pygame.K_KP1:
				a.stop()

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_KP2:
				b.play()
		elif event.type == pygame.KEYUP:
			if event.key == pygame.K_KP2:
				b.stop()

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_KP3:
				c.play()
		elif event.type == pygame.KEYUP:
			if event.key == pygame.K_KP3:
				c.stop()
		
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_KP4:
				d.play()
		elif event.type == pygame.KEYUP:
			if event.key == pygame.K_KP4:
				d.stop()
		
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_KP5:
				e.play()
		elif event.type == pygame.KEYUP:
			if event.key == pygame.K_KP5:
				e.stop()
		
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_KP6:
				f.play()
		elif event.type == pygame.KEYUP:
			if event.key == pygame.K_KP6:
				f.stop()
						
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_KP7:
				g.play()
		elif event.type == pygame.KEYUP:
			if event.key == pygame.K_KP7:
				g.stop()
		
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_KP8:
				h.play()
		elif event.type == pygame.KEYUP:
			if event.key == pygame.K_KP8:
				h.stop()
				
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_KP9:
				i.play()
		elif event.type == pygame.KEYUP:
			if event.key == pygame.K_KP9:
				i.stop()
					
		screen.fill(colour)

		pygame.display.flip()
