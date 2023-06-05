from collections.abc import Iterable
MOLAR_VOLUME = 379.3  #scf/lbmole
def CO2_lbmole_lb(par):
    '''This function converts lbmole CO2/time to lb CO2/time
    
    where:
        1 lbmole CO2 = 44lb CO2
    '''
    return 44*par

def lb_tonnes(par):
    '''This function converts pounds to tonnes.
    
        where:
        1 tonnes = 2204.62lb
    '''
    return (1/2204.62)*par

def scf_lbmole(volume_rate):
    '''This function converts volumetric flowrate in scf/time to molar flowrate in lbmole/time
    Molar volume of a gas at Standard temperature and pressure is given as:
    1 lbmole gas = 379.3scf gas
    
    Arguments: volume_rate in scf/time  
    '''
    molar_flowrate = volume_rate*(1/MOLAR_VOLUME)
    return molar_flowrate

def molefraction_massfraction(mole_fraction:Iterable[float], molecular_weight:Iterable[float]):
    '''This function converts mole fraction to weight or mass fraction.
    Arguments: 
    1) mole fraction(Array)
    2) Molecular weight of each gas component in lb/lbmole
    
    '''
    x = zip(mole_fraction, molecular_weight)
    product_list = []
    for a, b in x:
        product_list.append(a*b/molecular_weight_of_mixture_molefraction(mole_fraction, molecular_weight))
    return product_list

def massfraction_molefraction(weight_fraction:Iterable[float], molecular_weight:Iterable[float]):
    '''This function converts mole fraction to weight or mass fraction.
    Arguments: 
    1) weight fraction(Array)
    2) Molecular weight of each gas component in lb/lbmole
    
    '''
    x = zip(weight_fraction, molecular_weight)
    product_list = []
    for a, b in x:
        product_list.append(a*molecular_weight_of_mixture_molefraction(mole_fraction, molecular_weight)/b)
    return product_list