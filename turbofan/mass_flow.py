#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
from openmdao.api import Group, IndepVarComp
from lsdo_utils.api import constants, PowerCombinationComp
from openmdao.api import ExplicitComponent


class Mass_Flow_Rate(ExplicitComponent):

    def setup(self):
        
#        self.add_input('mass_flow_rate_coeffecient')
        self.add_input('thottled_thrust')
        self.add_output('mass_flow_rate')

        self.declare_partials('mass_flow_rate', 'thottled_thrust')
#        self.declare_partials('mass_flow_rate', 'mass_flow_rate_coeffecient')

    def compute (self, inputs, outputs):
#        mass_flow_rate_coeffecient=inputs['mass_flow_rate_coeffecient']
        thrust=inputs['thottled_thrust']
        mass_flow_rate_coeffecient=0.61   
        outputs['mass_flow_rate'] = (thrust * mass_flow_rate_coeffecient)


#    def Mass_Flow_Rate(self, inputs, outputs):
#        comp = PowerCombinationComp(
#            shape=shape,
#            out_name='mass_flow_rate',
#            coeff=module['thrust_specific_fuel_consumption'],
#            powers_dict=dict(
#                thrust=1.,
#            ),
#        )

    def compute_partials(self, inputs, partials):
#        mass_flow_rate_coeffecient=inputs['mass_flow_rate_coeffecient']
        thrust=inputs['thottled_thrust']
        mass_flow_rate_coeffecient=0.61
        partials['mass_flow_rate', 'thottled_thrust'] = mass_flow_rate_coeffecient
#        partials['mass_flow_rate', 'mass_flow_rate_coeffecient'] = thrust
