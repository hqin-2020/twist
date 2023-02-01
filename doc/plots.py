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

if optimize_over_ell == 0:
    filename_ell = "azt_"*str(round(alpha_z_tilde_ex,3)).replace(".","")*"_ell_ex_"*str(round(ell_ex,3)).replace(".","")+"_"
elif optimize_over_ell == 1:
    filename_ell = "azt_"*str(round(alpha_z_tilde_ex,3)).replace(".","")*"_ell_opt_"

npz = np.load("output/" + filename_ell + filename + ".npz")
def trans(x):
    return np.exp(x)/(np.exp(x)+1)
def read_csv(name):
    h1 = pd.DataFrame(npz[name])
    h1.index = trans(np.linspace(-18,18,1001))
    h1.columns = np.linspace(-1,1,201)
    return h1
h1 = read_csv('h1')
h2 = read_csv('h2')
hz = read_csv('hz')
fig, ax = plt.subplots(1,1,figsize = (8,8))
sns.lineplot(data = h1[0],label = r"$-H_1$")
sns.lineplot(data = h2[0],label = r"$-H_2$")
sns.lineplot(data = hz[0],label = r"$-H_z$")
ax.set_title('alpha_z_tilde'+str(alpha_z_tilde_ex)+'_ell_star_'+str(npz['ell_star']))
fig.tight_layout()
fig.savefig(filename_ell + filename+'H.png', dpi = 1200)
plt.show()

