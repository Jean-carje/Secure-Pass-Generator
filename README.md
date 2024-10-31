# SecurePassGen

**SecurePassGen** is a robust and secure password generator written in Python. It utilizes cryptographically secure methods to create strong, random passwords, ensuring maximum security for your accounts and data.

## Features

- **Cryptographically Secure**: Uses Python's `secrets` module to generate passwords that are secure and unpredictable.
- **Includes All Character Types**: Guarantees the inclusion of lowercase letters, uppercase letters, digits, and symbols.
- **Optional Exclusion of Ambiguous Characters**: Allows users to exclude characters that can be easily confused, such as `'l'`, `'1'`, `'O'`, and `'0'`.
- **Entropy Calculation**: Calculates and displays the entropy of the generated password, providing insight into its strength.
- **Customizable Length**: Users can specify the desired length of the password.
- **User-Friendly Interface**: Easy-to-use command-line interface.

## Installation

```bash
# Clone the repository
git clone https://github.com/Jean-carje/SecurePassGen.git

# Navigate to the project directory
cd SecurePassGen
```

## Usage

```bash
python secure_pass_gen.py
```

Follow the on-screen instructions to generate a secure password.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for improvements, bug fixes, or new features.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.