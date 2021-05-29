import tkinter
from python.Gui import Main

def run(createHtmlHandle):
	root = tkinter.Tk()
	app = Main.Application(root, createHtmlHandle)
	app.mainloop()
