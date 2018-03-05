#tmp.py
import tifffile as tiff # module downloaded from https://github.com/blink1073/tifffile.git
import numpy as np
import matplotlib as mpl

# read in .lsm data and return a numpy array 
image = tiff.imread("../../Yale/Projects/calcium_imaging/20180125_20180213/20180125_SKHep_1.lsm")
print(type(image)) # 'numpy.ndarray'
print(image.shape) # [1, 1, no_of_pictures, width, height]
print(image[0][0][0][0:2][0:2])
tiff.imsave("tmp.tif", image) # allows to save .lsm picture as a .tiff

# display of more than one plot in a window is possible
# (fig, (full, full2, zoom, zoom2)) = plt.subplots(ncols = 4, figsize = (12, 6)) 
# full.imshow(first_image, cmap = "viridis", interpolation = "bicubic")
# full2.imshow(first_image, cmap = "viridis", clim = (20.0, 256.0), interpolation = "bicubic")
# zoom.imshow(first_image_zoomed, cmap = "viridis", interpolation = "bicubic")
# zoom2.imshow(first_image_zoomed, cmap = "viridis", clim = (20.0, 256.0), interpolation = "bicubic")
# plt.show("hold")

# Select ROI with openCV
# r = cv2.selectROI(first_image)
# print(r)
# Crop image
# imCrop = first_image[int(r[1]):int(r[1]+r[3]), int(r[0]):int(r[0]+r[2])]
# Display cropped image
# cv2.imshow("Image", imCrop)
# cv2.waitKey(0)