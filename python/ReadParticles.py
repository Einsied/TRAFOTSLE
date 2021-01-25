import os
import json

def reformParagraph(lineList):
	paragraph = ""
	for line in lineList:
		paragraph += " " + line.strip()
	return paragraph.strip()

def Read(ParticleFolder):
	ParticleFiles = os.listdir(ParticleFolder)
	Particles = {}

	for ParticleFile in ParticleFiles:
		with open(ParticleFolder + ParticleFile, "r") as particleFile:
			try:
				particle = json.load(particleFile)
			except ValueError:
				print("Error while reading {ParticleFile:}".format(
					ParticleFile = ParticleFile
				))
				raise
			Particles[particle["Id"]] = {
				"Content": reformParagraph(particle["Content"]),
				"SourceId": particle["SourceId"]
			}
	return Particles
