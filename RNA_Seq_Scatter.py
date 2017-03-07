###############################################################################
# Filename: RNA_Seq_Scatter.py                                                #
# Written by: Lon Blauvelt                                                    #
# Data, stylesheet, and guidance Provided by Prof. Christopher Vollmers       #
#                                                                             #
# Plot w/3 Panels                                                             #
# Creates a plot of RNA Seq Data from a text file                             #
# Graph has three panels: a main panel plotting the x/y of the seq data, and  #
# two histogram panels flanking the sides whose size reflects the number of   #
# dots along the x or y space each adjoins respectively.                      #
###############################################################################

import matplotlib.pyplot as plt
import matplotlib.patches as mplpatches
import numpy as np

# Location:
# /home/lifeisaboutfishtacos/.local/lib/python3.5/site-packages/matplotlib/mpl-data/stylelib
plt.style.use('vollmers')

# Set the size of the figure
plt.figure(figsize=(2, 2))

###############################################################################
# Read data and prepare it for plotting in each of the 3 panels.              #
# Data File: data.txt                                                         #
###############################################################################

x_list = []
y_list = []
gene_length_list = []

for line in open('data.txt'):
    split_line = line.strip().split('\t')
    gene_name = split_line[0]
    gene_length = int(split_line[1])
    x_value = int(split_line[2])
    y_value = int(split_line[3])
    x_list.append(x_value)
    y_list.append(y_value)
    gene_length_list.append(gene_length)

x_array = np.array(x_list)
y_array = np.array(y_list)
x_array_log = np.log2(x_array + 1)
y_array_log = np.log2(y_array + 1)

bins = np.arange(0, 30, 0.5)

###############################################################################
# Panel 1: Histogram of the number of dots along each "y = #" region flanked  #
###############################################################################

panel1 = plt.axes([0.2, 0.15, 0.125, 0.5])  # (left x-coord, bottom y-coord, extends x right, extends y up)

y_array_log_hist, bins1 = np.histogram(y_array_log, bins)

for step in np.arange(0, len(y_array_log_hist), 1):
    bottom = bins[step]
    left = 0 # 400 - y_array_log_hist[step]
    height = bins[step + 1] - bins[step]
    width = y_array_log_hist[step]

    rectangle1 = mplpatches.Rectangle((left, bottom), width, height, \
                                      linewidth=0.1, \
                                      facecolor=(0.5, 0.5, 0.5), \
                                      edgecolor=(0, 0, 0))
    panel1.add_patch(rectangle1)

panel1.set_xticks([0,400])
panel1.set_yticks([0,2,4,6,8,10,12,14])

# Set Axes Limits
panel1.set_xlim([400, 0])
panel1.set_ylim([0, 14])

# Turn On or Off Plot Axes
panel1.tick_params(axis='both', which='both', \
                   bottom='on', labelbottom='on', \
                   left='on', labelleft='on', \
                   right='off', labelright='off', \
                   top='off', labeltop='off')

###############################################################################
# Panel 2: Plot of RNA Seq Data Along the X and Y Axes.                       #
###############################################################################

panel2 = plt.axes([0.36, 0.15, 0.5, 0.5])  # (left x-coord, bottom y-coord, extends x right, extends y up)

panel2.scatter(x_array_log, y_array_log, \
               s=2, \
               alpha=0.3, \
               facecolor=(0, 0, 0), \
               edgecolor=(0, 0, 0),
               linewidth=0.1)

panel2.set_xticks([0,2,4,6,8,10,12,14])
# panel2.set_yticks([0,2,4,6,8,10,12,14]) ## Panel 2 Y-Axis TURNED OFF

# Set Axes Limits
panel2.set_xlim([0, 14])
panel2.set_ylim([0, 14])

# Turn On or Off Plot Axes
panel2.tick_params(axis='both', which='both', \
                   bottom='on', labelbottom='on', \
                   left='off', labelleft='off', \
                   right='off', labelright='off', \
                   top='off', labeltop='off')

###############################################################################
# Panel 3: Histogram of the number of dots along each "x = #" region flanked  #
###############################################################################

panel3 = plt.axes([0.36, 0.685, 0.5, 0.125])  # (left x-coord, bottom y-coord, extends x right, extends y up)

x_array_log_hist, bins1 = np.histogram(x_array_log, bins)

for step in np.arange(0, len(x_array_log_hist), 1):
    left = bins[step]
    bottom = 0
    width = bins[step + 1] - bins[step]
    height = x_array_log_hist[step]

    rectangle1 = mplpatches.Rectangle((left, bottom), width, height, \
                                      linewidth=0.1, \
                                      facecolor=(0.5, 0.5, 0.5), \
                                      edgecolor=(0, 0, 0))
    panel3.add_patch(rectangle1)

# Set Axes Limits
panel3.set_xlim([0, 14])
panel3.set_ylim([0, 400])

# panel3.set_xticks([0,400]) ## Panel 3 X-Axis TURNED OFF
panel3.set_yticks([0,400])

# Turn On or Off Plot Axes
panel3.tick_params(axis='both', which='both', \
                   bottom='off', labelbottom='off', \
                   left='on', labelleft='on', \
                   right='off', labelright='off', \
                   top='off', labeltop='off')

plt.savefig('RNA_Seq_Scatter.pdf')
