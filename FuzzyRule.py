"""	Fuzzy Rules have the form of:
                    if {antecedent clauses} then {consequent clauses}"""


def evaluation(ut, tdiff, td, ev):
    if ut == 'Low' and tdiff == 'Zero' and td == 'Optimal' and ev == 'Regular':
        return 'Low', 'Fast', 'AC', 'Toward'  # 2. grey
    elif ut == 'Optimal' and tdiff == 'Zero' and td == 'Optimal' and ev == 'Regular':
        return 'Low', 'Medium', 'AC', 'Toward'  # 3. dark red
    elif ut != 'Low' and tdiff == 'Positive' and td == 'Optimal' and ev == 'Regular':
        return 'Medium', 'Medium', 'AC', 'Toward'  # 5. blue
    elif ut == 'Low' and (tdiff == 'Negative' or tdiff == 'Zero') and td == 'Humid' and ev == 'Regular':
        return 'Fast', 'Fast', 'DE', 'Toward'  # 6. yellow
    elif ut != 'Low' and tdiff == 'Negative' and td == 'Humid' and ev == 'Regular':
        return 'Low', 'Low', 'DE', 'Away'  # 7. violet
    elif ut == 'Optimal' and tdiff == 'Zero' and td == 'Humid' and ev == 'Regular':
        return 'Medium', 'Fast', 'DE', 'Toward'  # 8. dark green
    elif ut == 'High' and tdiff == 'Zero' and td == 'Humid' and ev == 'Low':
        return 'Medium', 'Medium', 'DE', 'Toward'  # 9. Orange
    elif ut == 'High' and tdiff == 'Positive' and td == 'Humid' and ev == 'Regular':
        return 'Medium', 'Fast', 'AC', 'Toward'  # 10. Red
    elif ev == 'Regular' and \
            (td == 'Humid') or \
            (tdiff == 'Large' and td == 'Optimal') or \
            (ut == 'Low' and tdiff == 'Positive'):
        return 'Fast', 'Fast', 'AC', 'Toward'  # 4. green
    else:
        return 'Low', 'Low', 'AC', 'Away'  # 1. pink
