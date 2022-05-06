import FuzzyVariable as fv
import FuzzySystem as fs

# Visualize these universes and membership functions
fv.show_graphics()

while True:
    # Ask for the values for the function:
    ut = input("Enter User temperature Value: ")
    tdiff = input("Enter Temperature Difference Value: ")
    td = input("Enter Dew Point Value: ")
    ev = input("Enter Electric Volt Value: ")

    output = fs.take_values(float(ut), float(tdiff), float(td), float(ev))

    print(output)

