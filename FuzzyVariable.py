import numpy as np
import membership_functions
import matplotlib.pyplot as plt

# Visualize these universes and membership functions


def show_graphics():
    fig, (ax0, ax1, ax2, ax3) = plt.subplots(nrows=4, figsize=(8, 9))

    # user temperature
    x = np.linspace(20, 30, 100)

    user_temperature_low = np.vectorize(membership_functions.user_temperature_low)
    user_temperature_optimal = np.vectorize(membership_functions.user_temperature_optimal)
    user_temperature_high = np.vectorize(membership_functions.user_temperature_high)

    ax0.plot(x, user_temperature_low(x), 'b', linewidth=1.5, label='Low')
    ax0.plot(x, user_temperature_optimal(x), 'g', linewidth=1.5, label='Optimal')
    ax0.plot(x, user_temperature_high(x), 'r', linewidth=1.5, label='High')

    ax0.set_title('User Temperature')
    ax0.legend()

    # Temperature difference
    y = np.linspace(-2, 2, 100)

    temperature_difference_negative = np.vectorize(membership_functions.temperature_difference_negative)
    temperature_difference_large = np.vectorize(membership_functions.temperature_difference_large)
    temperature_difference_zero = np.vectorize(membership_functions.temperature_difference_zero)
    temperature_difference_positive = np.vectorize(membership_functions.temperature_difference_positive)

    ax1.plot(y, temperature_difference_negative(y), 'b', linewidth=1.5, label='Negative')
    ax1.plot(y, temperature_difference_large(y), 'g', linewidth=1.5, label='Large')
    ax1.plot(y, temperature_difference_zero(y), 'r', linewidth=1.5, label='Zero')
    ax1.plot(y, temperature_difference_positive(y), 'c', linewidth=1.5, label='Positive')

    ax1.set_title('Temperature Difference')
    ax1.legend()

    # Dew Point
    z = np.linspace(9, 20, 100)

    dew_point_optimal = np.vectorize(membership_functions.dew_point_optimal)
    dew_point_humid = np.vectorize(membership_functions.dew_point_humid)

    ax2.plot(y, dew_point_optimal(z), 'b', linewidth=1.5, label='Optimal')
    ax2.plot(y, dew_point_humid(z), 'r', linewidth=1.5, label='Humid')

    ax2.set_title('Dew Point')
    ax2.legend()

    # Electric Volt
    w = np.linspace(120, 230, 100)

    electric_volt_low = np.vectorize(membership_functions.electric_volt_low)
    electric_volt_high = np.vectorize(membership_functions.electric_volt_high)

    ax3.plot(y, electric_volt_low(w), 'b', linewidth=1.5, label='Low')
    ax3.plot(y, electric_volt_high(w), 'r', linewidth=1.5, label='High')

    ax3.set_title('Electric Volt')
    ax3.legend()

    # Turn off top/right axes
    for ax in (ax0, ax1, ax2, ax3):
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.get_xaxis().tick_bottom()
        ax.get_yaxis().tick_left()

    plt.tight_layout()

    plt.show()
