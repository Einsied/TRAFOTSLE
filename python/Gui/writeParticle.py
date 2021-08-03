import tkinter

#Source Types
analog = 0
digital = 1
textFieldHeight = 10

class writeWidget(tkinter.Frame):
	def __init__(self, master):
		super().__init__(master)
		self.master = master
		self.source = analog
		self.SourceId = "none"
		self.creatingNew = False
		self.createMetaFrame()
		self.textField = tkinter.Text(self, width = 60,
			height = textFieldHeight, wrap=tkinter.WORD
		)
		self.textField.pack()
		self.saveButton = tkinter.Button(self, text="Save Particle",
			command=self.saveParticle
		)
		self.saveButton.pack(side="bottom")
		self.loadParticle()
	def createMetaFrame(self):
		def particleSelection():
			particleFrontLabel = tkinter.Label(
				self.metaFrame, text = "Particle: P"
			)
			particleFrontLabel.grid(row = 0, column = 0)
			self.particleSpinbox = tkinter.Spinbox(
				self.metaFrame, from_ = 1, 
				to = len(self.master.main.Particles), 
				format="%04.0f", width = 4
			)
			self.particleSpinbox.delete(0, "end")
			self.particleSpinbox.insert(0, "{:04d}".format(
				len(self.master.main.Particles)
			))
			self.particleSpinbox.grid(row = 0, column = 1)
			particleEndLabel = tkinter.Label(
				self.metaFrame, text = ".json"
			)
			particleEndLabel.grid(row = 0, column = 2)
			self.loadButton = tkinter.Button(self.metaFrame, 
				text="Load", command=self.loadParticle, width = 8
			)
			self.loadButton.grid(row = 0, column = 3)
			self.newButton = tkinter.Button(self.metaFrame, 
				text="New", command=self.createNewParticle, width = 8
			)
			self.newButton.grid(row = 0, column = 4)
		def sourceSelection():
			self.sourceFrontLabel = tkinter.Label(
				self.metaFrame, text = "Source: X"
			)
			self.sourceFrontLabel.grid(row = 1, column = 0)
			self.sourceSpinbox = tkinter.Spinbox(
				self.metaFrame, from_ = 1, 
				to = 2, format="%03.0f", width = 3
			)
			self.sourceSpinbox.grid(row = 1, column = 1)
			sourceEndLabel = tkinter.Label(
				self.metaFrame, text = ".json"
			)
			sourceEndLabel.grid(row = 1, column = 2)
			self.sourceSwitchButton = tkinter.Button(self.metaFrame, 
				text="Switch", command=self.switchSource
			)
			self.sourceSwitchButton.grid(row = 1, column = 4)
			self.linkButton = tkinter.Button(self.metaFrame, 
				text="not linked", command=self.linkSource, width = 8
			)
			self.linkButton.grid(row = 1, column = 3)
			self.switchSource()
		self.metaFrame = tkinter.Frame(self)
		particleSelection()
		sourceSelection()
		self.metaFrame.pack(side="top")
	def loadParticle(self):
		curIndex = "{:04d}".format(int(self.particleSpinbox.get()))
		self.textField.delete("1.0", tkinter.END)
		self.textField.insert(tkinter.END,
			self.master.main.Particles["P" + curIndex]["Content"]
		)
		self.particleSpinbox.delete(0, "end")
		self.particleSpinbox.insert(0, curIndex)
		newSourceId = self.master.main.Particles["P" + curIndex]["SourceId"]
		if newSourceId != None:
			source = analog
			if newSourceId[0] == "I":
				source = digital
			if self.source != source:
				self.switchSource()
			self.sourceSpinbox.delete(0, "end")
			self.sourceSpinbox.insert(0, "{:03d}".format(
				int(newSourceId[1:])
			))
			if self.SourceId == "none":
				self.linkSource()
				self.updateSource()
			else:
				self.updateSource()
		else:
			if self.SourceId != "none":
				self.linkSource()
				self.updateSource()
	def createNewParticle(self):
		if (not self.creatingNew):
			self.newButton["text"] = "Abort"
			self.textField.delete("1.0", tkinter.END)
			self.particleSpinbox["to"] = len(self.master.main.Particles) + 1 
			self.particleSpinbox.delete(0, "end")
			self.particleSpinbox.insert(0, "{:04d}".format(
				len(self.master.main.Particles) + 1
			))
			self.SourceId = "" 
			# Link soruce checks if the field is "none" if not it unlinks
			self.linkSource()
			# Make sure we can not load into nonsense
			self.loadButton["state"] = "disabled"
		else:
			self.newButton["text"] = "New"
			self.particleSpinbox.to = len(self.master.main.Particles)
			# Load the last particle
			self.particleSpinbox.delete(0, "end")
			self.particleSpinbox.insert(0, "{:04d}".format(
				len(self.master.main.Particles)
			))
			self.loadParticle()
			self.loadButton["state"] = "normal"
		self.creatingNew = not self.creatingNew 
	def switchSource(self):
		# Switch between states
		if self.source == analog:
			self.source += 1
		else:
			self.source = analog 
		self.setSource()
		self.updateSource()
	def setSource(self):
		activeArray = []
		if self.source == analog:
			activeArray = self.master.main.Notes
			self.sourceFrontLabel["text"] = "Source: N"
			self.sourceSwitchButton["text"] = "Switch to Items"
		elif self.source == digital:
			activeArray = self.master.main.Items
			self.sourceFrontLabel["text"] = "Source: I"
			self.sourceSwitchButton["text"] = "Switch to Notes"
		else:
			print("Source-type unknown")
		self.sourceSpinbox["to"] = len(activeArray)
		self.sourceSpinbox.delete(0, "end")
		self.sourceSpinbox.insert(0, "{:03d}".format(
			len(activeArray)
		))
	def linkSource(self):
		if self.SourceId == "none":
			self.SourceId = ""
			self.linkButton["text"] = "linked"
			self.updateSource()
		else:
			self.SourceId = "none"
			self.linkButton["text"] = "not linked"
	def updateSource(self):
		if self.SourceId != "none":
			curIndex = "{:03d}".format(int(self.sourceSpinbox.get()))
			if self.source == analog:
				self.SourceId = "N" + curIndex
			elif self.source == digital:
				self.SourceId = "I" + curIndex
			self.sourceSpinbox.delete(0, "end")
			self.sourceSpinbox.insert(0, curIndex)
	def saveParticle(self):
		SourceId = self.SourceId
		Id = "P{:04d}".format(int(self.particleSpinbox.get()))
		RawContent = self.textField.get("1.0", tkinter.END)
		RawContent = RawContent.replace('"', "''")
		RawContent = RawContent.replace("\n", " ")
		RawContentSplit = RawContent.split(" ")
		Content ='\t\t"'
		lineLength = 0
		for i in range(0, len(RawContentSplit), 1):
			word = RawContentSplit[i]
			lineLength += len(word) + 1
			spaceRequired = True
			if lineLength >= 80 - 8: # 8 stand fot to tabs
				Content += '",\n\t\t"'
				lineLength = len(word)
			Content += word + " "
		Content += '"'
		Content = Content.replace(' "', '"')
		Content = Content.replace('\n"', '"')
		json = '{{\n'
		json += '\t"Id": "{Id:}",\n'
		json += '\t"Content": [\n' 
		json += '{Content:}\n' 
		json += '\t],\n'
		json += '\t"SourceId": "{SourceId:}"\n'
		json += '}}'
		self.master.main.Particles[Id] = {
			"Content" : RawContent,
			"SourceId" : SourceId if SourceId != "none" else None,
			"Concepts" : [],
			"Topics" : []
		}
		self.particleSpinbox["to"] = len(self.master.main.Particles) 
		with open(self.master.main.particleFolder + Id + ".json", "w") as jsonFile:
			jsonFile.write(json.format(Id = Id, Content = Content, SourceId = SourceId))
			print("Saved: {:}".format(Id))
		if (self.creatingNew):
			self.createNewParticle()
