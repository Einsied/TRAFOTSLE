import os
import json

def reformParagraph(lineList):
	paragraph = ""
	for line in lineList:
		paragraph += " " + line.strip()
	return paragraph

def Read(ConceptFolder):
	ConceptFiles = os.listdir(ConceptFolder)
	Concepts = {}

	for ConceptFile in ConceptFiles:
		with open(ConceptFolder + ConceptFile, "r") as conceptFile:
			concept = json.load(conceptFile)
			Concepts[concept["Id"]] = {
				"Name": concept["Name"],
				"Description": [reformParagraph(line)
					for line in concept["Description"]
				],
				"Particles": concept["Particles"]
			}
	return Concepts
