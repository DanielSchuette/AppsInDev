"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app
"""
import ez_setup
ez_setup.use_setuptools()
from setuptools import setup
# from distutils.core import setup
import py2app
from plistlib import Plist
import os
import sys

APP = ['DanielsTestApp_v0.01.py']
DATA_FILES = ['giphy-downsized.gif']
ICON = '/Users/daniel/Projects_myApplications/AppInDev/if_application-x-python_8974.icns'

name = 'DanielsTestApp_v0.01'
version = '0.0.1'

if sys.platform == 'darwin':
    extra_options = dict(
        setup_requires=['py2app'],
        app=[APP],
        # Cross-platform applications generally expect sys.argv to
        # be used for opening files.
        options=dict(py2app=dict(argv_emulation=True)),
    )
elif sys.platform == 'win32':
    extra_options = dict(
        setup_requires=['py2exe'],
        app=[APP],
    )
else:
     extra_options = dict(
         # Normally unix-like platforms will use "setup.py install"
         # and install the main script as such
         scripts=[APP],
)

setup(
    app=APP,
    data_files=DATA_FILES,
    options=dict(
    	py2app=dict(
    		iconfile=ICON,
    		packages=['matplotlib', 'numpy'],
    		site_packages=True,
    		resources=[ICON],
    		plist=dict(
    			CFBundleName = name,
    			CFBundleShortVersionString = version,
    			CFBundleGetInfoString = name+" "+ version,
    			CFBundleExecutable = name,
    		),
    	),
    ),
)
