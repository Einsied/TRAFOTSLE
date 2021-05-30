import tkinter

#Source Types
analog = 0
digital = 1

class writeWidget(tkinter.Frame):
	def __init__(self, master):
		super().__init__(master)
		self.master = master
		self.source = analog
		self.SourceId = "none"
		self.createMetaFrame()
		self.textField = tkinter.Text(self, width = 60, height = 5,
			wrap=tkinter.WORD
		)
		self.textField.pack()
		self.saveButton = tkinter.Button(self, text="Save Particle",
			command=self.saveParticle
		)
		self.saveButton.pack(side="bottom")
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
		curIndex = self.particleSpinbox.get()
		self.textField.delete("1.0", tkinter.END)
		self.textField.insert(tkinter.END,
			self.master.main.Particles["P" + curIndex]["Content"]
		)
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
	def switchSource(self):
		if self.source == analog:
			activeArray = self.master.main.Notes
			self.sourceFrontLabel["text"] = "Source: N"
			self.sourceSwitchButton["text"] = "Switch to Items"
			self.source += 1
		else:
			activeArray = self.master.main.Items
			self.sourceFrontLabel["text"] = "Source: I"
			self.sourceSwitchButton["text"] = "Switch to Notes"
			self.source = analog
		self.sourceSpinbox["to"] = len(activeArray)
		self.sourceSpinbox.delete(0, "end")
		self.sourceSpinbox.insert(0, "{:03d}".format(
			len(activeArray)
		))
		self.updateSource()
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
			curIndex = self.sourceSpinbox.get()
			if self.source == analog:
				self.SourceId = "N" + curIndex
			elif self.source == digital:
				self.SourceId = "I" + curIndex
	def saveParticle(self):
		print(self.textField.get("1.0", tkinter.END))
		print(self.SourceId)
		print()
		print("Implementation Pending")
