import sys


def main():
    args = sys.argv[1:]
    if args:
        print(" ".join(args))
    else:
        print("No input provided. Usage: python echo.py [text to echo]")


if __name__ == "__main__":
    main()
