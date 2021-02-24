"""Open source-file, parse Urls and write parsed Urls to timestamp directory"""

import argparse
import re
import os

from datetime import datetime


def create_parse_args():
    """Create command line arguments"""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-s', '--source_file',
        help='path to file with urls you need to parse'
    )
    parser.add_argument(
        '-n', '--number_of_urls',
        default=2000,
        help='portion of urls in the list to write to file'
    )
    args = parser.parse_args()
    return args


def create_timestamp_directory(directory_path):
    """Create directory for output with timestamp"""
    dir_with_parsed_urls = f'{directory_path}/{datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}'
    os.makedirs(dir_with_parsed_urls)
    return dir_with_parsed_urls


def parse_urls(url):
    """Remove everything from the url except the domain and path"""
    parsed_url = re.sub(r'^\w+://|www\.|[^/]+$', '', url)
    return parsed_url


def open_source_file(file):
    """Open file with unparsed urls"""
    file_with_urls = open(format(file))
    return file_with_urls


def write_parsed_urls():
    """Write parsed urls to timestamp directory"""
    with open_source_file(create_parse_args().args.source_file) as urls:
        list_of_valid_urls = list()
        with open(
                os.path.join(
                    create_timestamp_directory('data'),
                    'parsed_urls.txt'), 'w') as parsed_urls:
            for item in urls:
                valid_url = parse_urls(item)
                if len(list_of_valid_urls) == create_parse_args().number_of_urls:
                    parsed_urls.writelines(list_of_valid_urls)
                    list_of_valid_urls = list()
                else:
                    list_of_valid_urls.append(valid_url + '\n')
            if list_of_valid_urls:
                parsed_urls.writelines(list_of_valid_urls)


if __name__ == '__main__':
    write_parsed_urls()
