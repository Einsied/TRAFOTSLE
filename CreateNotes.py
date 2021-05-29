import os
from python import CreateImageIndex
from python import ReadParticles
from python import ReadConcepts
from python import ReadTopics
from python import ReadAnalogItems
from python import ReadDigitalNotes
from python import Connect
from python import CreateHtmlNotes

class main:
	def __init__(self):
		self.jsonFileName = CreateImageIndex.CreateIndex("./analog_notes/")
		self.Items = ReadAnalogItems.Read("./analog_notes/NewIndex.json", "./analog_notes/OldIndex.json", self.jsonFileName)
		self.Notes = ReadDigitalNotes.Read("./digital_notes/Index.json")
		self.Particles = ReadParticles.Read("./particles/")
		self.Concepts = ReadConcepts.Read("./concepts/")
		self.Topics = ReadTopics.Read("./topics/")
		self.Uncontained = Connect.connect(
			self.Topics, self.Concepts, self.Particles, self.Items, self.Notes
		)
	def createHtml(self):
		CreateHtmlNotes.HtmlNotes("./html").CreateNotes(
			self.Items, self.Notes, self.Particles, self.Concepts, self.Topics, 
			self.Uncontained
		)

Main = main()
Main.createHtml()
