from BayesianNetwork import BayesianNetwork
from BayesianNode import BayesianNode
from NetworkLoader import NetworkLoader
from MapManager import MapManager

from Misc import debugPrint as db
from Misc import normalPrint as pr
from Misc import errorPrint as er
from Misc import Config as cnf

from PyGameHelpers import *
import pygame
from pygame.locals import * 

import threading

import unittest

class UtilitySolver:

	def __init__(self):
		self.tasks = []
		self.running = False

		# Variables to be loaded during run
		self.screen = None
		self.save = None
		self.network = None
		self.mapsize = [768, 576]

		# Variables that can be loaded now
		self.loader = NetworkLoader()
		self.mapManager = MapManager(self.mapsize)

	def run(self):
		if(testMode != None):
			pygame.init()
			self.screen = pygame.display.set_mode((self.mapsize[0], self.mapsize[1]))
			pygame.display.set_caption('UtilitySolver')
			pygame.mouse.set_visible(1)


		## Init pyGame
		pygame.init()
		self.screen = pygame.display.set_mode((self.mapsize[0], self.mapsize[1]))
		pygame.display.set_caption('UtilitySolver')
		pygame.mouse.set_visible(1)

		# load images
		BayesianNode.loadImages(1.2)

		# Init network
		self.loader = NetworkLoader()

		self.save = self.loader.checkForPossibleSaves()

		if(self.save == None):
			pr("Okey, no saves to load, lets make a new network.")
			name = raw_input("What do you want to call your network? ")
			self.save = self.loader.createSave(name)
			pr("New network " + name + " created")

		pr("UtilitySolver " + cnf.versionName+"\n")

		# Goto mainloop
		self.loop()

	def loop(self):	

		node1 = BayesianNode()

		self.running = True

		inputThread = threading.Thread(target = self.inputManager)
		inputThread.start()

		# Set backgroundinitial color to white
		self.screen.fill(Color(255,255,255,255))
		try:
			while(self.running):

				# Event-handling
				for event in pygame.event.get():
					if event.type == QUIT:
						running = False
						return
				# Redraw
				self.screen.blit(BayesianNode.image, BayesianNode.imageRect)
				pygame.display.flip()
		except:
			er("Something went wrong...")
		finally:
			# Clean-up
			self.running = False

			pygame.quit()
			inputThread.join()

	def inputManager(self):
		while(self.running):
			pr(cnf.mainMenu)
			ans = raw_input("What do you want to do? ")

			while(True):
				try:
					ans = int(ans)
					break
				except:
					ans = raw_input("Invalid input, try again: ")
					continue

			# Decode input
			if(ans == 1):
				self.editNetwork()
			elif(ans == 2):
				self.saveNetwork()
			elif(ans == 3):
				self.loadNetwork()
			elif(ans == 4):
				self.running = False
			#elif(ans == 5):

	# Network functions

	def editNetwork(self):
		lol = 3

	def saveNetwork(self):
		lol = 4

	def loadNetwork(self):
		lol = 5		

	def doInference(self):
		lol = 2

	def editNetwork(self):
		lol = 4


if __name__ == '__main__':
	cnf.debug = False
	util = UtilitySolver()
	util.run()



