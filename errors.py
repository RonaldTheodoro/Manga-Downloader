import os
import timeit


def check_if_file_exists(local_filename):
    if os.path.exists(local_filename):
        print('{} was already downloaded'.format(
            local_filename.split('/')[-1]))
        return True
    return False


def show_error_msg(status_code):
    print('File not find, Error: {}'.format(status_code))
