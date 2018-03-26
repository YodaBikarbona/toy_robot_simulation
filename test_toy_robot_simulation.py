import unittest
from toy_robot_simulation import Table
from toy_robot_simulation import RobotPosition

import unittest

class TestRobotSimulation(unittest.TestCase):

    def setUp(self):
    	self.test_table = Table()
    	self.test_robot = RobotPosition(x_position=3, y_position=3, direction='NORTH')
    
    def test_robot_set_position(self):
    	import pdb;pdb.set_trace()
    	self.assertEqual(self.test_robot.x_position, 3)


if __name__ == '__main__':
    unittest.main()