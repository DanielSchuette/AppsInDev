'''
developed by Daniel (d.schuette@online.de)
This module helps to detect the python version at runtime 
while loading the correct tkinter or throwing an error
repository: https://github.com/DanielSchuette/AppsInDev.git
'''

# identify python version and import functions that are version dependent
def pythonVersionCheck():
	import sys # sys is not a global import
	global tk # ... to ensure that tk is globally available IN THIS MODULE
	global ttk
	print("\n" + "********************************" + "\n")
	print("Program started successfully")
	if sys.version_info[0] < 3:
		print("You're running Python 2.x")
		tk = __import__("tkinter", globals(), locals())
		from tkinter import ttk
	else:
		print("You're running Python 3.x")
		print("The app does not run with python 3 at the moment!")
		print("\n" + "********************************" + "\n")
		sys.exit()