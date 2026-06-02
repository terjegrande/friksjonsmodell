import numpy as np
from scipy.integrate import solve_ivp
from model import odes, c_epi, eps

t_span = (0, 48)
t_eval = np.linspace(0, 48, 600)

def simulate(MYR, PEA, ASH):
    y0 = [1.0, 0.5, 0.5]
    sol = solve_ivp(odes, t_span, y0, t_eval=t_eval, args=(MYR, PEA, ASH))
    NAD, F_mit, F_crowd = sol.y
    F_epi = c_epi / (NAD + eps)
    F_total = 0.33*F_epi + 0.33*F_mit + 0.34*F_crowd
    return sol.t, F_total, F_epi, F_mit, F_crowd, NAD
