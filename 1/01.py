def fuel_needed_for_mass(mass):
    return int(mass / 3) - 2


def calc_mass(mass):
    total_fuel = 0
    current_fuel = fuel_needed_for_mass(mass)
    while current_fuel > 0:
        total_fuel += current_fuel
        current_fuel = fuel_needed_for_mass(current_fuel)
    return total_fuel


if __name__ == "__main__":
    assert calc_mass(12) == 2
    assert calc_mass(14) == 2
    assert calc_mass(1969) == 966
    assert calc_mass(100756) == 50346

    print(sum([calc_mass(int(x)) for x in open("01.in").readlines()]))
