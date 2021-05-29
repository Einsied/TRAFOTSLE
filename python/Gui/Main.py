import tkinter

class Application(tkinter.Frame):
	def __init__(self, master, createHtmlHandle):
		super().__init__(master)
		self.master = master
		self.createHtml = createHtmlHandle
		self.pack()
		self.create_widgets()

	def create_widgets(self):
		self.createHtml = tkinter.Button(self, text="Create Html",
			command=self.createHtml
		)
		self.createHtml.pack(side="top")

		self.quit = tkinter.Button(self, text="Quit", fg="red",
			command=self.master.destroy
		)
		self.quit.pack(side="bottom")

	def say_hi(self):
		print("Hi")
