import os
import json

def Read(ParticleFolder):
	ParticleFiles = os.listdir(ParticleFolder)
	Particles = {}

	for ParticleFile in ParticleFiles:
		with open(ParticleFolder + ParticleFile, "r") as particleFile:
			particle = json.load(particleFile)
			Particles[particle["Id"]] = particle["Content"]
	return Particles
