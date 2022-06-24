import os


def list_files(path : str = os.curdir):
    return list(filter(lambda file: os.path.isfile(file), os.listdir(path)))


def rename_file(src, dest, dir = os.curdir):
    src = os.path.join(dir, src)
    dest = os.path.join(dir, dest)
    os.rename(src, dest)


def create_file(name, dir = os.curdir):
    name = os.path.join(dir, name)
    open(name, "w").close()


