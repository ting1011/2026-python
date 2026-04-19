import unittest

from robot_core import Robot, World, execute_command, execute_commands


class TestRobotScent(unittest.TestCase):
    def test_first_lost_leaves_scent(self):
        world = World(5, 3)
        robot = Robot(0, 3, "N")
        execute_command(world, robot, "F")
        self.assertIn((0, 3, "N"), world.scents)
        self.assertTrue(robot.lost)

    def test_second_robot_ignores_same_dangerous_forward(self):
        world = World(5, 3)
        r1 = Robot(0, 3, "N")
        execute_command(world, r1, "F")

        r2 = Robot(0, 3, "N")
        execute_command(world, r2, "F")

        self.assertFalse(r2.lost)
        self.assertEqual((r2.x, r2.y, r2.direction), (0, 3, "N"))

    def test_same_cell_different_direction_not_shared(self):
        world = World(5, 3)
        r1 = Robot(0, 3, "N")
        execute_command(world, r1, "F")

        r2 = Robot(0, 3, "E")
        execute_commands(world, r2, "F")

        self.assertFalse(r2.lost)
        self.assertEqual((r2.x, r2.y), (1, 3))

    def test_invalid_command_raises_error(self):
        world = World(5, 3)
        robot = Robot(0, 0, "N")
        with self.assertRaises(ValueError):
            execute_command(world, robot, "X")
