# simple entry widget in tkinter
import tkinter as tk

root = tk.Tk()
root.config(bg = "light yellow")
root.title("Simple Tkinter Window")

tk.Label(root, text ="First Name", bg = "light yellow").grid(row = 0, column = 0, sticky = tk.W)
tk.Label(root, text ="Last Name", bg = "light yellow").grid(row = 1, column = 0, sticky = tk.W)
entry1 = tk.Entry(root, bg = "light blue", highlightbackground = "light yellow", font = "Calibri 16 italic")
entry1.grid(row = 0, column = 1)
entry2 = tk.Entry(root, bg = "light blue", highlightbackground = "light yellow", font = "Calibri 16 italic")
entry2.grid(row = 1, column = 1)


var1 = tk.StringVar()
var1.set("No input yet!")

entry_list = [entry1, entry2]
def showInput():
   global var1
   print("Your Name is %s %s" % (entry1.get(), entry2.get()))
   # make sure that a first and last name were entered
   if(entry1.get() != "" and entry2.get() != ""):
   	var1.set("Your Name is %s %s" % (entry1.get(), entry2.get()))
   else:
   	var1.set("Please enter your first and last name.")
   # delete all entered string when clicking the 'Show input' button
   for entry in entry_list:
   	entry.delete(0, tk.END)

def callback1(event):
	print("clicked at", event.x, event.y)
	entry1.delete(0, tk.END)
	for entry in entry_list:
		entry.config(font = "Arial 20")
   	
def callback2(event):
	print("clicked at", event.x, event.y)
   	entry2.delete(0, tk.END)	

# introduce some buttons
button1 = tk.Button(root, text = "Show Input", font = "Arial 16 italic", command = showInput, highlightbackground = "light yellow")
# cave: for a 'label', an 'activebackground = ' argument would be required!
button1.grid(row = 2, column = 1, pady = 16)   

button2 = tk.Button(root, text = "Quit", font = "Arial 16 italic", command = root.quit, highlightbackground = "light yellow")
button2.grid(row = 2, column = 0, pady = 16)

# turns button 'active' and GUI a bit before turning back to 'normal' what imitates a "button-pressed"-effect
import time as time
button_list = [button1, button2]
def buttonPress(*args):
	for button in button_list:
		button.config(state = "active")
    	button.update()
    	time.sleep(0.5)
    	button.config(state = "normal")

button1.bind("<Button-1>", buttonPress)
button2.bind("<Button-1>", buttonPress)

# introduce some labels    	
label1 = tk.Label(root, textvariable = var1, font = "Arial 20", bg = "light blue") # this is a dynamic label
label1.grid(row = 3, column = 1, pady = 4)

entry1.insert(10, "Click and write...")
entry2.insert(10, "Click and write...")

entry1.bind("<Button-1>", callback1) # hopefully, that feeds "<Button-1>" into 'callback()'
entry2.bind("<Button-1>", callback2) # hopefully, that feeds "<Button-1>" into 'callback()'

# start the main loop to make a GUI window appear
root.mainloop()
