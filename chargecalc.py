e = 1.6e-19

def no_q(n, e):
    return n * e

def no_n(q, e):
    return q / e

def get_input(prompt, error_message):
    while True:
        try:
            input_value = float(input(prompt).strip())
            if prompt.lower().startswith("enter the whole number"):
                if input_value.is_integer():
                    return input_value
                else:
                    raise ValueError
            return input_value
        except ValueError:
            print(error_message)

def main():
    print("Welcome to the Charge Calculator")

    valid_options = ['q', 'n']
    missing = None

    while missing not in valid_options:
        missing_input = input("Which variable are you solving for (q or n)? ").strip().lower()
        if missing_input in valid_options:
            missing = missing_input
        else:
            print("Invalid option. Please enter one of the following: q, n.")

    q = n = None

    if missing != 'q':
        q = get_input("Enter the Total charge of the equation: ", "Invalid format. Please enter a number.")
    if missing != 'n':
        n = get_input("Enter the whole number: ", "Invalid format. Please enter a whole number.")

    print("Calculating...")
    if missing == 'q':
        result = no_q(n, e)
    elif missing == 'n':
        result = no_n(q, e)

    print(f"Calculated value of {missing}: {result:.3e} ({result})")


if __name__ == "__main__":
    main()
