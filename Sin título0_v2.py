#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 12 00:00:19 2025

@author: roman
"""

# Librerías externas NumPy, SciPy y Matplotlib
from scipy.signal import TransferFunction
import matplotlib.pyplot as plt
import numpy as np


# Librería de TC2, esta la vas a usar mucho
from pytc2.sistemas_lineales import pzmap, bodePlot

# Esta parte de código la agregamos SOLO en los notebooks para fijar el estilo de los gráficos.
#
# Setup inline graphics: Esto lo hacemos para que el tamaño de la salida, 
# sea un poco más adecuada al tamaño del jupyter notebook documento

# algún bug cuando lo hice:
plt.figure(1)
plt.close(1)

import matplotlib as mpl

fig_sz_x = 13
fig_sz_y = 7
fig_dpi = 80 # dpi
fig_font_size = 11

mpl.rcParams['figure.figsize'] = (fig_sz_x, fig_sz_y)
mpl.rcParams['figure.dpi'] = fig_dpi
plt.rcParams.update({'font.size':fig_font_size})

w0 = 1
k_param = [0, 1, 10]

for k in range(len(k_param)):
    
    my_tf = TransferFunction([1, -k_param[k] * w0], [1, w0]) # k_param = R2/R1
    
    bodePlot(my_tf, fig_id=1, filter_description = 'k = {:d}'.format(k_param[k]))
    pzmap(my_tf, fig_id=2, filter_description = 'K={:d}'.format(k_param[k]))