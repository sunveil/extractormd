from extractormd import extractor
from graphqlclient import GraphQLClient
import fnmatch
import argparse
import os

__END_PINT_URL = 'http://gridmsu34.sinp.msu.ru:5000/graphql'
__REGEXP = r"/\w+/(DATA(_|-)(IACT)/(\d{4}-\d{2})/(\w{5})/(\d{6}.?\d*.?\w*)/(\w{3}\d{2})/(\w*.?\w*))"


def main():
    path = "/k2/DATA_IACT/2016-17/dec16/011216/BSM05/010101.01"

    client = GraphQLClient(__END_PINT_URL)

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
                if extractor.check_path(path):
                    print(path)
                else:
                    exit(1)

                variables = extractor.extract_from_file(path)

                mutation = '''mutation Mtfm
                {{
                    createFile(input:
                        {{
                            sha1: "{sha1}",
                            portion: "{portion}",
                            fullPath: "{full_path}",
                            runDate: "{run_date}",
                            facillityId: "{facility_id}",
                            seasonId: "{season_id}",
                            periodId: "{period_id}",
                            runId: "{run_id}",
                            clusterId: "{cluster_id}",
                            flags: "{flags}"
                        }}) {{
                    file
                        {{
                            fid,
                            sha1,
                            portion,
                            fullPath,
                            runDate,
                            facillityId,
                            seasonId,
                            periodId,
                            runId,
                            clusterId,
                            flags
                        }}
                    }}
                }}'''

                mutation = mutation.format(**variables)
                print(mutation)
                result = client.execute(mutation)
                if result:
                    print("ok")



if __name__ == '__main__':
    main()
