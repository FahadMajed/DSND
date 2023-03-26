## Locally save and call this file ex.py ##

# Code to demonstrate the use of some of the OS modules in python

import os


def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.
    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.
    There are no limit to the depth of the subdirectories can be.
    Args:
    suffix(str): suffix if the file name to be found
    path(str): path of the file system
    Returns:
    a list of paths
    """

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
