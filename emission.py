
from collections.abc import Iterable
import pandas as pd
import re
from chemicals import *

class Emission:
    '''This Emission class serves as the base class for emission quantification for CO2, CH4, and N2O. It defines all input parameters,
    and calculates all relavant methods required for calculation of emission.

    ...
    Attributes
    ------------
    compounds: str
        An array or list of flare gas components chemical formulas, or common_name

    composition: float
        An corresponding array or list of the mole fraction or weight fraction of flare gas components.

    HC : float
        The mass or volume flowrate of the gas to the flare.

    FUEL_EFFICIENCY: float
        Usually given a default value of 0.98
    '''
    def __init__(self, compounds:Iterable[str], composition:Iterable[float], HC, FUEL_EFFICENCY, *args, **kwargs):
        self.compounds = compounds
        self.composition = composition
        self.HC = HC
        self.FUEL_EFFICIENCY = FUEL_EFFICENCY
        self.args = args
        self.kwargs = kwargs
        
    def get_molecular_weight_list(self):
        '''This function returns the list of molecular weight for the components in a gas mixture.
            The function Receives an array or list of the common name or molecular formular of the gas components as argument.
        '''
        # list of gas components.

        list_of_components = []
        list_of_molecular_weight = []
        list_of_molecular_formula = []
        for i in identifiers.pubchem_db:
            for j in self.compounds:
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
        
    def molecularweight_mixture_molefraction(self, molecular_weight:Iterable[float]):
        '''This function calculates molecular weight fraction of the gas mixture given:
        mole fraction, and molecular weight

        '''
        x = zip(self.composition, molecular_weight)
        product_list = []
        for a, b in x:
            product_list.append(a*b)

        return sum(product_list)
    
    def molecularweight_mixture_weightfraction(self, molecular_weight:Iterable[float]):
        '''This function calculates molecular weight fraction of the gas mixture given:
        component weight fractions, and molecular weights.

        '''
        x = zip(self.composition, molecular_weight)
        product_list = []
        for a, b in x:
            product_list.append(a/b)

        return sum(product_list)
    
    def find_hydrocarbons_in_gas_mixture(self):
        '''
        This function returns only the hydrocarbon components present in a mixture of gases.
        '''
        # create a regular expression in python for strings that contains on C and H, and digits between the C and H
        pattern = r'^[CH\d]+$'
        list_of_hydrocarbons = []
        for i in identifiers.pubchem_db:
            if re.search(pattern, i.formula):
                for j in self.compounds:
                    if i.formula == j or i.common_name == j:
                        list_of_hydrocarbons.append(i)
            else:
                None
        return list_of_hydrocarbons
    
    def adjusted_composition(self):
        '''This function takes the mole fraction or weight fraction of the gas mixture as argument and returns a list of the adjusted mole fraction of weight fraction.'''

        # combine two lists, compound and composition into a dictionary of key and value pair.
        dictionary = dict(zip(self.compounds, self.composition))
        included_list = self.find_hydrocarbons_in_gas_mixture()
        for key, value in dictionary.items():
            if key in [i.formula for i in included_list]:
                dictionary[key] = value  # Set value to value if key is in include_list
            elif key in [i.common_name for i in included_list]:
                dictionary[key] = value  # Set value to value if key is in include_list
            else:
                dictionary[key] = 0 # Set value to value if key is not in include_list

        # print(dictionary)

        # find the sum of the new dictionary values when non-hydrocarbon components are set to zero
        sum_composition = sum(dictionary.values())
        for key, values in dictionary.items():
            dictionary[key] = values/sum_composition
        return dictionary
    
    def carbon_ratio(self, compound):
        matches = re.findall(r"C(\d+)H", compound)
        if compound == 'CH4':
            digits = 1
        elif matches == []:
            digits = None
        else:
            digits = matches[0]
        return digits
    
    def adjustedComposition_molecularweight_table(self):
        
        # List to define the sorting order
        sorting_order = list(self.adjusted_composition())

        # Sort the DataFrame based on the sorting_order list
        df_sorted = self.get_molecular_weight_list().sort_values(by='Formula', key=lambda x: x.map({value: i for i, value in enumerate(sorting_order)})).reset_index(drop=True)

        # Append adjusted composition to sorted dataFrame
        df_sorted['Adjusted Composition'] = pd.Series(self.adjusted_composition().values())


        # Append Carbon Ratio to the dataframe
        df_sorted['Carbon Ratio'] = df_sorted['Formula'].apply(lambda formula: self.carbon_ratio(formula))
        return df_sorted.fillna(0)
    
    def carbon_content_mole_basis(self):
        data_table = self.adjustedComposition_molecularweight_table()
        data_table['Mole Fraction'] = pd.Series(self.composition)
        data_table = data_table.fillna(0)
        mole_fraction_carbonratio = lambda row: row['Mole Fraction']*float(row['Carbon Ratio'])

        data_table['Carbon Content'] = data_table.apply(mole_fraction_carbonratio, axis=1)

        return data_table
    
    def carbon_content_weight_basis(self):
        data_table = self.adjustedComposition_molecularweight_table()
        data_table['Weight Fraction'] = pd.Series(self.composition)
        data_table = data_table.fillna(0)
        mole_fraction_carbonratio = lambda row: row['Adjusted Composition']*float(row['Carbon Ratio'])*12/row['Molecular Weight']

        data_table['Carbon Content'] = data_table.apply(mole_fraction_carbonratio, axis=1)

        return data_table
    
    def carbon_content_fuel_mixture_mole_basis(self):
        C_mixture = sum(self.carbon_content_mole_basis()['Carbon Content'])
        return C_mixture

    def carbon_content_fuel_mixture_weight_basis(self):
        C_mixture = sum(self.carbon_content_weight_basis()['Carbon Content'])
        return C_mixture
        
    def CO2_composition(self):
        '''Mass of CO2 in the flared stream based on CO2 composition of the inlet stream'''
        dictionary = dict(zip(self.compounds, self.composition))
        if 'CO2' in self.compounds:
             co2_composition = dictionary['CO2']
        elif dictionary['carbon dioxide']:
            co2_composition = dictionary['carbon dioxide']
        return co2_composition

    def CH4_composition(self):
        '''CH4 composition'''
        dictionary = dict(zip(self.compounds, self.composition))
        if 'CH4' in self.compounds:
            CH4_composition = dictionary['CH4']
        elif dictionary['methane']:
            CH4_composition = dictionary['methane']
        return CH4_composition
