
import os


def find_files(suffix, path):

    if os.path.isdir(path) == False:
        raise Exception('Please Provide Valid Directory')

    paths = os.listdir(path)
    files = []
    for p in paths:
        file_path = Path(p, path, suffix)
        if file_path.is_directory():
            files += find_files(suffix, file_path.path)
        if file_path.matches_suffix():
            files.append(file_path.path)

    return files


class Path:
    def __init__(self, path, root, suffix):
        self.path = os.path.join(root, path)
        self.suffix = suffix

    def is_directory(self):
        return os.path.isdir(self.path)

    def matches_suffix(self):
        return os.path.isfile(self.path) and self.path.endswith(self.suffix)
