'''
developed by Daniel (d.schuette@online.de)
This is a test .app to test tkinter and py2app
latest version: v0.03 (as of 02/28/2018)
-> runs with python 2.7.14 and python 3.6.x
'''
# test which version runs to install Tkinter correctly
import VersionCheck as vs
vs.pythonVersionCheck() # makes tk available in module
from VersionCheck import tk # imports tk from module

# initializes a window
root = tk.Tk()

# starts mainloop
root.mainloop() 

