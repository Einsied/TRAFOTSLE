import json

def reformParagraph(lineList):
	paragraph = ""
	for line in lineList:
		paragraph += " " + line.strip()
	return paragraph.strip()

def Read(NoteFilePath):
	Notes = {}
	with open(NoteFilePath, "r") as NoteFile:
		NotesTmp = json.load(NoteFile)
		for Note in NotesTmp["Notes"]:
			Notes[Note["Id"]] = {
				"Description": reformParagraph(Note["Description"]),
				"File": Note["File"]
			}
	return Notes 
