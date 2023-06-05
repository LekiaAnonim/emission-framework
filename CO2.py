from emission import Emission
import convert
class CH4(Emission):
    
    def inletvolume_molefraction(self):
        '''
        This function calculates the Methane emission rate in tonnes when the flare inlet data is known.
        CALCULATION STEPS:
        '''
        CH4_mass_emission_rate = convert.lb_tonnes(convert.scf_lbmole(self.CH4_composition(self.compounds, self.composition)*self.HC)*(1-self.FUEL_EFFICIENCY)*16)
        return CH4_mass_emission_rate
    
    def inletmass_weightfraction(self):
        '''
        This function calculates the Methane emission rate in tonnes when the flare inlet data is known.
        CALCULATION STEPS:
        '''
        CH4_mass_emission_rate = convert.lb_tonnes(self.CH4_composition(self.compounds, self.composition)*self.HC*(1-self.FUEL_EFFICIENCY))
        return CH4_mass_emission_rate
    
    def outletvolume_molefraction(self):
        '''
        This function calculates the Methane emission rate in tonnes when the flare inlet data is known.
        CALCULATION STEPS:
        '''
        CH4_mass_emission_rate = convert.lb_tonnes(convert.scf_lbmole(self.CH4_composition(self.compounds, self.composition)*self.HC)*16)
        return CH4_mass_emission_rate
    
    def outletmass_weightfraction(self):
        '''
        This function calculates the Methane emission rate in tonnes when the flare inlet data is known.
        CALCULATION STEPS:
        '''
        CH4_mass_emission_rate = convert.lb_tonnes(self.CH4_composition(self.compounds, self.composition)*self.HC)
        return CH4_mass_emission_rate