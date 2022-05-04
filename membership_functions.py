#   inputs
def user_temperature_low(x):
    if x <= 22:
        return 1
    elif 22 <= x <= 25:
        return (25-x) / 3
    else:
        return 0


def user_temperature_optimal(x):
    if 22 <= x <= 25:
        return (x - 22) / 3
    elif 25 <= x <= 28:
        return (28 - x) / 3


def user_temperature_high(x):
    if 25 <= x <= 28:
        return (x - 25) / 3
    elif 28 <= x <= 30:
        return 1
    else:
        return 0


def temperature_difference_negative(x):
    if -1 <= x <= -0.9:
        return 1
    elif -0.9 <= x <= 0:
        return -0.9*x
    else:
        return 0


def temperature_difference_zero(x):
    if -0.5 <= x <= 0:
        return 2 * (x + 0.5)
    elif 0 <= x <= 0.5:
        return 2 * (0.5 - x)


def temperature_difference_positive(x):
    if 0 <= x <= 1:
        return x
    elif 1 <= x <= 2:
        return 2 - x


def temperature_difference_large(x):
    if 1 <= x <= 2:
        return 1 - x
    elif 2 <= x <= 3:
        return 1
    else:
        return 0


def dew_point_optimal(x):
    if 10 <= x <= 11:
        return 1
    elif 11 <= x <= 14:
        return (14 - x) / 3
    else:
        return 0


def dew_point_humid(x):
    if 12 <= x <= 15:
        return (x - 12) / 5
    elif 15 <= x <= 18:
        return 1
    else:
        return 0


def electric_volt_low(x):
    if 130 <= x <= 160:
        return 1
    elif 160 <= x <= 180:
        return (180 - x) / 20
    else:
        return 0


def electric_volt_high(x):
    if 170 <= x <= 190:
        return (x - 170) / 2
    elif 160 <= x <= 180:
        return 1
    else:
        return 0


# outputs


def compressor_speed_low(x):
    if 0 <= x <= 30:
        return 1
    elif 30 <= x <= 50:
        return (50 - x) / 2
    else:
        return 0


def compressor_speed_medium(x):
    if 40 <= x <= 60:
        return (x - 40) / 20
    elif 60 <= x <= 80:
        return (80 - x) / 20
    else:
        return 0


def compressor_speed_fast(x):
    if 70 <= x <= 90:
        return (x - 70) / 20
    elif 90 <= x <= 100:
        return 1
    else:
        return 0


def fan_speed_low(x):
    if 0 <= x <= 30:
        return 1
    elif 30 <= x <= 50:
        return (50 - x) / 20
    else:
        return 0


def fan_speed_medium(x):
    if 40 <= x <= 60:
        return (x - 40) / 20
    elif 60 <= x <= 80:
        return (80 - x) / 20
    else:
        return 0


def fan_speed_fast(x):
    if 70 <= x <= 90:
        return (x - 70) / 20
    elif 90 <= x <= 100:
        return 1
    else:
        return 0


def mode_of_operation_ac(x):
    return x


def mode_of_operation_dc(x):
    return 1 - x


def fin_direction_away(x):
    if x < 25:
        return 0
    elif 25 <= x <= 75:
        return (x - 25) / 50
    elif 75 < x:
        return 1


def fin_direction_towards(x):
    if x < 25:
        return 1
    elif 25 <= x <= 75:
        return (75 - x) / 50
    elif 75 < x:
        return 0
