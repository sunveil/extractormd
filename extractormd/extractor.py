import hashlib
import os
import re
from datetime import datetime

__RUN_DATE = 2


def extract_from_file(path):
    sha1 = __get_sha1(path)
    portion = __extract_period(path)
    run_date = __extract_run_date(path)
    facility_id = __extract_facility(path)
    season_id = __extract_season(path)
    period_id = __extract_period(path)
    run_id = __extract_run(path)
    cluster_id = __extract_cluster(path)
    return {
        'sha1': sha1,
        'portion': portion,
        'full_path': path,
        'run_date': run_date,
        'facility_id': facility_id,
        'season_id': season_id,
        'period_id': period_id,
        'run_id': run_id,
        'cluster_id': cluster_id,
        'flags': "00000000"
    }


def check_path(path):
    regex = r"/\w+/(DATA(_|-)(IACT)/(\d{4}-\d{2})/(\w{5})/(\d{6}.?\d*.?\w*)/(\w{3}\d{2})/(\w*.?\w*))"
    pattern = re.compile(regex)
    m = pattern.match(path)
    if m:
        return True
    return False


def __get_sha1(path):
    # f = open(path)
    # read = f.read()
    # return hashlib.sha1(read)
    return "da39a3ee5e6b4b0d3255bfef95601890afd80709"


def __extract_cluster(path):
    return "1"


def __extract_from_folder(folder):
    return "1"


def __extract_portion(path):
    return "1"


def __extract_run_date(path):
    path_list = path.split(os.sep)
    path_list.reverse()
    run = path_list[__RUN_DATE]
    run_date = run.split(".")[0]
    date_time = datetime.strptime(run_date, "%m%d%y").strftime("%Y-%m-%dT%H:%M:%S")
    return date_time


def __extract_facility(path):
    return "1"


def __extract_season(path):
    return "1"


def __extract_period(path):
    return "1"


def __extract_run(path):
    return "1"
