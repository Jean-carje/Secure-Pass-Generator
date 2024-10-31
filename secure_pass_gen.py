import secrets
import string
import math

def calculate_entropy(length, num_ch):
    """
    Calculates the ENTROPY of the password.

    Entropy is a measure of the unpredictability or randomness of the password.
    Higher entropy indicates a stronger, more secure password.

    Parameters:
        length (int): The length of the password.
        num_ch (int): The total number of characters used to generate the password.

    Returns:
        float: The calculated entropy in bits.
    """
    # Entropy formula: log2(number_of_characters ^ length)
    return math.log2(num_ch ** length)

def classify_entropy(entropy):
    """
    Classifies the entropy into low, medium, or high.
    
    Parameters:
        entropy (float): The entropy value in bits.

    Returns:
        str: The classification of the entropy.
    """
    if entropy < 50:
        return "Low"
    elif 50 <= entropy < 80:
        return "Medium"
    else:
        return "High"

def generate_password(length=12, excl_ambiguous=False):
    """
    Generates a secure password of the specified length.

    Parameters:
        length (int): Desired length of the password. (12 for defect)
        excl_ambiguous (bool): If True, excludes ambiguous characters.

    Returns:
        tuple: A tuple containing the generated password and its entropy.
    """
    # Define the different types of characters
    lowercase_letters = set(string.ascii_lowercase)
    uppercase_letters = set(string.ascii_uppercase)
    digits = set(string.digits)
    symbols = set(string.punctuation)

    # Optionally exclude ambiguous characters
    if excl_ambiguous:
        ambiguous_characters = {'l', 'I', '1', '0', 'O', 'o'}
        lowercase_letters -= ambiguous_characters
        uppercase_letters -= ambiguous_characters
        digits -= ambiguous_characters
        symbols -= ambiguous_characters

    # Create a list of character categories that are not empty..
    categories = [lowercase_letters, uppercase_letters, digits, symbols]
    categories = [list(category) for category in categories if category]

    # Ensure there are enough character to generate a password
    if len(categories) == 0:
        raise ValueError("Not enough character types available to generate the password.")

    # Ensure the password length is at least equal to the number of categories
    if length < len(categories):
        raise ValueError(f"The minimum length is {len(categories)} to include all selected character types.")

    # Ensure the password contains at least one character from each category
    password = [secrets.choice(category) for category in categories]

    # Combine all available characters into a single list
    all_characters = [char for category in categories for char in category]

    # Fill the remaining length of the password with random choices from all characters
    for _ in range(length - len(password)):
        password.append(secrets.choice(all_characters))

    # Securely shuffle the password to avoid any predictable patterns
    secrets.SystemRandom().shuffle(password)

    # Join the characters to form the final password string
    password = ''.join(password)

    # Calculate entropy and classify it
    entropy = calculate_entropy(length, len(all_characters))
    entropy_level = classify_entropy(entropy)

    return password, entropy, entropy_level

def main():
    print("Secure Password Generator")
    try:
        # Prompt the user to enter the desired password length
        length_input = input("Enter the password length (default 12): ") or "12"
        length = int(length_input)

        # Ask if the user wants to exclude ambiguous characters
        excl_ambiguous_input = input(
            "Do you want to exclude ambiguous characters like 'l', '1', 'O', '0'? (y/n, default 'n'): "
        ) or "n"
        excl_ambiguous = excl_ambiguous_input.strip().lower() == 'y'

        # Generate the password with the specified options
        password, entropy, entropy_level = generate_password(length, excl_ambiguous)

        # Display the generated password and its entropy
        print(f"\nYour new secure password is: {password}")
        print(f"Estimated entropy: {entropy:.2f} bits ({entropy_level})")
    except ValueError as e:
        # Handle any ValueError exceptions (e.g., invalid input)
        print(f"Error: {e}. Please try again.")

if __name__ == "__main__":
    main()
