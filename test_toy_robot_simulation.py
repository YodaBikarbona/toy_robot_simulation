from toy_robot_simulation import Table
from toy_robot_simulation import Robot
from constants import InvalidCommand
from toy_robot_simulation import Command
import unittest


class TestRobotSimulation(unittest.TestCase):

    def setUp(self):
        self.test_table = Table()
        self.test_robot = Robot(x_position=0, y_position=0, direction='NORTH')

    def test_robot_set_position(self):
        self.assertEqual(self.test_robot.x_position, 0)

    def test_robot_set_direction(self):
        self.assertEqual(self.test_robot.direction, "NORTH")

    def test_robot_move(self):
        self.test_robot.move_robot(Table=self.test_table)
        self.assertEqual(self.test_robot.y_position, 1)

    def test_robot_rotate(self):
        self.test_robot.rotate_robot(command="LEFT")
        self.assertEqual(self.test_robot.direction, "WEST")
        self.test_robot.rotate_robot(command="RIGHT")
        self.assertEqual(self.test_robot.direction, "NORTH")

    def test_robot_error_direction(self):
        with self.assertRaises(ValueError):
            self.test_robot2 = Robot(x_position=3, y_position=3, direction='MOVE')

    def test_robot_error_position(self):
        with self.assertRaises(ValueError):
            self.test_robot2 = Robot(x_position=3, y_position="k", direction="NORTH")

    def test_robot_move_error(self):
        with self.assertRaises(ValueError):
            self.test_robot3 = Robot(x_position=3, y_position=5, direction='NORTH')
            self.test_robot3.move_robot(Table=self.test_table)

    def test_robot_command_place_error(self):
        with self.assertRaises(InvalidCommand):
            self.command_list = Command(command_list=["PLACE", "0,0", "MOVE", "REPORT"])
            self.command_list.command_func()

    def test_robot_report(self):
        self.test_robot.move_robot(Table=self.test_table)
        self.assertEqual(self.test_robot.report_of_robot(), "0,1,NORTH")


if __name__ == '__main__':
    unittest.main()
