# https://docs.python.org/3/library/unittest.html

import unittest
import main


class TestsMain(unittest.TestCase):
    def test_count_number_of_increases_with_empty_mesurements(self):
        # AAA
        # Arrange
        measurements = []
        # Act
        increases = main.number_of_times_a_depth_measurement_increases(measurements)
        # Assert
        self.assertEquals(increases, 0)

    def test_count_number_of_increases_with_one_measurement(self):
        # AAA
        # Arrange
        measurements = [
            199,
        ]
        # Act
        increases = main.number_of_times_a_depth_measurement_increases(measurements)
        # Assert
        self.assertEquals(increases, 0)

    def test_count_number_of_increases(self):
        # AAA
        # Arrange
        measurements = [
            199,
            200,
            208,
            210,
            200,
            207,
            240,
            269,
            260,
            263,
        ]
        # Act
        increases = main.number_of_times_a_depth_measurement_increases(measurements)
        # Assert
        self.assertEquals(increases, 7)

    def test_number_of_times_a_depth_measurement_increases_convert_measurements_to_numbers(
        self,
    ):
        # AAA
        # Arrange
        measurements = [
            100,
            20,
        ]
        # Act
        increases = main.number_of_times_a_depth_measurement_increases(measurements)
        # Assert
        self.assertEquals(increases, 0)

    def test_the_number_of_times_the_sum_of_measurements_in_this_sliding_window_increases(
        self,
    ):
        # AAA
        # Arrange
        sliding_window_measurements = [
            199,
            200,
            208,
            210,
            200,
            207,
            240,
            269,
            260,
            263,
        ]
        measurements = main.transform_sliding_measurements_into_measurements(
            sliding_window_measurements
        )
        # Act
        increases = main.number_of_times_a_depth_measurement_increases(measurements)
        # Assert
        self.assertEquals(increases, 5)

    def test_transform_sliding_measurements_into_measurements(
        self,
    ):
        # AAA
        # Arrange
        sliding_window_measurements = [
            199,
            200,
            208,
            210,
            200,
            207,
            240,
            269,
            260,
            263,
        ]
        expected_measurements = [
            607,
            618,
            618,
            617,
            647,
            716,
            769,
            792,
        ]
        # Act
        measurements = main.transform_sliding_measurements_into_measurements(
            sliding_window_measurements
        )
        # Assert
        self.assertListEqual(expected_measurements, measurements)


if __name__ == "__main__":
    unittest.main()
