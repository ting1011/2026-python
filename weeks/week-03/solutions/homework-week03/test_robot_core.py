import unittest

from robot_core import Robot, World, execute_commands, turn_left, turn_right


class TestRobotCore(unittest.TestCase):
    def test_n_plus_l_equals_w(self):
        self.assertEqual(turn_left("N"), "W")

    def test_n_plus_r_equals_e(self):
        self.assertEqual(turn_right("N"), "E")

    def test_four_right_turns_back_to_origin_direction(self):
        d = "N"
        for _ in range(4):
            d = turn_right(d)
        self.assertEqual(d, "N")

    def test_forward_inside_bounds_not_lost(self):
        world = World(5, 3)
        robot = Robot(1, 1, "N")
        execute_commands(world, robot, "F")
        self.assertEqual((robot.x, robot.y, robot.direction, robot.lost), (1, 2, "N", False))

    def test_forward_out_of_bounds_lost(self):
        world = World(5, 3)
        robot = Robot(0, 3, "N")
        execute_commands(world, robot, "F")
        self.assertTrue(robot.lost)
        self.assertEqual((robot.x, robot.y), (0, 3))

    def test_lost_robot_stops_following_commands(self):
        world = World(5, 3)
        robot = Robot(0, 3, "N")
        execute_commands(world, robot, "FRFFLF")
        self.assertEqual((robot.x, robot.y, robot.direction, robot.lost), (0, 3, "N", True))
