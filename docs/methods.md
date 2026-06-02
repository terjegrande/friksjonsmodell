# Methods – Friksjonsmodell

Modellen består av tre ODE-moduler:
1. NAD+-dynamikk
2. Mitokondriell friksjon
3. Crowding/proteostase

Epigenetisk friksjon beregnes som:
F_epi = c_epi / (NAD + eps)

Total friksjon:
F_total = 0.33*F_epi + 0.33*F_mit + 0.34*F_crowd

Modulatorer (MYR, PEA, ASH) påvirker q_nad, k_mit_late, k_clear og k_agg.
