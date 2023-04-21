import sys
import os.path


def get_full_path(path):
    return os.path.abspath(path)


def file_exists(path):
    return os.path.isfile(path)


def get_file_size(file_path):
    try:
        return os.path.getsize(file_path)
    except OSError:
        file_error(file_path)


def open_file_for_reading(file_path):
    try:
        return open(file_path, "rt")
    except OSError:
        file_error(file_path)


def file_error(path):
    if not isinstance(path, str) or path == "":
        path = "Filename"
    print(f"""Wrong filename! {path} does not exist or is not a file!
If {path} shoud exist, check if you have read permission!
Exiting...""")
    sys.exit(1)


def zero_arguments():
    version = "0.1"
    print(f"""You didn't supply any arguments!
Usage: python3 binSearch.py [FILE]
Version: {version}""")
    sys.exit(1)


if __name__ == '__main__':

    if len(sys.argv) == 1:
        zero_arguments()

    path_from_cl = sys.argv[1]
    file_path = get_full_path(path_from_cl)

    if file_exists(file_path) == False:
        file_size = get_file_size(file_path)
        print(f"File {path_from_cl} exists and has {file_size} bytes")
    else:
        file_error(path_from_cl)
