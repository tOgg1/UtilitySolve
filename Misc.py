class Config:
	debug = True
	notFoundHash = "returnvalue:NotFound"
	errorHash = "returnvalue:Error"
	useSaveFile = True

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


