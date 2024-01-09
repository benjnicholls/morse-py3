# Morse Code Translator

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.11%2B-blue.svg)](https://www.python.org/downloads/release)

This Python script translates text to Morse code and vice versa. It also supports replacing periods and dashes with Morse code equivalents.

## Morse Code Dictionary

The Morse code dictionary used in the script is as follows:

```python
morse_code = {
    'A': '·—',
    'B': '—·',
    # ... (other letters, numbers, and characters)
    ' ': ' / ',
    '0': '—————',
    '1': '·————',
    # ... (other numbers)
    '.': '·—·—·—',
    ',': '——··——',
    '?': '··——··',
    '!': '—·—·——',
    '"': '·—··—·'
}
```

## Features

- Translate text to Morse code.
- Translate Morse code to text.
- Handle spaces, numbers, and common punctuation.

## Installation

```bash
pip install morse-py3
```

## Usage

To use the script, run the following command:

```bash
morse-py3 [options]
```

### Options

- `input_string`: The input for the translator.
- `--morse`: Translate input to Morse code.
- `--text`: Translate input from Morse code to text.

### Examples

```bash
# Translate text to Morse code
morse-py3 "Hello World" --morse

# Translate Morse code to text
morse-py3 ".... . .-.. .-.. --- / .-- --- .-. .-.. -.. " --text
```

## Error Handling

The script gracefully handles unrecognized characters and provides informative error messages.

## Dependencies

- `argparse`

## License

This Morse code translator script is licensed under the [MIT License](LICENSE.txt).

Feel free to use and modify this script for your Morse code translation needs! Contributions and feedback are welcome. If you encounter any issues or have suggestions for improvement, please open an issue on the [GitHub repository](https://github.com/benjnicholls/morse-py3).