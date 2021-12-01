# https://docs.python.org/3/library/unittest.html

import unittest
from main import sum
from main import number_of_times_a_depth_measurement_increases


class TestsMain(unittest.TestCase):
    def test_sum(self):
        assert sum(1, 1) == 2

    def test_count_number_of_increases_with_empty_mesurements(self):
        # AAA
        # Arrange
        measurements = []
        # Act
        increases = number_of_times_a_depth_measurement_increases(measurements)
        # Assert
        self.assertEquals(increases, 0)

    def test_count_number_of_increases_with_one_measurement(self):
        # AAA
        # Arrange
        measurements = [
            "199",
        ]
        # Act
        increases = number_of_times_a_depth_measurement_increases(measurements)
        # Assert
        self.assertEquals(increases, 0)

    def test_count_number_of_increases(self):
        # AAA
        # Arrange
        measurements = [
            "199",
            "200",
            "208",
            "210",
            "200",
            "207",
            "240",
            "269",
            "260",
            "263",
        ]
        # Act
        increases = number_of_times_a_depth_measurement_increases(measurements)
        # Assert
        self.assertEquals(increases, 7)

    def test_number_of_times_a_depth_measurement_increases_convert_measurements_to_numbers(
        self,
    ):
        # AAA
        # Arrange
        measurements = [
            "100",
            "20",
        ]
        # Act
        increases = number_of_times_a_depth_measurement_increases(measurements)
        # Assert
        self.assertEquals(increases, 0)


if __name__ == "__main__":
    unittest.main()
