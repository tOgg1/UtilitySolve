import os.path
import pygame
from pygame.locals import * 

def loadImage(name):
	path = os.path.join('res', name)
	try:
		image = pygame.image.load(path)
	except pygame.error, message:
		print 'Image unable to load: ', name
		raise SystemExit, message

	image = image.convert()

	return image, image.get_rect()
