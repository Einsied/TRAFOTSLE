import os
import json

def Read(NoteFilePath):
	Notes = {}
	with open(NoteFilePath, "r") as NoteFile:
		NotesTmp = json.load(NoteFile)
		for Note in NotesTmp["Notes"]:
			Notes[Note["Id"]] = {
				"Description": Note["Description"],
				"File": Note["File"],
				"Particles": Note["Particles"]
			}
	return Notes 
