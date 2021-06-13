import os
import sys
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
		self.particleFolder = "./particles/"
		self.jsonFileName = CreateImageIndex.CreateIndex("./analog_notes/")
		self.Items = ReadAnalogItems.Read("./analog_notes/NewIndex.json", "./analog_notes/OldIndex.json", self.jsonFileName)
		self.Notes = ReadDigitalNotes.Read("./digital_notes/Index.json")
		self.Particles = ReadParticles.Read(self.particleFolder)
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
		print("Wrote html files!")
	def addUi(self):
		from python import Ui
		Ui.run(self)

sysargv = sys.argv[1:]
html = "-html"
headless = "-headless"
commands = [html, headless]
for arg in sysargv:
	if arg not in commands:
		print("argument \"{command:}\" unknown".format(command = arg))
Main = main()
if html in sysargv:
	Main.createHtml()
if not headless in sysargv:
	Main.addUi()
