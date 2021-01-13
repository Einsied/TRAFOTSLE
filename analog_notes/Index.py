import os

def GenerateFolder(Folder):
	if not os.path.exists(Folder):
		os.makedirs(Folder)
	return

def indentedNewLine(content, indentationDepth = 0):
	return "\t" * indentationDepth + content
	
ItemFolders = os.listdir("./")

Images = {}

for Folder in ItemFolders:
	if os.path.isdir(Folder):
		Images[Folder] = (os.listdir(Folder))

jsonIndentation = 0
jsonString = indentedNewLine("{\n", jsonIndentation)
jsonIndentation += 1
jsonString += indentedNewLine("\"Items\":[", jsonIndentation)
jsonIndentation += 1
first = True
for key in Images.keys():
	if not first:
		jsonString += ","
	else:
		first = False
	jsonString += "\n" + indentedNewLine("{", jsonIndentation)
	jsonIndentation += 1
	jsonString += "\n" + indentedNewLine("\"Id\":\"{key:}\",".format(key = key), jsonIndentation)
	jsonString += "\n" + indentedNewLine("\"Images\":[", jsonIndentation)
	jsonIndentation += 1
	firstImage = True
	for Image in Images[key]:
		if not firstImage:
			jsonString += ","
		else:
			firstImage = False
		jsonString += "\n" + indentedNewLine("\"{Image:}\"".format(Image = Image), jsonIndentation)
	jsonIndentation -= 1
	jsonString += "\n" + indentedNewLine("]", jsonIndentation)
	jsonIndentation -= 1
	jsonString += "\n" + indentedNewLine("}", jsonIndentation)
jsonIndentation -= 1
jsonString += "\n" + indentedNewLine("]", jsonIndentation)
jsonIndentation -= 1
jsonString += "\n" + indentedNewLine("}", jsonIndentation)
with open("ImageIndex.json", "w") as index:
	index.write(jsonString)
