# identify python version and import functions that are version dependent
def pythonVersionCheck():
	import sys
	if sys.version_info[0] < 3:
    	print("You're running Python 2.x")
    	import Tkinter as tk
	else:
    	print("You're running Python 3.x")
    	import tkinter as tk