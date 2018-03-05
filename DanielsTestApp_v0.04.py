'''
developed by Daniel (d.schuette@online.de)
This is a test .app to test tkinter and py2app
latest version: v0.04 (as of 03/01/2018)
-> runs with python 2.7.14 and NOT with python 3.6.x
repository: https://github.com/DanielSchuette/AppsInDev.git
'''
# checks version at runtime to install Tkinter correctly
import VersionCheck as vs
vs.pythonVersionCheck() # makes tk available in module
from VersionCheck import tk, ttk # imports tk from module

import helper_functions as hp

# define a new class to get a scrollable frame in tkinter
class ScrollableFrame(ttk.Frame):
    '''
    Consider me a regular frame with a vertical scrollbar on the right, after 
    adding/removing widgets to/from me call my method update() to refresh the scrollable area. 
    Don't pack(), place() or grid() me. I like to be alone in the parent frame.
    '''
    def __init__(self, parent):

        # scrollbar on right in parent 
        yscrollbar = tk.Scrollbar(parent, width = 24)
        yscrollbar.pack(side = tk.RIGHT, fill = tk.Y, expand = False)

        # canvas on left in parent
        self.canvas = tk.Canvas(parent, yscrollcommand = yscrollbar.set, borderwidth = 0, background = "dark red")
        self.canvas.pack(side = tk.LEFT, fill = tk.BOTH, expand = True)

        style = ttk.Style()
        style.theme_use("classic")
        
        def fill_canvas(event):
            "enlarge the windows item to the canvas width"
            canvas_width = event.width
            self.canvas.itemconfig(self.windows_item, width = canvas_width)

        self.canvas.bind('<Configure>', fill_canvas)

        yscrollbar.config(command = self.canvas.yview)    

        # create the scrollable frame and assign it to the windows item of the canvas
        ttk.Frame.__init__(self, parent)
        self.windows_item = self.canvas.create_window(0,0, window = self, anchor = tk.NW)

    def update(self):
        """
        Update changes to the canvas before the program gets
        back the mainloop, then update the scrollregion
        """
        self.update_idletasks()
        self.canvas.config(scrollregion = self.canvas.bbox(self.windows_item))


# cave: make sure to set a large width, otherwise the canvas will look odd
# build a new window and add all elements to new frame class
root = tk.Tk()

root.title("This is a simple counter")

scrollable_fr = ScrollableFrame(root)

# import a .gif and make a logo with it
foto1 = tk.PhotoImage(file = "giphy-downsized.gif")
logo1 = tk.Label(scrollable_fr, image = foto1, justify = tk.LEFT, width = 322, bg = "light grey")

# orange is default background color
var1 = tk.StringVar() # initialize an interactive variable
var1.set("orange")

# create a simple counter
label1 = tk.Label(scrollable_fr, fg = "black", bg = var1.get(), justify = tk.CENTER,
				  font = "Arial 100 bold", width = 5) # initialize a label to pack counter on

hp.counter_label(label = label1) # start to count

button1 = tk.Button(scrollable_fr, text = "STOP", font = "Arial 20 italic", width = 15, command = root.destroy)
button2 = tk.Button(scrollable_fr, text = "RESET secs.", font = "Arial 20 italic", width = 15, command = hp.set_counter)

# create another buttons to count manually
def call_manual_counter():
	hp.manual_counter(label = label2)

def call_reset_manual_counter():
	hp.reset_manual_counter(label = label2)	

label2 = tk.Label(scrollable_fr, text = 0, font = "Arial 100 bold", width = 5, bg = var1.get(),
				  justify = tk.CENTER, fg = "black")

button3 = tk.Button(scrollable_fr, text = "Count manually", font = "Arial 20 italic", width = 15, command = call_manual_counter)
button4 = tk.Button(scrollable_fr, text = "RESET man.", font = "Arial 20 italic", width = 15, command = call_reset_manual_counter)

label3 = tk.Label(scrollable_fr, text = "Choose a background color for your counter:", font = "Arial 20 bold", bg = var1.get(),
		 		  justify = tk.CENTER, padx = 10, width = 200)
 
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

label4 = tk.Label(scrollable_fr, text = "What do you plan to use this app for:", width = 80, bg = "light grey",
                  font = "Arial 32 bold")

checkbut1 = tk.Checkbutton(scrollable_fr, text = "commercial use", variable = var2, width = 15, bg = "light grey",
                           font = "Arial 20 italic")
checkbut2 = tk.Checkbutton(scrollable_fr, text = "academic use", variable = var3, width = 15, bg = "light grey",
                           font = "Arial 20 italic")

# packs all elements of widget, also .grid(row = 0, sticky = tk.W)
label3.pack()
for name, color in background_colors: # splits tuples from above to iterate of colors
	tk.Radiobutton(scrollable_fr, text = name, padx = 20, variable = var1, bg = "light grey",
                   command = update_background_color, font = "Arial 16 italic",
                   value = color, width = 10).pack(anchor = tk.W)
logo1.pack()

label1.pack(side = tk.TOP)
button1.pack(side = tk.TOP)
button2.pack(side = tk.TOP)

label2.pack(side = tk.TOP)
button3.pack(side = tk.TOP)
button4.pack(side = tk.TOP)

label4.pack(side = tk.TOP, anchor = tk.W, pady = 10) # pady to keep some space between elements in y direction
checkbut1.pack(side = tk.TOP, anchor = tk.W, pady = 2)
checkbut2.pack(side = tk.TOP, anchor = tk.W, pady = 2)

# update the scrollable frame to include labels, buttons, etc.
scrollable_fr.update()

# start mainloop
root.mainloop()
