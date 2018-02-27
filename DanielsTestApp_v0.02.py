'''
developed by Daniel (d.schuette@online.de)
This is a test .app to test tkinter and py2app
latest version: v0.02 (as of 02/27/2018)
-> runs with python 2.7.14
'''
# console output to indicate a smooth start
print("Program started successfully")
# import tkinter depending on python version
import sys
if sys.version_info[0] < 3:
    print("You're running Python 2.x")
    import Tkinter as tk
else:
    print("You're running Python 3.x")
    import tkinter as tk
    
# set up a GUI window
root = tk.Tk() # initializes the root widget (there can be just one!)

# all following widgets have to refer to the parent/root widget
label1 = tk.Label(root, text = "Hello World!") 
label1.pack() # pack method puts label into window and fits window size to text

# add another label with justified text
text1 = "This picture is a .gif, the only foto format (except for\nPPM/PGM) that is currently supported by TKinter..!"
label2 = tk.Label(root, text = text1, justify = tk.LEFT, padx = 10)
label2.pack(side = "left")

# fotos can be included as well
foto1 = tk.PhotoImage(file = "giphy-downsized.gif")
logo1 = tk.Label(root, image = foto1)
logo1.pack(side = "right") # currently, just GIF and PPM/PGM formats!

# to make the window appear, the the mainloop method is required
root.mainloop()

# as long as the window is not killed, no further console output will be printed
# meaning, that the following print() function will be executed after closing it
print("Program closed successfully")
