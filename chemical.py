from chemicals import *
import pandas as pd
import re
compound = ['CO2', 'N2', 'CH4', 'C2H6', 'C3H8', 'C4H10']
mole_fraction = [0.12, 0.021, 0.8, 0.042, 0.013, 0.004]
weight_fraction = [0.12, 0.021, 0.8, 0.042, 0.013, 0.004]
MOLAR_VOLUME = 379.3  #scf/lbmole

def convert_lbmole_CO2_to_lbCO2():
    '''This function converts lbmole CO2/time to lb CO2/time
    
    where:
        1 lbmole CO2 = 44lb CO2
    '''
    return 44

def convert_lb_to_tonnes():
    '''This function converts pounds to tonnes.
    
        where:
        1 tonnes = 2204.62lb
    '''
    return 1/2204.62

def find_hydrocarbons_in_gas_mixture(mixture):
    '''
    This function returns only the hydrocarbon components present in a mixture of gases.
    '''
    # create a regular expression in python for strings that contains on C and H, and digits between the C and H
    pattern = r'^[CH\d]+$'
    list_of_hydrocarbons = []
    for i in identifiers.pubchem_db:
        if re.search(pattern, i.formula):
            for j in mixture:
                if i.formula == j or i.common_name == j:
                    list_of_hydrocarbons.append(i)
        else:
            None
    return list_of_hydrocarbons

# print(find_hydrocarbons_in_gas_mixture(compound))

def get_molecular_weight_list(mixture):
    '''This function returns the list of molecular weight for the components in a gas mixture.
        The function Receives an array or list of the common name or molecular formular of the gas components as argument.
    '''
    # list of gas components.

    list_of_components = []
    list_of_molecular_weight = []
    list_of_molecular_formula = []
    for i in identifiers.pubchem_db:
        for j in mixture:
            if i.formula == j or i.common_name == j:
                list_of_components.append(i.common_name)
                list_of_molecular_weight.append(i.MW)
                list_of_molecular_formula.append(i.formula)
            else:
                None

    # Create a pandas dataframe from three lists of column names Compound, Formula, and Molecular weight.
    data = {
        'Compound': list_of_components,
        'Formula': list_of_molecular_formula,
        'Molecular Weight': list_of_molecular_weight
    }
    df = pd.DataFrame(data)

    return df

# print(get_molecular_weight_list(compound))

def adjusted_composition(compound, composition):
    '''This function takes the mole fraction or weight fraction of the gas mixture as argument and returns a list of the adjusted mole fraction of weight fraction.'''

    # combine two lists, compound and composition into a dictionary of key and value pair.
    dictionary = dict(zip(compound, composition))
    included_list = find_hydrocarbons_in_gas_mixture(compound)
    for key, value in dictionary.items():
        if key in [i.formula for i in included_list]:
            dictionary[key] = value  # Set value to value if key is in include_list
        else:
            dictionary[key] = 0 # Set value to value if key is not in include_list

    # find the sum of the new dictionary values when non-hydrocarbon components are set to zero
    sum_composition = sum(dictionary.values())
    for key, values in dictionary.items():
        dictionary[key] = values/sum_composition
    return dictionary

# print(pd.Series(adjusted_composition(compound, mole_fraction).values()))

def carbon_ratio(compound):
    matches = re.findall(r"C(\d+)H", compound)
    if compound == 'CH4':
        digits = 1
    elif matches == []:
        digits = None
    else:
        digits = matches[0]
    return digits

def adjusted_composition_and_molecular_weight_table(compound, composition):

    # List to define the sorting order
    sorting_order = list(adjusted_composition(compound, composition))

    # Sort the DataFrame based on the sorting_order list
    df_sorted = get_molecular_weight_list(compound).sort_values(by='Formula', key=lambda x: x.map({value: i for i, value in enumerate(sorting_order)})).reset_index(drop=True)

    # Append adjusted composition to sorted dataFrame
    df_sorted['Adjusted Composition'] = pd.Series(adjusted_composition(compound, composition).values())


    # Append Carbon Ratio to the dataframe
    df_sorted['Carbon Ratio'] = df_sorted['Formula'].apply(lambda formula: carbon_ratio(formula))
    return df_sorted.fillna(0)


def carbon_content_mole_basis():
    data_table = adjusted_composition_and_molecular_weight_table(compound, mole_fraction)
    data_table['Mole Fraction'] = pd.Series(mole_fraction)
    data_table = data_table.fillna(0)
    mole_fraction_carbonratio = lambda row: row['Mole Fraction']*float(row['Carbon Ratio'])

    data_table['Carbon Content'] = data_table.apply(mole_fraction_carbonratio, axis=1)

    return data_table

# print(carbon_content_mole_basis())

def carbon_content_weight_basis():
    data_table = adjusted_composition_and_molecular_weight_table(compound, weight_fraction)
    data_table['Weight Fraction'] = pd.Series(weight_fraction)
    data_table = data_table.fillna(0)
    mole_fraction_carbonratio = lambda row: row['Adjusted Composition']*float(row['Carbon Ratio'])*12/row['Molecular Weight']

    data_table['Carbon Content'] = data_table.apply(mole_fraction_carbonratio, axis=1)

    return data_table
# print(carbon_content_weight_basis())

def carbon_content_fuel_mixture_mole_basis():
    C_mixture = sum(carbon_content_mole_basis()['Carbon Content'])
    return C_mixture

def carbon_content_fuel_mixture_weight_basis():
    C_mixture = sum(carbon_content_weight_basis()['Carbon Content'])
    return C_mixture

def mass_CO2_mole_composition_basis(compound, composition):
    '''Mass of CO2 in the flared stream based on CO2 composition of the inlet stream'''
    dictionary = dict(zip(compound, composition))
    co2_composition = dictionary['CO2']
    return co2_composition

def CH4_composition(compound, composition):
    '''CH4 composition'''
    dictionary = dict(zip(compound, composition))
    CH4_composition = dictionary['CH4']
    return CH4_composition

def convert_scf_to_lbmole(volume_rate):
    '''This function converts volumetric flowrate in scf/time to molar flowrate in lbmole/time
    Molar volume of a gas at Standard temperature and pressure is given as:
    1 lbmole gas = 379.3scf gas
    
    Arguments: volume_rate in scf/time  
    '''
    molar_flowrate = volume_rate*(1/MOLAR_VOLUME)
    return molar_flowrate

def CO2_emissions_inlet_known_volume_mole_basis(HCin, FUEL_EFFICIENCY):
    '''
    This function calculates the Carbon dioxide emission rate in tonnes when the flare inlet data is known.
    
    Definition of variables:
    HCin = Flare hydrocarbon inlet rate (to the flare) in SCF
    CFhc = Carbon weight fraction in the inlet hydrocarbon
    FE = Flare combustion efficiency
    Mco2 = Mass of CO2 in flared stream based on CO2 composition of the inlet stream.
    
    CALCULATION STEPS:
    '''
    CO2_mass_emission_rate = convert_scf_to_lbmole(HCin)*(carbon_content_fuel_mixture_mole_basis()*FUEL_EFFICIENCY + mass_CO2_mole_composition_basis(compound, mole_fraction))*convert_lbmole_CO2_to_lbCO2()*convert_lb_to_tonnes()
    return CO2_mass_emission_rate

def CO2_emissions_inlet_known_mass_weight_fraction_basis(HCin, FUEL_EFFICIENCY):
    '''
    This function calculates the Carbon dioxide emission rate in tonnes when the flare inlet data is known.
    
    Definition of variables:
    HCin = Flare hydrocarbon inlet rate (to the flare) in lb
    FUEL_EFFICIENCY = Flare combustion efficiency
    
    CALCULATION STEPS:
    '''
    CO2_mass_emission_rate = HCin*(carbon_content_fuel_mixture_weight_basis()*FUEL_EFFICIENCY*44/12 + mass_CO2_mole_composition_basis(compound, weight_fraction))*convert_lb_to_tonnes()
    return CO2_mass_emission_rate


def CO2_emissions_outlet_known_volume_mole_basis(HCout, FUEL_EFFICIENCY):
    '''
    This function calculates the Carbon dioxide emission rate in tonnes when the flare outlet data is known.
    
    Definition of variables:
    HCout = Flare hydrocarbon outlet rate (to the flare) in SCF
    FUEL_EFFICIENCY = Flare combustion efficiency
    
    CALCULATION STEPS:
    '''
    CO2_mass_emission_rate = convert_scf_to_lbmole(HCout)*(carbon_content_fuel_mixture_mole_basis()*(FUEL_EFFICIENCY/(1-FUEL_EFFICIENCY)) + mass_CO2_mole_composition_basis(compound, mole_fraction))*convert_lbmole_CO2_to_lbCO2()*convert_lb_to_tonnes()
    return CO2_mass_emission_rate

def CO2_emissions_outlet_known_mass_weight_fraction_basis(HCout, FUEL_EFFICIENCY):
    '''
    This function calculates the Carbon dioxide emission rate in tonnes when the flare outlet data is known.
    
    Definition of variables:
    HCout = Flare hydrocarbon outlet rate (to the flare) in lb
    FUEL_EFFICIENCY = Flare combustion efficiency
    
    CALCULATION STEPS:
    '''
    CO2_mass_emission_rate = HCout*(carbon_content_fuel_mixture_weight_basis()*(FUEL_EFFICIENCY/(1-FUEL_EFFICIENCY))*44/12 + mass_CO2_mole_composition_basis(compound, weight_fraction))*convert_lb_to_tonnes()
    return CO2_mass_emission_rate

def CH4_emissions_volume_mole_basis(HCin):
    '''
    This function calculates the Methane emission rate in tonnes when the flare inlet data is known.
    
    CALCULATION STEPS:
    '''
    CH4_mass_emission_rate = convert_scf_to_lbmole(CH4_composition(compound, mole_fraction)*HCin)*(1-FUEL_EFFICIENCY)*16*convert_lb_to_tonnes()
    return CH4_mass_emission_rate

def CH4_emissions_mass_weight_fraction_basis(HCin):
    '''
    This function calculates the Methane emission rate in tonnes when the flare inlet data is known.
    
    CALCULATION STEPS:
    '''
    CH4_mass_emission_rate = CH4_composition(compound, weight_fraction)*HCin*(1-FUEL_EFFICIENCY)*convert_lb_to_tonnes()
    return CH4_mass_emission_rate

def CH4_emissions_volume_outlet_mole_basis(HCout):
    '''
    This function calculates the Methane emission rate in tonnes when the flare inlet data is known.
    
    CALCULATION STEPS:
    '''
    CH4_mass_emission_rate = convert_scf_to_lbmole(CH4_composition(compound, mole_fraction)*HCout)*16*convert_lb_to_tonnes()
    return CH4_mass_emission_rate

def CH4_emissions_mass_outlet_weight_fraction_basis(HCout):
    '''
    This function calculates the Methane emission rate in tonnes when the flare inlet data is known.
    
    CALCULATION STEPS:
    '''
    CH4_mass_emission_rate = CH4_composition(compound, weight_fraction)*HCout*convert_lb_to_tonnes()
    return CH4_mass_emission_rate