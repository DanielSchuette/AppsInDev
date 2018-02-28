'''
developed by Daniel (d.schuette@online.de)
This is a test .app to test tkinter and py2app
latest version: v0.03 (as of 02/28/2018)
-> runs with python 2.7.14 and python 3.6.x
'''

# identify python version and tinkter that should be used
import sys
if sys.version_info[0] < 3:
    print("You're running Python 2.x")
    import Tkinter as tk
else:
    print("You're running Python 3.x")
    import tkinter as tk

    