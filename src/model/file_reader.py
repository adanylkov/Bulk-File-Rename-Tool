import os


def list_files(path : str):
    return os.listdir(path)


def rename_file(dir, src, dest):
    src = os.path.join(dir, src)
    dest = os.path.join(dir, dest)
    os.rename(src, dest)


if __name__ == "__main__":
    rename_file(os.curdir, 'test.txt', 'supertest.txt')
