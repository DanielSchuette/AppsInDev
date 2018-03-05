'''
developed by Daniel (d.schuette@online.de)
This is a .app for the analysis of calcium imaging results
latest version: v0.01 (as of 03/02/2018)
-> runs with python 2.7.14 and with python 3.6.x
repository: https://github.com/DanielSchuette/AppsInDev.git
'''
import tifffile as tiff # module downloaded from https://github.com/blink1073/tifffile.git
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
from pylab import *
import cv2 as cv2

# program start 
print("\n" + "********************************" + "\n")

# enable popup windows (plt.show("hold") is required as well; because of ST3; you might want to change that behavior)
matplotlib.interactive(True)

# read in .lsm data and return a numpy array with certain dimensions: CHANGE FILE PATH!!
file_path = "../../Yale/Projects/calcium_imaging/20180125_20180213/20180125_SKHep_1.lsm"
image = tiff.imread(file_path)
print("You successfully imported a .lsm file from" + "\n" + str(file_path) + "." + "\n")
print("Image dimensions: " + str(image.shape)) # [1, 1, no_of_pictures, height, width]
np.amax(image) # max value of 255; that needs to be transformed to range(0, 1)

# select the first image of the movie 
first_image = (image[0, 0, 1, 0:512, 0:512])
first_image_zoomed = first_image[100:300, 100:300]

# write tiffs for inspection to active working directory
tiff.imsave("tmp.tif", image) # allows to save .lsm picture as a .tiff
tiff.imsave("first_image.tif", first_image)

# check image dimensions before plotting
print("\n" + "The plotted images is of " + str(type(first_image)) + " and a " + str(first_image.dtype) 
	  + " with dimensions " + str(first_image.shape) + ".")

# plot your image
plt.figure()
plt.subplot(231)
ax2 = plt.subplot(231)
ax2.tick_params(bottom = False, left = False)
ax2.tick_params(labelbottom = False, labelleft = False)
plt.imshow(first_image, cmap = "viridis", interpolation = "bicubic") # colormaps "jet", "gray, "viridis" work
# "bicubic" interpolation smoothes the edges, "nearest" leads to a more pixelated figure
plt.colorbar() # adds a colorbar according to latest 'cmap' that was specified
plt.title("First Image of ~400")

# create a new figure that extracts prominent features 
plt.subplot(232)
ax1 = plt.subplot(232)
# show contours with origin upper left corner
contour(first_image, origin = "image", cmap = "gray")
# Hide the axis but leave the spine
ax1.tick_params(bottom = False, left = False)
ax1.tick_params(labelbottom = False, labelleft = False)
plt.title("Feature Extraction without\nPrior Background Reduction")


# a boxplot helps to see the distribution of pixel values
plt.subplot(233)
plt.hist(first_image.ravel(), bins = 256, range = (0.0, 256.0), fc = "k", ec = "k")
plt.yscale("log", nonposy = "clip")
plt.title("Histogram of Gray Scale\nValues in First Image")

# mask different gray scale values from the image
tmp1 = first_image
tmp1[tmp1 < 50] = 0

plt.subplot(235)
ax3 = plt.subplot(235)
contour(tmp1, origin = "image", cmap = "gray")
plt.title("Gray Scale Cutoff = 50")
ax3.tick_params(bottom = False, left = False)
ax3.tick_params(labelbottom = False, labelleft = False)

tmp2 = first_image
tmp2[tmp2 < 100] = 0

plt.subplot(236)
ax4 = plt.subplot(236)
contour(tmp2, origin = "image", cmap = "gray")
plt.title("Gray Scale Cutoff = 100")
ax4.tick_params(bottom = False, left = False)
ax4.tick_params(labelbottom = False, labelleft = False)

# mask values from image
pixel_values = []
cutoffs = []
tmp3 = first_image
for cutoff in range(256):
	print(cutoff)
	mask = tmp3 < cutoff
	tmp3[mask] = 0
	pixel_values.append(mean(mask) * 100)
	cutoffs.append(cutoff)

plt.subplot(234)
plt.grid(False)
plt.scatter(x = cutoffs, y = pixel_values, s = 20, c = "darkred")
plt.title("Number of Pixels Below Certain Cutoff")
plt.xlabel("Gray Scale Value Cutoff")
plt.ylabel("Percentage of Cells Below Cutoff")
plt.show("hold")

# program end
print("\n" + "********************************" + "\n")
