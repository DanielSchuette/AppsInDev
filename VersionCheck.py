# identify python version and import functions that are version dependent
def pythonVersionCheck():
	import sys # sys is not a global import
	global tk # ... to ensure that tk is globally available IN THIS MODULE
	print("\n" + "********************************" + "\n")
	print("Program started successfully")
	if sys.version_info[0] < 3:
		print("You're running Python 2.x")
		tk = __import__("Tkinter", globals(), locals())
	else:
		print("You're running Python 3.x")
		tk = __import__("Tkinter", globals(), locals())
	print("\n" + "********************************" + "\n")