def sum(value1, value2):
    return value1 + value2


# https://docs.python.org/3/library/typing.html
Measurements = list[str]


def number_of_times_a_depth_measurement_increases(measurements: Measurements):
    if len(measurements) == 0:
        return 0

    # list comprehension
    measurements = [int(measurement) for measurement in measurements]
    # ms = []
    # for measurement in measurements:
    #     ms.append(int(measurement))
    # measurements = ms

    current_value = measurements[0]
    nb_of_increases = 0
    for measurement in measurements:
        if measurement > current_value:
            nb_of_increases += 1
        current_value = measurement
    return nb_of_increases


if __name__ == "__main__":
    measurements = open("in.txt").readlines()
    increases = number_of_times_a_depth_measurement_increases(measurements)
    print(f"Number of increases {increases}")
