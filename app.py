


from CO2 import CO2
from CH4 import CH4
from emission import Emission
FE = 0.98
# EXHIBIT 1
compounds = ['CO2', 'N2', 'CH4', 'C2H6', 'C3H8', 'C4H10']
composition = [0.12, 0.021, 0.8, 0.042, 0.013, 0.004] # mole/weight fraction
HC = 20000000 # scf/year

print('EXHIBIT 1: \n')
emission1 = Emission(compounds, composition, HC, FE)
print('Data Table \n')
print(emission1.carbon_content_fuel_mixture_mole_basis())
# print('------ \n')
# CO2_emission = CO2(compounds, composition, HC, FE)
# print('CO2 EMISSION CALCULATION')
# print('Inlet Volume Known, using mole fraction')
# print(CO2_emission.inletvolume_molefraction(), 'tonnes/year')
# print('----------------- \n')
# print('Inlet Mass Known, using weight fraction')
# print(CO2_emission.inletmass_weightfraction(), 'tonnes/year')
# print('----------------- \n')
# print('Outlet Volume Known, using mole fraction')
# print(CO2_emission.outletvolume_molefraction(), 'tonnes/year')
# print('----------------- \n')
# print('Outlet Mass Known, using weight fraction')
# print(CO2_emission.outletmass_weightfraction(), 'tonnes/year')
# print('----------------- \n \n')

# CH4_emission = CH4(compounds, composition, HC, FE)
# print('CH4 EMISSION CALCULATION')
# print('Inlet Volume Known, using mole fraction')
# print(CH4_emission.inletvolume_molefraction(), 'tonnes/year')
# print('----------------- \n')
# print('Inlet Mass Known, using weight fraction')
# print(CH4_emission.inletmass_weightfraction(), 'tonnes/year')
# print('----------------- \n')
# print('Outlet Volume Known, using mole fraction')
# print(CH4_emission.outletvolume_molefraction(), 'tonnes/year')
# print('----------------- \n')
# print('Outlet Mass Known, using weight fraction')
# print(CH4_emission.outletmass_weightfraction(), 'tonnes/year')
# print('----------------- \n \n')


# EXHIBIT 2
compounds = ['CH4', 'C2H6', 'C3H8', 'C4H10','C5H12','C6H14', 'CO2', 'N2']
composition = [0.0273, 0.0085, 0.0135, 0.0099, 0.0083, 0.0216, 0.9043, 0.0066] # mole/weight fraction
HC = 7380 # lb

print('EXHIBIT 2: \n')
emission2 = Emission(compounds, composition, HC, FE)
print('Data Table \n')
print(emission2.carbon_content_fuel_mixture_mole_basis())
# print('------ \n')
# CO2_emission = CO2(compounds, composition, HC, FE)
# print('CO2 EMISSION CALCULATION')
# print('Inlet Volume Known, using mole fraction')
# print(CO2_emission.inletvolume_molefraction(), 'tonnes/year')
# print('----------------- \n')
# print('Inlet Mass Known, using weight fraction')
# print(CO2_emission.inletmass_weightfraction(), 'tonnes/year')
# print('----------------- \n')
# print('Outlet Volume Known, using mole fraction')
# print(CO2_emission.outletvolume_molefraction(), 'tonnes/year')
# print('----------------- \n')
# print('Outlet Mass Known, using weight fraction')
# print(CO2_emission.outletmass_weightfraction(), 'tonnes/year')
# print('----------------- \n \n')

# CH4_emission = CH4(compounds, composition, HC, FE)
# print('CH4 EMISSION CALCULATION')
# print('Inlet Volume Known, using mole fraction')
# print(CH4_emission.inletvolume_molefraction() , 'tonnes/year')
# print('----------------- \n')
# print('Inlet Mass Known, using weight fraction')
# print(CH4_emission.inletmass_weightfraction(), 'tonnes/year')
# print('----------------- \n')
# print('Outlet Volume Known, using mole fraction')
# print(CH4_emission.outletvolume_molefraction(), 'tonnes/year')
# print('----------------- \n')
# print('Outlet Mass Known, using weight fraction')
# print(CH4_emission.outletmass_weightfraction(), 'tonnes/year')
# print('----------------- \n \n')