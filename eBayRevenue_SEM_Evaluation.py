import warnings
warnings.filterwarnings("ignore")
import sys
import os
sys.path.append(os.path.abspath("../"))
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
plt.style.use('ggplot')
from tqdm import tqdm
from synthdid.model import SynthDID  

raw_df = pd.read_csv('/Users/macbook/Downloads/PaidSearch.csv')

Y_mat=raw_df.pivot(index=('dma','treated'), columns=("date",'treatment_period'))["revenue"]
Y_mat=Y_mat.sort_values(by=['treated'], axis=0).sort_values(by=['treatment_period'], axis=1)
Y_mat.shape

logY=np.log(Y_mat)

control =logY.iloc[:68,:]
treat = logY.iloc[68:,:]
rep_treat = np.mean(treat,axis =0)
CollapsedY = control.append(rep_treat,ignore_index = True)
CollapsedY.shape

pre_treat = [0,50]
post_treat = [51,113]
avg_treat = [68]
Y_input = CollapsedY.T
base_mod = SynthDID(Y_input, pre_treat, post_treat, avg_treat)

base_mod.fit(zeta_type="base")
hat_omega_simple = base_mod.estimated_params(model="sc")
base_mod.plot(model="did")

base_mod.fit(zeta_type="base")
hat_omega_simple = base_mod.estimated_params(model="sc")
base_mod.plot(model="sc")

base_mod.fit(zeta_type="base")
hat_omega_simple = base_mod.estimated_params(model="sc")
base_mod.plot(model="sdid")

hat_omega = base_mod.estimated_params(model="sc")
hat_omega_sdid, hat_lambda_sdid, = base_mod.estimated_params()

base_mod.cal_se(algo="placebo", replications=200)

base_mod.summary(model="did")

base_mod.summary(model="sc")

base_mod.summary(model="sdid")
