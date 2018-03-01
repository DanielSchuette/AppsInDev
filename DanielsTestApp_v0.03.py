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
root.title("This is a simple counter")

# make background color ('bg') of counter available through radio button
tk.Label(text = "Choose a background color for your counter:", font = "Arial 20 bold", bg = "light blue").pack()

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
				  font = "Arial 100 bold", width = 5)
label1.pack(side = "top")
counter_label(label1)

button1 = tk.Button(root, text = "STOP", font = "Arial 20 italic", width = 20, command = root.destroy)
button2 = tk.Button(root, text = "RESET secs.", font = "Arial 20 italic", width = 20, command = set_counter)

button1.pack(side = "bottom")
button2.pack(side = "bottom")

# create another buttons to count manually
frame = tk.Frame()
frame.pack()

int_dynamic1 = tk.IntVar(0)
counter2 = 0

button4 = tk.Button(frame, text = "Count manually", font = "Arial 20 italic", width = 12, command = manual_counter)
button4.pack(side = tk.LEFT)
button5 = tk.Button(frame, text = "RESET man.", font = "Arial 20 italic", width = 12, command = reset_manual_counter)
button5.pack(side = tk.RIGHT)

label2 = tk.Label(root, text = int_dynamic1.get(), font = "Arial 100 bold", width = 5, bg = "light blue",
				  justify = tk.CENTER, fg = "black")
label2.pack(side = tk.BOTTOM)

def manual_counter():
	global int_dynamic1
	global counter2
	counter2 += 1
	int_dynamic1.set(counter2)
	label2.config(text = int_dynamic1.get())

def reset_manual_counter():
	global counter2
	counter2 = 0
	int_dynamic1.set(counter2)
	label2.config(text = int_dynamic1.get())

# starts mainloop
root.mainloop() 

