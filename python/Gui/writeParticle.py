import tkinter

class writeWidget(tkinter.Frame):
	def __init__(self, master):
		super().__init__(master)
		self.master = master
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
				text="Load", command=self.loadParticle
			)
			self.loadButton.grid(row = 0, column = 3)
			self.metaFrame.pack(side="top")
		self.metaFrame = tkinter.Frame(self)
		particleSelection()
	def loadParticle(self):
		curIndex = self.particleSpinbox.get()
		self.textField.delete("1.0", tkinter.END)
		self.textField.insert(tkinter.END,
			self.master.main.Particles["P" + curIndex]["Content"]
		)
	def saveParticle(self):
		print(self.textField.get("1.0", tkinter.END))
		print()
		print("Implementation Pending")
