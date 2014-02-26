from BayesianNetwork import BayesianNetwork
from BayesianNode import BayesianNode
from NetworkLoader import NetworkLoader
from Misc import debugPrint as db
from Misc import normalPrint as pr
from Misc import errorPrint as er
from Misc import Config as cnf
import pygame
from pygame.locals import * 


def main():
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

	loop()

def loop():	
	while(True):
		pr(cnf.mainMenu)

def doInference():
	lol = 2

def editNetwork():
	lol = 4

main()


