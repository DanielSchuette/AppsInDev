'''
developed by Daniel (d.schuette@online.de)
This is a test .app to test tkinter and py2app
latest version: v0.02 (as of 02/27/2018)
-> runs with python 2.7.14
'''
# console output to indicate a smooth start
print("Program started successfully")
# import tkinter depending on python version

import time as time
# time.sleep(1) # prevents tkinter from updating the GUI! that is why it does not work!
# when you need to loop in a GUI, use .after method!

import sys
if sys.version_info[0] < 3:
    print("You're running Python 2.x")
    import Tkinter as tk
else:
    print("You're running Python 3.x")
    import tkinter as tk


# set up a GUI window
root = tk.Tk() # initializes the root widget (there can be just one!)
root.maxsize(7000, 3000)

# all following widgets have to refer to the parent/root widget
# label1 = tk.Label(root, text = "Hello World!", bg = "dark blue", fg = "dark red", font = "Calibri 32 bold") 
# label1.pack() # pack method puts label into window and fits window size to text

# add another label with justified text
text1 = "This picture is a .gif, the only foto format (except for\nPPM/PGM) that is currently supported by TKinter..!"
# label2 = tk.Label(root, text = text1, justify = tk.LEFT, padx = 10)
# label2.pack(side = "left")

# fotos can be included as well
foto1 = tk.PhotoImage(file = "giphy-downsized.gif")
# logo1 = tk.Label(root, image = foto1)
# logo1.pack(side = "right") # currently, just GIF and PPM/PGM formats!

# a foto can be printed relative to the text (compound = tk.CENTER, tk.BOTTOM, tk.TOP, ...)
# text font can be changed as shown below as well
logo2  = tk.Label(root, image = foto1, text = text1, compound = tk.BOTTOM, padx = 10, justify = tk.LEFT,
                  fg = "dark red", font = "Times 20 bold italic", bg = "light blue")
logo2.pack(side = "left")

# labels can also contain dynamical content:
counter = 0
def counter_label(label):
    def count():
        global counter
        counter += 0.1
        label.config(text = str(counter)) # ..config method of tk.Label class .config(label_options, ...)
        label.after(100, count) # .after method of tk.Label class .after(delay, function_to_call)    
    count()

def set_counter():
    global counter
    counter = 0

root.title("This application counts seconds")
label2 = tk.Label(root, bg = "light blue", fg = "dark red", font = "Calibri 200 bold")
label2.pack()
counter_label(label = label2)

button1 = tk.Button(root, text = "Reset", width = 25, command = set_counter)
button1.pack(side = "bottom")

button2 = tk.Button(root, text = "Stop", width = 25, command = root.destroy)
button2.pack(side = "bottom")


# another way to display a text message is the tk.Message widget
# the .config method lets you access properties
text2 = "Time (in secs)"
text3 = "Do not forget to close the window!"

var1 = tk.StringVar(root)
var1.set(text2)



message1 = tk.Message(root, textvariable = var1)
message1.config(bg = "light blue", fg = "black", font = "Calibri 24 bold", width = 360, borderwidth = 85, 
    relief = "flat", anchor = "nw", textvariable = var1) 
message1.pack(side = "top")

# to make the window appear, the the mainloop method is required
root.mainloop()

# as long as the window is not killed, no further console output will be printed
# meaning, that the following print() function will be executed after closing it
initialize = True
debug_time = 0  
def debug_printer(initialize):
    global debug_time
    while(debug_time <= 4):
        debug_time += 1
        print(debug_time)
debug_printer(initialize = initialize)

print("Program closed successfully")
