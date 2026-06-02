import matplotlib.pyplot as plt
from simulate import simulate

t, F0, _, _, _, _ = simulate(0,0,0)
t, F_M, _, _, _, _ = simulate(1,0,0)
t, F_P, _, _, _, _ = simulate(0,1,0)
t, F_A, _, _, _, _ = simulate(0,0,1)

plt.figure(figsize=(7,5))
plt.plot(t, F0, 'k-', label='Baseline')
plt.plot(t, F_M, 'b-', label='Myricetin')
plt.plot(t, F_P, 'r-', label='PEA')
plt.plot(t, F_A, 'g-', label='Ashwagandha')

plt.xlabel("Tid (timer)")
plt.ylabel("Total friksjon")
plt.title("Simulert U-kurve (0–48 t)")
plt.legend()
plt.grid(True)
plt.tight_layout()

plt.savefig("figure1.svg", format="svg", bbox_inches="tight")
plt.savefig("figure1.pdf", format="pdf", bbox_inches="tight")
