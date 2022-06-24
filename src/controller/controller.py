import string


availible_options = {
    'rename': 'rename',
    'r': 'rename',
    'create': 'create',
    'c': 'create',
}

incompactible = {
        'rename': ['create',],
        'create': ['rename',],
        }


def parse_arguments(arguments):
    assert isinstance(arguments, list)
    actions, filenames = [], []
    for argument in arguments:
        if argument.startswith('--'):
            actions.append(long_argument(argument))
        elif argument.startswith('-'):
            action = short_argument(argument)
            if action:
                actions.extend(action)
        else:
            filenames.append(argument)
    return actions, filenames


def long_argument(argument):
    argument = argument.removeprefix('--')
    return availible_options.get(argument)


def short_argument(argument):
    options = []
    for option in argument.removeprefix('-'):
        if option not in string.ascii_lowercase:
            return None
        options.append(availible_options.get(option))
    return options


def check_compactible(actions : list):
    for option in actions:
        incompactible_actions = incompactible.get(option, [])
        for action in incompactible_actions:
            if action in actions:
                return False
    return True

if __name__ == "__main__":
    a = parse_arguments(['-r', '--rename', 'file'])
    print(a)
    print(check_compactible(a[0]))
