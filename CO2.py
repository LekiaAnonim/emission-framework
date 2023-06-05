from emission import Emission
import convert
class CO2(Emission):
        
    def inletvolume_molefraction(self):
        '''
        This function calculates the Carbon dioxide emission rate in tonnes when the flare inlet data is known.
        CALCULATION STEPS:
        '''
        CO2_mass_emission_rate = convert.lb_tonnes(convert.CO2_lbmole_lb(convert.scf_lbmole(self.HC)*(self.carbon_content_fuel_mixture_mole_basis()*self.FUEL_EFFICIENCY + self.CO2_composition())))
        return CO2_mass_emission_rate
    
    def inletmass_weightfraction(self):
        '''
        This function calculates the Carbon dioxide emission rate in tonnes when the flare inlet data is known.
        CALCULATION STEPS:
        '''
        CO2_mass_emission_rate = convert.lb_tonnes(self.HC*(self.carbon_content_fuel_mixture_weight_basis()*self.FUEL_EFFICIENCY*44/12 + self.CO2_composition()))
        return CO2_mass_emission_rate
    
    def outletvolume_molefraction(self):
        '''
        This function calculates the Carbon dioxide emission rate in tonnes when the flare outlet data is known.
        CALCULATION STEPS:
        '''
        CO2_mass_emission_rate = convert.lb_tonnes(convert.CO2_lbmole_lb(convert.scf_lbmole(self.HC)*(self.carbon_content_fuel_mixture_mole_basis()*(self.FUEL_EFFICIENCY/(1-self.FUEL_EFFICIENCY)) + CO2_composition())))
        return CO2_mass_emission_rate
    
    def outletmass_weightfraction(self):
        '''
        This function calculates the Carbon dioxide emission rate in tonnes when the flare outlet data is known.
        CALCULATION STEPS:
        '''
        CO2_mass_emission_rate = convert.lb_tonnes(self.HC*(self.carbon_content_fuel_mixture_weight_basis()*(self.FUEL_EFFICIENCY/(1-self.FUEL_EFFICIENCY))*44/12 + self.CO2_composition()))
        return CO2_mass_emission_rate