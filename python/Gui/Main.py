import tkinter
import python.Gui.writeParticle

class Application(tkinter.Frame):
	def __init__(self, master, main):
		super().__init__(master)
		self.master = master
		self.main = main 
		self.writeWidget = python.Gui.writeParticle.writeWidget(self)
		self.writeWidget.pack(side="right")
		self.pack()
		self.create_widgets()

	def create_widgets(self):
		self.createHtml = tkinter.Button(self, text="Create Html",
			command=self.main.createHtml
		)
		self.createHtml.pack(side="top")

		self.quit = tkinter.Button(self, text="Quit", fg="red",
			command=self.master.destroy
		)
		self.quit.pack(side="bottom")
