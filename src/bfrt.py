import sys


def main():
    argc = len(sys.argv)
    if argc < 3:
        print(f"Usage: {sys.argv[0]} <option> <filenames>")
        sys.exit(1)


if __name__ == "__main__":
    main()
