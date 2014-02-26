from BayesianNetwork import BayesianNetwork
from BayesianNode import BayesianNode
from NetworkLoader import NetworkLoader

from Misc import debugPrint as db
from Misc import normalPrint as pr
from Misc import errorPrint as er
from Misc import Config as cnf

from PyGameHelpers import *
import pygame
from pygame.locals import * 

def main():

	## Init pyGame
	pygame.init()
	screen = pygame.display.set_mode((768, 560))
	pygame.display.set_caption('UtilitySolver')
	pygame.mouse.set_visible(1)

	# load images
	BayesianNode.loadImages(1.2)

	loop(screen)

	# Init network
	cnf.debug = False
	loader = NetworkLoader()

	fileToLoad = loader.checkForPossibleSaves()
	save = None

	if(fileToLoad == -1):
		pr("Okey, no saves to load, lets make a new network.")
		name = raw_input("What do you want to call your network? ")
		save = loader.createSave(name)
		pr("New network " + name + " created")
	else:
		save = loader.loadSave(fileToLoad)

	pr("UtilitySolver " + cnf.versionName+"\n")

	# Goto mainloop
	loop(screen)

def loop(screen):	

	node1 = BayesianNode()

	screen.fill(Color(255,255,255,255))
	print BayesianNode.imageRect.size
	screen.blit(BayesianNode.image, BayesianNode.imageRect)
	pygame.display.flip()
	#while(True):
	#pr(cnf.mainMenu)
	hei = 2342
	
def doInference():
	lol = 2

def editNetwork():
	lol = 4

main()


