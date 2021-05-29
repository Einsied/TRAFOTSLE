import tkinter
from python.Gui import Main

def run(main):
	root = tkinter.Tk()
	app = Main.Application(root, main)
	app.mainloop()
