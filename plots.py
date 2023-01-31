import os
import sys
import numpy as np
np.set_printoptions(suppress=True)
np.set_printoptions(linewidth=200)
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
pd.options.display.float_format = '{:.3g}'.format
sns.set(font_scale = 1.4, rc={"grid.linewidth": 1,'grid.color': '#b0b0b0', 'axes.edgecolor': 'black',"lines.linewidth": 3.0}, style = 'whitegrid')

import argparse
parser = argparse.ArgumentParser(description="parameter settings")
parser.add_argument("--symmetric_returns",type=int,default=0)
parser.add_argument("--state_dependent_xi",type=int,default=0)
parser.add_argument("--optimize_over_ell",type=int,default=0)
parser.add_argument("--ell_ex",type=float,default=0.05)
parser.add_argument("--alpha_z_tilde_ex",type=float,default=0.05)
args = parser.parse_args()

symmetric_returns = args.symmetric_returns
state_dependent_xi = args.state_dependent_xi
optimize_over_ell = args.optimize_over_ell
ell_ex = args.ell_ex
alpha_z_tilde_ex = args.alpha_z_tilde_ex

if symmetric_returns == 1:
    if state_dependent_xi == 0:
        filename = "model_sym_HS.npz"
    elif state_dependent_xi == 1:
        filename = "model_sym_HSHS.npz"
    elif state_dependent_xi == 2:
        filename = "model_sym_HSHS2.npz"
elif symmetric_returns == 0:
    if state_dependent_xi == 0:
        filename = "model_asym_HS.npz"
    elif state_dependent_xi == 1:
        filename = "model_asym_HSHS.npz"
    elif state_dependent_xi == 2:
        filename = "model_asym_HSHS2.npz"

if optimize_over_ell == 1:
    filename_ell = "azt_"*str(round(alpha_z_tilde_ex,3)).replace(".","")*"_ell_ex_"*str(round(ell_ex,3)).replace(".","")
elif optimize_over_ell == 0:
    filename_ell = "azt_"*str(round(alpha_z_tilde_ex,3)).replace(".","")*"_ell_opt_"

