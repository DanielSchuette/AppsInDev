'''
developed by Daniel (d.schuette@online.de)
This module loads helper functions for
tkinter widgets like automatic and manual
counter (03/01/18); 
repository: https://github.com/DanielSchuette/AppsInDev.git
'''
# checks version at runtime to install Tkinter correctly
import VersionCheck as vs
vs.pythonVersionCheck() # makes tk available in module
from VersionCheck import tk # imports tk from module

# initialize a counter
counter = 0

# call function with reference to a label to start the counter
def counter_label(label):
	def count():
		global counter
		counter += 0.1
		label.config(text = str(counter))
		label.after(100, count)
	count()

# resets counter to 0
def set_counter():
	global counter
	counter = 0

# functions to count manually
counter2 = 0 # initialize a counter

def manual_counter(label):
	global counter2
	counter2 += 1
	label.config(text = counter2)

def reset_manual_counter(label):
	global counter2
	counter2 = 0
	label.config(text = counter2)
