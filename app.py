compounds = ['CO2', 'N2', 'CH4', 'C2H6', 'C3H8', 'C4H10']
mole_fraction = [0.12, 0.021, 0.8, 0.042, 0.013, 0.004]
weight_fraction = [0.12, 0.021, 0.8, 0.042, 0.013, 0.004]
MOLAR_VOLUME = 379.3  #scf/lbmole


from CO2 import CO2
HCin = 20000 #scf
FE = 0.98
CO2_emission = CO2(compounds, mole_fraction, HCin, FE)
print(CO2_emission.inletvolume_molefraction())