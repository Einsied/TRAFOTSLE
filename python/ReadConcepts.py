import os
import json

def reformParagraph(lineList):
	paragraph = ""
	for line in lineList:
		paragraph += " " + line.strip()
	return paragraph.strip()

def Read(ConceptFolder):
	ConceptFiles = os.listdir(ConceptFolder)
	Concepts = {}

	for ConceptFile in ConceptFiles:
		with open(ConceptFolder + ConceptFile, "r") as conceptFile:
			try:
				concept = json.load(conceptFile)
			except ValueError:
				print("Error while reading(ConceptFile:)".format(
					ConceptFile = ConceptFile
				))
				raise
			Concepts[concept["Id"]] = {
				"Name": concept["Name"],
				"Description": [reformParagraph(line)
					for line in concept["Description"]
				],
				"Particles": concept["Particles"]
			}
	return Concepts
