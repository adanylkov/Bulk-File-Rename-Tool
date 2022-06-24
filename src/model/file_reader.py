import os


def list_files(path : str):
    return os.listdir(path)


def rename_file(dir, src, dest):
    src = os.path.join(dir, src)
    dest = os.path.join(dir, dest)
    os.rename(src, dest)


def create_file(dir, name):
    name = os.path.join(dir, name)
    open(name, "w").close()
