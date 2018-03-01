'''
developed by Daniel (d.schuette@online.de)
This is a test .app to test tkinter and py2app
latest version: v0.031 (as of 02/28/2018)
-> runs with python 2.7.14 and python 3.6.x
'''
# checks version at runtime to install Tkinter correctly
import VersionCheck as vs
vs.pythonVersionCheck() # makes tk available in module
from VersionCheck import tk # imports tk from module

# initializes a window
root = tk.Tk()
root.maxsize(2500, 2500)
root.title("This is a simple counter")

# import and pack a .gif 
foto1 = tk.PhotoImage(file = "giphy-downsized.gif")
logo1 = tk.Label(root, image = foto1, justify = tk.LEFT)
logo1.pack()

# create a simple counter
counter = 0
def counter_label(label):
	def count():
		global counter
		counter += 0.1
		label.config(text = str(counter))
		label.after(100, count)
	count()

def set_counter():
	global counter
	counter = 0

label1 = tk.Label(root, fg = "black", bg = "light blue", justify = tk.CENTER,
				  font = "Arial 100 bold")
label1.pack(side = "top")
counter_label(label1)

button1 = tk.Button(root, text = "STOP", font = "Arial 20 italic", width = 18, command = root.destroy)
button2 = tk.Button(root, text = "RESET", font = "Arial 20 italic", width = 18, command = set_counter)

button1.pack(side = "bottom")
button2.pack(side = "bottom")
# starts mainloop
root.mainloop() 

