import string
import model.file_reader as model


availible_options = {
    'rename': 'rename',
    'r': 'rename',
    'create': 'create',
    'c': 'create',
    'count': 'count',
    't': 'count'
}

incompactible = {
        'rename': ['create',],
        'create': ['rename',],
        }


def parse_arguments(arguments):
    assert isinstance(arguments, list)
    actions, filenames = [], None
    for argument in arguments:
        if argument.startswith('--'):
            actions.append(long_argument(argument))
        elif argument.startswith('-'):
            action = short_argument(argument)
            if action:
                actions.extend(action)
        else:
            filenames = argument
    if filenames:
        return actions, filenames.split()
    return actions, None


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
    if not actions: return False
    for option in actions:
        if option == 'rename':
            if len(actions) > 1:
                print("--rename cannot be used with other options")
                return False
        elif option == 'create':
            if 'count' not in actions:
                print("--create has to be used with --count")
                return False
    return True


def handle_files(filenames : list):
    if not filenames:
        return None, None
    *files, pattern = filenames
    if '*' not in pattern or pattern.count('*') != 1:
        return None, None
    return files, pattern


def generate_filenames(filenames: list, pattern : 'str', count=None):
    if not pattern:
        print("Please add pattern name at the end 'image*.jpg'")
        exit(1)

    prefix, suffix = pattern.split('*')
    for i in range(count or len(filenames)):
        yield f"{prefix}{i}{suffix}"


def get_count(arguments : list):
    try:
        index = arguments.index('--count')
    except ValueError:
        index = None
        for i, arg in enumerate(arguments):
            if arg.startswith('-'):
                if 't' in arg: index = i; break

    if index is not None:
        count = arguments.pop(index + 1)
        if count.isdigit(): return int(count)
        else: print(f"count value: {count} is not digit")
    else: print("No count specified"); exit(1)


def main(arguments):
    actions, filenames = parse_arguments(arguments)
    if not filenames:
        print("Please add pattern name at the end 'image*.jpg'")
        exit(1)

    if filenames and check_compactible(actions):
        filenames, pattern = handle_files(filenames)
        if not filenames: filenames = model.list_files()

        for action in actions:
            if action == 'rename':
                generator = generate_filenames(filenames, pattern)
                for filename, new_filename in zip(filenames, generator):
                        model.rename_file(filename, new_filename)
            elif action == 'create':
                count = get_count(arguments)
                generator = generate_filenames(filenames, pattern, count=count)
                for new_filename in generator:
                    model.create_file(new_filename)
