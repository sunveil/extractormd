from extractormd import extractor
from graphqlclient import GraphQLClient
import fnmatch
import argparse
import os


__END_PINT_URL = 'http://gridmsu34.sinp.msu.ru:5000/graphql'
__REGEXP = r"/\w+/(DATA(_|-)(IACT)/(\d{4}-\d{2})/(\w{5})/(\d{6}.?\d*.?\w*)/(\w{3}\d{2})/(\w*.?\w*))"


def main():
    path = "/k2/DATA_IACT/2016-17/dec16/011216/BSM05/010101.01"
    if extractor.check_path(path):
        print(path)

    parser = argparse.ArgumentParser()
    parser.add_argument('path', help='input folder for processing')
    args = parser.parse_args()
    root_dir = args.path
    is_dir = os.path.isdir(root_dir)
    if not is_dir:
        raise Exception('It is not a directory')

    for dir_name, subdir_list, file_list in os.walk(root_dir):
        for file_name in fnmatch.filter(file_list, "*"):
            path = os.path.join(dir_name, file_name)
            if extractor.check_path(path):
                print(path)

    client = GraphQLClient(__END_PINT_URL)

#    result = client.execute('''
#        query{
#          files{
#            fid,
#            fullPath
#          }
#        }
#        ''')


if __name__ == '__main__':
    main()
