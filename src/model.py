import numpy as np
from scipy.integrate import solve_ivp

# Basisparametre
p_nad = 0.08
q_nad = 0.06
eps   = 0.05
c_epi = 1.0

k_mit_base = 0.03
k_mit_late = 0.10
t_mit_on   = 20.0

k_agg   = 0.03
k_clear = 0.04

# Modulatorer
alpha_NAD_MYR   = 0.25
alpha_mit_MYR   = 0.45
alpha_clear_MYR = 0.20

alpha_NAD_PEA = 0.15
alpha_mit_PEA = 0.30

alpha_NAD_ASH   = 0.20
alpha_mit_ASH   = 0.25
alpha_agg_ASH   = 0.20
alpha_clear_ASH = 0.15

def heaviside(x):
    return 0 if x < 0 else 1

def A(t):
    return 1.0 / (1 + np.exp(-(t-12)/2))

def odes(t, y, MYR, PEA, ASH):
    NAD, F_mit, F_crowd = y

    q_nad_eff      = q_nad * (1 - alpha_NAD_MYR*MYR - alpha_NAD_PEA*PEA - alpha_NAD_ASH*ASH)
    k_mit_late_eff = k_mit_late * (1 - alpha_mit_MYR*MYR - alpha_mit_PEA*PEA - alpha_mit_ASH*ASH)
    k_agg_eff      = k_agg * (1 - alpha_agg_ASH*ASH)
    k_clear_eff    = k_clear * (1 + alpha_clear_MYR*MYR + alpha_clear_ASH*ASH)

    dNAD_dt = p_nad - q_nad_eff * NAD

    H = heaviside(t - t_mit_on)
    dFmit_dt = k_mit_base*(1 - F_mit) + k_mit_late_eff*H

    dFcrowd_dt = -k_clear_eff*A(t) + k_agg_eff*(1 - F_crowd)

    return [dNAD_dt, dFmit_dt, dFcrowd_dt]
