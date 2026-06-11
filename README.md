# password-generator

A simple command-line password generator written in Python.

## Features

- Customizable password length
- Generate multiple passwords at once
- Options to include/exclude uppercase, digits, symbols
- No external dependencies

## Usage

```bash
# Default (16 chars, all character types)
python passgen.py

# Custom length
python passgen.py --length=24

# Generate multiple passwords
python passgen.py --count=5

# No symbols
python passgen.py --length=20 --no-symbols

# Combined options
python passgen.py --length=32 --count=3 --no-symbols
```

## Example Output

```
Generated 3 password(s) [length=16]:
----------------------------------------
  aB3!xQw@9kLm#2Rp
  Tz7$nYe!4vKj@8Wc
  Pm2#uHq!6dNs@5Xb
----------------------------------------
```

## Requirements

- Python 3.x
