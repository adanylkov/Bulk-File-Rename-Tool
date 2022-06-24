def get_line():
    return input("> ")

def get_lines(line_names : list):
    ret = []
    for name in line_names:
        print(name)
        ret.append(input("> "))
    return ret


def print_menu(menu_header : str, menu_items : list):
    print(menu_header)
    for i, item in enumerate(menu_items):
        print(f"{i+1}. {item}")
    print("0. Exit")
