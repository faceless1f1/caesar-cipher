# caesar-cipher

## Description

This script implements a simple graphical user interface (GUI) for encrypting text using the Caesar cipher. The application allows users to input a message, specify an encryption key (shift value between 1 and 25), and obtain the encrypted text. The GUI is built using Tkinter.

## Features

- User-friendly interface with a text input box.

- Allows setting an encryption key (shift value) between 1 and 25.

- Displays the encrypted text in real-time.

- Preserves non-alphabetic characters in the input text.

## Requirements

Python 3.x

Tkinter (comes pre-installed with most Python distributions)

## Installation

Ensure you have Python installed on your system.

Clone or download this repository.

## Usage

Run the script using the following command:
```bash
python cipher.py
```

## How to Use

- Enter the message you want to encrypt in the text box.

- Enter an encryption key (a number between 1 and 25).

- Click the "Encrypt" button.

- The encrypted text will be displayed below the button.

## Encryption Logic

-  Caesar cipher shifts each letter in the input text by the specified encryption key:

- Lowercase letters shift within 'a' to 'z'.

- Uppercase letters shift within 'A' to 'Z'.

- Non-alphabetic characters remain unchanged.

## Contributing

Contributions and improvements are welcome! Feel free to fork the repository and submit pull requests. Please make sure to follow the existing coding style and add tests for new features.

## License

This project is licensed under the [MIT License](LICENSE).
 
