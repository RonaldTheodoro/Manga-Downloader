import os
import requests
from errors import check_if_file_exists
from errors import show_error_msg
from status_bar import create_status_bar_iterable


def download_file(url):
    local_filename = download_path(url)

    if not check_if_file_exists(local_filename):
        response = requests_get(url)

        if response.status_code != 200:
            show_error_msg(response.status_code)
        else:
            write_file(local_filename, response)


def download_path(url):
    return os.path.join(
        os.path.dirname(__file__), 'download', url.split('/')[-1])


def requests_get(url):
    return requests.get(url, stream=True)


def write_file(local_filename, response):
    with open(local_filename, 'wb') as file:
        download_chunks(file, response)


def download_chunks(file, response):
    for chunk in create_status_bar_iterable(response): 
        if chunk:
            file.write(chunk)
            file.flush()
