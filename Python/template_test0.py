import numpy as np
from skimage.io import imshow, imread
from skimage.color import rgb2gray
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from skimage.feature import match_template
from skimage.feature import peak_local_max
import time

sample = imread('python\image0.jpg')
#sample_g = rgb2gray(sample)
#fig, ax = plt.subplots(1,2,figsize=(10,5))
#ax[0].imshow(sample)
#ax[1].imshow(sample_g,cmap='gray')
#ax[0].set_title('Colored Image',fontsize=15)
#ax[1].set_title('Grayscale Image',fontsize=15)
#plt.show()

patch_x_min=1530
patch_x_max=1565
patch_y_min=1635
patch_y_max=1665

fig, ax = plt.subplots(1,2,figsize=(10,10))
ax[0].imshow(sample,cmap='gray')
ax[0].add_patch(Rectangle((patch_x_min, patch_x_max), patch_x_max-patch_x_min, patch_y_max-patch_y_min, edgecolor='b', facecolor='none'));
ax[0].set_title('Patch Location',fontsize=15)
#Showing Patch
patch = sample[patch_x_min:patch_x_max, patch_y_min:patch_y_max]
ax[1].imshow(patch,cmap='gray')
ax[1].set_title('Patch',fontsize=15)
plt.show()

sample2 = imread('python\image1.jpg')
t0 = time.time()
sample_mt = match_template(sample2, patch)

fig, ax = plt.subplots(1,2,figsize=(10,10))
ax[0].imshow(sample,cmap='gray')
ax[1].imshow(sample_mt,cmap='gray')
ax[0].set_title('Grayscale',fontsize=15)
ax[1].set_title('Template Matching',fontsize=15);

fig, ax = plt.subplots(1,2,figsize=(10,10))
ax[0].imshow(sample,cmap='gray')
ax[1].imshow(sample,cmap='gray')

patch_width, patch_height = patch.shape
a=[]
for x, y in peak_local_max(sample_mt, threshold_abs=0.76):
    rect = plt.Rectangle((y, x), patch_height, patch_width, color='r', 
                         fc='none')
    ax[1].add_patch(rect)
    #a.append([x,y])
ax[0].set_title('Grayscale',fontsize=15)
ax[1].set_title('Template Matched',fontsize=15);
plt.show()