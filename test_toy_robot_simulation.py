import unittest
from toy_robot_simulation import Table
from toy_robot_simulation import Robot
from constants import InvalidCommand
from toy_robot_simulation import Command

import unittest

class TestRobotSimulation(unittest.TestCase):

    def setUp(self):
    	self.test_table = Table()
    	self.test_robot = Robot(x_position=3, y_position=3, direction='NORTH')
    
    def test_robot_set_position(self):
    	self.assertEqual(self.test_robot.x_position, 3)
    	
    def test_robot_set_direction(self):
    	self.assertEqual(self.test_robot.direction, "NORTH")
    
    def test_robot_move(self):
    	self.test_robot.move_robot(Table=self.test_table)
    	self.assertEqual(self.test_robot.y_position, 4)
    
    def test_robot_rotate(self):
    	self.test_robot.rotate_robot(command="LEFT")
    	self.assertEqual(self.test_robot.direction, "WEST")
    	self.test_robot.rotate_robot(command="RIGHT")
    	self.assertEqual(self.test_robot.direction, "NORTH")
    
    def test_robot_wrong_direction(self):
    	with self.assertRaises(ValueError):
    		self.test_robot2 = Robot(x_position=3, y_position=3, direction='MOVE')
    
    def test_robot_position_not_number(self):
    	with self.assertRaises(ValueError):
    		self.test_robot2 = Robot(x_position=3, y_position="k", direction="NORTH")


if __name__ == '__main__':
    unittest.main()