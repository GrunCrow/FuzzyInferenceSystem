import membership_functions as mf
import FuzzyRule as fr


def take_values(ut, tdiff, td, ev):
    ut_low = mf.user_temperature_low(ut)
    ut_optimal = mf.user_temperature_optimal(ut)    # can be None
    ut_high = mf.user_temperature_high(ut)

    td_negative = mf.temperature_difference_negative(tdiff)
    td_large = mf.temperature_difference_large(tdiff)
    td_zero = mf.temperature_difference_zero(tdiff)     # can be None
    td_positive = mf.temperature_difference_positive(tdiff)     # can be None

    dp_optimal = mf.dew_point_optimal(td)
    dp_humid = mf.dew_point_humid(td)

    ev_low = mf.electric_volt_low(ev)
    ev_high = mf.electric_volt_high(ev)

    ut_value = 'Low', ut_low

    if ut_high > ut_value[1]:
        ut_value = 'High', ut_high
    elif ut_optimal is not None:
        if ut_optimal > ut_value[1]:
            ut_value = 'Optimal', ut_optimal

    td_value = 'Negative', td_negative
    if td_large > td_value[1]:
        td_value = 'Large', td_large
    elif td_zero is not None:
        if td_zero > td_value[1]:
            td_value = 'Zero', td_zero
    elif td_positive is not None:
        if td_positive > td_value[1]:
            td_value = 'Positive', td_positive

    dp_value = 'Optimal', dp_optimal
    if dp_humid > dp_value[1]:
        dp_value = 'Humid', dp_humid

    ev_value = 'Low', ev_low
    if ev_low > ev_value[1]:
        ev_value = 'High', ev_high

    results = fr.evaluation(ut_value[0], td_value[0], dp_value[0], ev_value[0])

    print(results)

