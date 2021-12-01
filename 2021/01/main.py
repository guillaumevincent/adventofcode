# https://docs.python.org/3/library/typing.html


def number_of_times_a_depth_measurement_increases(measurements: list[int]):
    if len(measurements) == 0:
        return 0
    current_value = measurements[0]
    nb_of_increases = 0
    for measurement in measurements:
        if measurement > current_value:
            nb_of_increases += 1
        current_value = measurement
    return nb_of_increases


def transform_sliding_measurements_into_measurements(
    sliding_window_measurements: list[int],
):
    measurements = []
    for index in range(len(sliding_window_measurements) - 2):
        measurements.append(sum(sliding_window_measurements[index : index + 3]))
    return measurements


if __name__ == "__main__":
    measurements = open("puzzle1.in").readlines()
    measurements = [int(measurement) for measurement in measurements]
    increases = number_of_times_a_depth_measurement_increases(measurements)
    print(f"a Number of increases {increases}")
    measurements = transform_sliding_measurements_into_measurements(measurements)
    increases = number_of_times_a_depth_measurement_increases(measurements)
    print(f"b Number of increases {increases}")
