G = 6.6700e-11

def no_m(r, g):
    return g * r**2 / G

def no_r(m, g):
    return (G * m / g)**0.5

def no_g(m, r):
    return G * m / r**2

def get_input(prompt, error_message):
    while True:
        try:
            return float(input(prompt).strip())
        except ValueError:
            print(error_message)

def main():
    print("Welcome to the Gravity Acceleration Calculator")
    valid_options = ['m', 'g', 'r']
    missing = None

    while missing not in valid_options:
        missing_input = input("Which variable are you solving for (m, g, r)? ").strip().lower()
        if missing_input in valid_options:
            missing = missing_input
        else:
            print("Invalid option. Please enter one of the following: m, g, r.")

        m = r = g = None

    if missing != 'm':
        m = get_input("Enter the value of the mass (m) in kilograms: ", "Invalid format. Please enter a number.")
    if missing != 'r':
        r = get_input("Enter the value of the distance from the mass (r) in meters: ", "Invalid format. Please enter a number.")
    if missing != 'g':
        g = get_input("Enter the value of the gravitational acceleration (g) in m/s^2: ", "Invalid format. Please enter a number.")

    print("Calculating...")
    if missing == 'm':
        result = no_m(r, g)
    elif missing == 'r':
        result = no_r(m, g)
    elif missing == 'g':
        result = no_g(m, r)


    print(f"Calculated value of {missing}: {result:.3e} ({result})")
    
if __name__ == "__main__":
    main()