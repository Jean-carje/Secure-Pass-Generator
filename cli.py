import argparse
from secure_pass_gen import generate_password

# Create base Parser
parser = argparse.ArgumentParser()

# Command Optional Arguments
parser.add_argument('-l', '--length', type=int,default=12, help="Lenght of the password (Default: 12, Min: 4)")
parser.add_argument('-r', '--remove-ambiguous', action="store_true", default=False, help="Remove ambiguous characters like 'l', '1', 'O', '0' (Default: False)")

# Store argument values
args = parser.parse_args()

# Generate the password with the specified options
password, entropy, entropy_level = generate_password(args.length, args.remove_ambiguous)

# Display the generated password and its entropy
print(f"\nYour new secure password is: {password}")
print(f"Estimated entropy: {entropy:.2f} bits ({entropy_level})")
