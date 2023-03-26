from find_files import find_files


def test_test_dir():
    files_end_with_c = find_files(".c", "./testdir")
    print(files_end_with_c)
    assert (len(files_end_with_c) == 4)


def test_empty_dir():
    files_end_with_c = find_files(".c", "./empty")
    print(files_end_with_c)
    assert (len(files_end_with_c) == 0)


def test_non_exists_dir():
    try:
        files_end_with_c = find_files(".c", "./fahad")
        print(files_end_with_c)
        assert (False == True)
    except:
        print("Exception")
