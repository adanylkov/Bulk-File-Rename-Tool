import sys
import controller.controller as controller


def main():
    argc = len(sys.argv)
    if argc < 3:
        print(f"Usage: {sys.argv[0]} <option> <filenames>")
        sys.exit(1)
    controller.main(sys.argv[1:])
        


if __name__ == "__main__":
    main()
