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
import tkMessageBox

# initializes a window and an additional frame
root = tk.Tk()
root.title("This is a simple counter")
frame = tk.Frame()

# import a .gif and make a logo with it
foto1 = tk.PhotoImage(file = "giphy-downsized.gif")
logo1 = tk.Label(root, image = foto1, justify = tk.LEFT)

# orange is default background color
var1 = tk.StringVar() # initialize an interactive variable
var1.set("orange")

# create a simple counter
label1 = tk.Label(root, fg = "black", bg = var1.get(), justify = tk.CENTER,
				  font = "Arial 100 bold", width = 5) # initialize a label to pack counter on

hp.counter_label(label = label1) # start to count

button1 = tk.Button(root, text = "STOP", font = "Arial 20 italic", width = 20, command = root.destroy)
button2 = tk.Button(root, text = "RESET secs.", font = "Arial 20 italic", width = 20, command = hp.set_counter)

# create another buttons to count manually
def call_manual_counter():
	hp.manual_counter(label = label2)

def call_reset_manual_counter():
	hp.reset_manual_counter(label = label2)	

label2 = tk.Label(frame, text = 0, font = "Arial 100 bold", width = 5, bg = var1.get(),
				  justify = tk.CENTER, fg = "black")

button3 = tk.Button(frame, text = "Count manually", font = "Arial 20 italic", width = 12, command = call_manual_counter)
button4 = tk.Button(frame, text = "RESET man.", font = "Arial 20 italic", width = 12, command = call_reset_manual_counter)

label3 = tk.Label(text = "Choose a background color for your counter:", font = "Arial 20 bold", bg = var1.get(),
		 		  justify = tk.CENTER, padx = 10)
 
# list of all tk labels for iteration
labellist = [label1, label2, label3]

# make background color ('bg') of counter available through a radio button
background_colors = [ # tuples of colors for iteration
    ("light blue", "light blue"),
    ("orange", "orange"),
    ("red", "dark red"),
    ("green", "dark green"),
    ("yellow", "yellow")
]

def update_background_color():
	global labellist
	for lab in labellist:
		lab.config(bg = var1.get())
		   	
# add some check boxes to indicate use options
var2 = tk.IntVar()
var3 = tk.IntVar()

def various_states():
	print("commercial use: %d,\nacademic use: %d" % (var2.get(), var3.get()))

label4 = tk.Label(root, text = "What do you plan to use this app for:")

checkbut1 = tk.Checkbutton(root, text = "commercial use", variable = var2)
checkbut2 = tk.Checkbutton(root, text = "academic use", variable = var3)

# packs all elements of widget, also .grid(row = 0, sticky = tk.W)
label3.pack()
for name, color in background_colors: # splits tuples from above to iterate over colors
	tk.Radiobutton(root, text = name, padx = 20, variable = var1,
                   command = update_background_color, font = "Arial 16 italic",
                   value = color).pack(anchor = tk.W)
logo1.pack()

label1.pack(side = tk.TOP)
button1.pack(side = tk.TOP)
button2.pack(side = tk.TOP)

frame.pack()
label2.pack(side = tk.TOP)
button3.pack(side = tk.LEFT)
button4.pack(side = tk.RIGHT)

label4.pack(side = tk.BOTTOM, anchor = tk.W, pady = 20) # pady to keep some space between elements in y direction
checkbut1.pack(side = tk.BOTTOM, anchor = tk.W, pady = 2)
checkbut2.pack(side = tk.BOTTOM, anchor = tk.W, pady = 2)

# include a message box to interact with window manager
def callback4():
    if tkMessageBox.askokcancel("Quit", "Do you really wish to quit?"):
        root.destroy()

root.protocol("WM_DELETE_WINDOW", callback4)

# starts mainloop
root.mainloop() 
