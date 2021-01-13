import os

def GenerateFolder(Folder):
	if not os.path.exists(Folder):
		os.makedir(Folder)
	return

def indentedNewLine(content, indentationDepth = 0):
	return "\t" * indentationDepth + content

def CreateNotes(HtmlFolder, Items, Particles):
	htmlIndentation = 0
	htmlString = ""
