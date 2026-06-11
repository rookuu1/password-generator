import random
import string
import sys

def generate(length=16, use_upper=True, use_digits=True, use_symbols=True, count=1):
    chars = string.ascii_lowercase

    if use_upper:
        chars += string.ascii_uppercase
    if use_digits:
        chars += string.digits
    if use_symbols:
        chars += "!@#$%^&*()-_=+[]{}|;:,.<>?"

    if not chars:
        print("Error: at least one character type must be enabled.")
        return

    passwords = []
    for _ in range(count):
        pwd = ''.join(random.choices(chars, k=length))
        passwords.append(pwd)

    print(f"\nGenerated {count} password(s) [length={length}]:")
    print("-" * 40)
    for pwd in passwords:
        print(f"  {pwd}")
    print("-" * 40)

def parse_args(args):
    length = 16
    count = 1
    use_upper = True
    use_digits = True
    use_symbols = True

    for arg in args:
        if arg.startswith("--length="):
            length = int(arg.split("=")[1])
        elif arg.startswith("--count="):
            count = int(arg.split("=")[1])
        elif arg == "--no-upper":
            use_upper = False
        elif arg == "--no-digits":
            use_digits = False
        elif arg == "--no-symbols":
            use_symbols = False

    return length, count, use_upper, use_digits, use_symbols

if __name__ == "__main__":
    args = sys.argv[1:]
    length, count, use_upper, use_digits, use_symbols = parse_args(args)
    generate(length, use_upper, use_digits, use_symbols, count)
