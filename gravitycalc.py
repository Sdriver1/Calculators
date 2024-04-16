G = 6.6700E-11

def no_m1(m2, r, F):
    return F * r**2 / (G * m2)

def no_m2(m1, r, F):
    return F * r**2 / (G * m1)

def no_r(m1, m2, F):
    return (G * m1 * m2 / F)**0.5

def no_F(m1, m2, r):
    return G * m1 * m2 / r**2

def get_input(prompt, error_message):
    while True:
        try:
            return float(input(prompt).strip())
        except ValueError:
            print(error_message)

def main():
    print("Welcome to the Gravity Calculator")

    valid_options = ['m1', 'm2', 'f', 'r']
    missing = None

    while missing not in valid_options:
        missing_input = input("Which variable are you solving for (m1, m2, r, F)? ").strip().lower()
        if missing_input in valid_options:
            missing = missing_input
        else:
            print("Invalid option. Please enter one of the following: m1, m2, r, F.")

    m1 = m2 = r = F = None

    if missing != 'm1':
        m1 = get_input("Enter the value of the first mass (m1) in kilograms: ", "Invalid format. Please enter a number.")
    if missing != 'm2':
        m2 = get_input("Enter the value of the second mass (m2) in kilograms: ", "Invalid format. Please enter a number.")
    if missing != 'r':
        r = get_input("Enter the value of the distance between the two masses (r) in meters: ", "Invalid format. Please enter a number.")
    if missing != 'f':
        F = get_input("Enter the value of the gravitational force between the two masses (F) in newtons: ", "Invalid format. Please enter a number.")

    print("Calculating...")
    if missing == 'm1':
        result = no_m1(m2, r, F)
    elif missing == 'm2':
        result = no_m2(m1, r, F)
    elif missing == 'r':
        result = no_r(m1, m2, F)
    elif missing == 'f':
        result = no_F(m1, m2, r)

    print(f"Calculated value of {missing}: {result:.3e} ({result})")

if __name__ == "__main__":
    main()