#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import unittest

from turbofan.mass_flow import Mass_Flow_Rate
from openmdao.api import Problem
from openmdao.utils.assert_utils import assert_check_partials


class TestMassFlowRate(unittest.TestCase):

    def test_component_and_derivatives(self):
        prob = Problem()
        prob.model = Mass_Flow_Rate(e=0.5)
        prob.setup()
        prob.run_model()

        data = prob.check_partials(out_stream=None)
        assert_check_partials(data, atol=1.e-3, rtol=1.e-3)


if __name__ == '__main__':
    unittest.main()

