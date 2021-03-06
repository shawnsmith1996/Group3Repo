import unittest

from turbofan.mach_num() import Thrust_Ratio
from openmdao.api import Problem
from openmdao.utils.assert_utils import assert_check_partials


class TestThrustRatio(unittest.TestCase):

    def test_component_and_derivatives(self):
        prob = Problem()
        prob.model = Mach_Num()
        prob.setup()
        prob.run_model()

        data = prob.check_partials(out_stream=None)
        assert_check_partials(data, atol=1.e-3, rtol=1.e-3)


if __name__ == '__main__':
    unittest.main()
