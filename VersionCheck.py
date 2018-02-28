# identify python version and import functions that are version dependent
def pythonVersionCheck():
	import sys
	if sys.version < 3:
		print("You're running Python 2.x")
		import TKinter as tk
	else:
		print("You're running Python 2.x")
		import tkinter as tk
