# Example on generation of spherical maps

import numpy
import matplotlib.pyplot as plt

cellSize = 1

class Planet:
	def __init__(self, radius):
		self.radius = radius
	def NumberOfCellsOfRing(self, Latitude):
		ringSize = 2* numpy.pi * numpy.sin(Latitude) * self.radius
		return int(numpy.floor(ringSize// cellSize) + 1)
	def createMap(self):
		self.Map = []
		for latitude in numpy.arange(0, numpy.pi/2, cellSize/(self.radius * numpy.pi)):
			self.Map.append([0]*self.NumberOfCellsOfRing(latitude))
		# This step is necessary due to rounding errors
		for i in range(len(self.Map)-1, -1, -1):
			self.Map.append([0]*len(self.Map[i]))
		return self.Map
	def showMap(self):
		for line in self.Map:
			print(line)

A = Planet(10)
A.createMap()
cells = [len(line) for line in A.Map]
polar = numpy.arange(0, numpy.pi, numpy.pi/len(cells))
plt.subplot(1, 2, 1)
plt.scatter(cells, polar)
plt.ylabel("Polar angle in rad")
plt.xlabel("Number of Cells")
plt.title("Number of Cells")
plt.subplot(1, 2, 2)
deltaCells = []
deltaCellsPolar = []
for i in range(0, len(cells) - 1, 1):
	deltaCellsPolar.append((polar[i] + polar[i+1])/2)
	deltaCells.append(abs(cells[i] - cells[i + 1]))
plt.scatter(deltaCells, deltaCellsPolar)
plt.ylabel("Polar angle in rad")
plt.xlabel("Change in the Number of cells of Cells (abs)")
plt.title("Change of Cells")
plt.show()
