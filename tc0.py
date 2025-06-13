#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  2 17:32:07 2025

@author: roman
"""

# Módulos externos

import numpy as np
import matplotlib as mpl
from matplotlib import pyplot as plt

# módulo de SciPy
from scipy import signal as sig

# Esta parte de código la agregamos SOLO en los notebooks para fijar el estilo de los gráficos.
fig_sz_x = 13
fig_sz_y = 7
fig_dpi = 80 # dpi
fig_font_size = 13

mpl.rcParams['figure.figsize'] = (fig_sz_x, fig_sz_y)
mpl.rcParams['figure.dpi'] = fig_dpi
plt.rcParams.update({'font.size':fig_font_size})

from pytc2.sistemas_lineales import analyze_sys, bodePlot, pzmap, pretty_print_bicuad_omegayq
from pytc2.general import print_latex, a_equal_b_latex_s

w0 = 1
ganancia_k = [1,10]

for valor_k in ganancia_k:
    
    num = np.array([0,1,-valor_k *w0])
    den = np.array([0,1,w0])

    H1 = sig.TransferFunction(num, den)
    _ = analyze_sys([H1], sys_name='Transferencia con a= {}'.format(valor_k))
