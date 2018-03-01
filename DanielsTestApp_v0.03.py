'''
developed by Daniel (d.schuette@online.de)
This is a test .app to test tkinter and py2app
latest version: v0.031 (as of 02/28/2018)
-> runs with python 2.7.14 and python 3.6.x
repository: https://github.com/DanielSchuette/AppsInDev.git
'''
# checks version at runtime to install Tkinter correctly
import VersionCheck as vs
vs.pythonVersionCheck() # makes tk available in module
from VersionCheck import tk # imports tk from module

import helper_functions as hp

# initializes a window
root = tk.Tk()
root.title("This is a simple counter")

# make background color ('bg') of counter available through radio button
var1 = tk.StringVar() # initialize an interactive variable
var1.set("orange") # orange is default

background_colors = [ # tuples of colors for iteration
    ("light blue", "light blue"),
    ("orange", "orange"),
    ("red", "dark red"),
    ("green", "dark green"),
    ("yellow", "yellow")
]

label0 = tk.Label(text = "Choose a background color for your counter:", font = "Arial 20 bold", bg = var1.get(),
		 		  justify = tk.CENTER, padx = 10)
label0.pack()

def update_background_color():
    label0.config(bg = var1.get())
    label1.config(bg = var1.get())
    label2.config(bg = var1.get())

for name, color in background_colors: # splits tuples from above to iterate of colors
	tk.Radiobutton(root, text = name, padx = 20, variable = var1, 
                   command = update_background_color, font = "Arial 16 italic",
                   value = color).pack(anchor = tk.W)

# import and pack a .gif 
foto1 = tk.PhotoImage(file = "giphy-downsized.gif")
logo1 = tk.Label(root, image = foto1, justify = tk.LEFT)
logo1.pack()

# create a simple counter
label1 = tk.Label(root, fg = "black", bg = var1.get(), justify = tk.CENTER,
				  font = "Arial 100 bold", width = 5) # initialize a label to pack counter on
label1.pack(side = "top")
hp.counter_label(label = label1) # start to count
button1 = tk.Button(root, text = "STOP", font = "Arial 20 italic", width = 20, command = root.destroy)
button2 = tk.Button(root, text = "RESET secs.", font = "Arial 20 italic", width = 20, command = hp.set_counter)
button1.pack(side = "bottom")
button2.pack(side = "bottom")

# create another buttons to count manually
def call_manual_counter():
	hp.manual_counter(label = label2)

def call_reset_manual_counter():
	hp.reset_manual_counter(label = label2)	

label2 = tk.Label(root, text = 0, font = "Arial 100 bold", width = 5, bg = var1.get(),
				  justify = tk.CENTER, fg = "black")
label2.pack(side = tk.BOTTOM)

frame = tk.Frame()
frame.pack()

button4 = tk.Button(frame, text = "Count manually", font = "Arial 20 italic", width = 12, command = call_manual_counter)
button4.pack(side = tk.LEFT)
button5 = tk.Button(frame, text = "RESET man.", font = "Arial 20 italic", width = 12, command = call_reset_manual_counter)
button5.pack(side = tk.RIGHT)

# starts mainloop
root.mainloop() 

