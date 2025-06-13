#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 11 17:47:17 2025

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

#Parametros ya dados
f0 = 10e3
normalizacion_frec = 2*np.pi*f0
C_des= 1e-9
Q = 20

#Componentes normalizados
C = C2 = 1
R = Q
R1 = R4 = 9
R3 = R5 = 1

#normalizacion de impedancia
normalizacion_z = C/(C_des * normalizacion_frec)

#desnormalizacion de componentes
C2_des = C_des
R_des = Q * normalizacion_z
R1_des = R4_des = 9 * normalizacion_z
R3_des = R5_des = 1 * normalizacion_z

num = np.array([0,1/(C_des * R_des),0])
den = np.array([1,1/(C_des * R_des),(R4_des/C_des * C_des * R1_des * R3_des * R5_des)])
    
H1 = sig.TransferFunction(num, den)
display(H1)
print_latex(a_equal_b_latex_s('H_d(s)', pretty_print_bicuad_omegayq(num,den,displaystr=False)))
_ = analyze_sys([H1],sys_name = 'Pasabanda Q = {:3.1f}'.format(Q))