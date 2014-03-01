class Config:
	versionName = "Version 1.0"
	versionValue = 10
	debug = True
	notFoundHash = "returnvalue:NotFound"
	errorHash = "returnvalue:Error"
	useSaveFile = True
	mainMenu = "[1]: Edit network\n[2]: Save network\n[3]: Load network\n[4]: Exit"
	networkMenu = ("[0]: Finalize\n[1]: Add Node\n[2]: Edit Node\n[3]: Delete Node\n"
				   "[4]: Add UtilityNode\n[5]: Add decision Node\n[6]: Do inference\n"
				   "[7]: Definalize")
	inferenceMenu = "[1]: Add evidence\n[2]: Calculate utility\n"

def normalPrint(content):
	print(content)

def debugPrint(text):
	if(Config.debug):
		print("[Debug]: " + text)

def errorPrint(text):
	print("[Error]: " + text)

def extractValue(content, value, lowIndex = None):
	try:
		index = content.find(value, lowIndex)
		if(index == -1):
			return Config.notFoundHash
		return content[index : content.find("\n", index)].replace(" ", "").split("=")[1]
	except:
		return Config.errorHash


