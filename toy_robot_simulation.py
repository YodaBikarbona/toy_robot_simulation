from constants import COMMAND_LIST
from constants import DIRECTION_LIST
from constants import InvalidCommand
import sys


class Table:

    def __init__(self):
        self.x_size = 5
        self.y_size = 5
        self.min_x = 0
        self.min_y = 0
        self.max_x = 5
        self.max_y = 5

        if self.x_size != 5 and self.y_size != 5:
            raise ValueError("Table must be 5x5 units")

    def __repr__(self):
        return "Table has dimension {0}x{1} units".format(self.x_size, self.y_size)


class RobotPosition:

    def __init__(self, x_position, y_position, direction):
        self.x_position = x_position
        self.y_position = y_position
        self.direction = direction

    def __repr__(self):
        return "Currently robot position is ({0}, {1}) and direction {2}"\
            .format(self.x_position, self.y_position, self.direction)

    def move_robot(self, Table):
        if self.direction == DIRECTION_LIST[0]:
            if self.x_position + 1 > Table.max_x:
                raise ValueError("Robot cannot go to {0} anymore!".format(self.direction))
            self.x_position += 1
        elif self.direction == DIRECTION_LIST[1]:
            if self.y_position + 1 > Table.max_y:
                raise ValueError("Robot cannot go to {0} anymore!".format(self.direction))
            self.y_position += 1
        elif self.direction == DIRECTION_LIST[2]:
            if self.x_position - 1 < Table.min_x:
                raise ValueError("Robot cannot go to {0} anymore!".format(self.direction))
            self.x_position -= 1
        else:
            if self.y_position - 1 < Table.min_y:
                raise ValueError("Robot cannot go to {0} anymore!".format(self.direction))
            self.y_position -= 1

    def rotate_robot(self, command):
        if command == COMMAND_LIST[2]:
            if self.direction == DIRECTION_LIST[0]:
                self.direction = DIRECTION_LIST[3]
            elif self.direction == DIRECTION_LIST[1]:
                self.direction = DIRECTION_LIST[0]
            elif self.direction == DIRECTION_LIST[2]:
                self.direction = DIRECTION_LIST[1]
            else:
                self.direction = DIRECTION_LIST[2]
        else:
            if self.direction == DIRECTION_LIST[0]:
                self.direction = DIRECTION_LIST[1]
            elif self.direction == DIRECTION_LIST[1]:
                self.direction = DIRECTION_LIST[2]
            elif self.direction == DIRECTION_LIST[2]:
                self.direction = DIRECTION_LIST[3]
            else:
                self.direction = DIRECTION_LIST[0]

    def report_of_robot(self):
        return "{0},{1},{2}".format(self.x_position, self.y_position, self.direction)


def command_func(command_list):
    table = Table()
    robot_info = False
    for command in command_list:
        if "{0}".format(command).upper() == COMMAND_LIST[0]:
            robot_info = True
        if robot_info == True and "{0}".format(command) not in COMMAND_LIST:
            command = "{0}".format(command).split(",")
            try:
                len(command) == 3
            except:
                raise InvalidCommand("Robot command PLACE must have three params, x-position, y-position, direction")
            try:
                x_position = int(command[0])
                y_position = int(command[1])
            except:
                raise ValueError("Robot position should be a number!")
            if "{0}".format(command[2]).upper() in DIRECTION_LIST:
                direction = "{0}".format(command[2]).upper()
                robot_info = False
                robot_position = RobotPosition(x_position=x_position, y_position=y_position, direction=direction)
            else:
                raise ValueError("Robot direction does not exist!")
        if "{0}".format(command).upper() == COMMAND_LIST[1]:
            robot_position.move_robot(Table=table)
        if "{0}".format(command).upper() in COMMAND_LIST[2:4]:
            robot_position.rotate_robot(command="{0}".format(command).upper())
        if "{0}".format(command).upper() == COMMAND_LIST[4]:
            print(robot_position.report_of_robot())


if __name__ == "__main__":
    sys.argv.pop(0)
    command_func(command_list=sys.argv)

