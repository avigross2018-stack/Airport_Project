from pathlib import Path
import csv
from actions_on_files import read_csv
airport_entry_file = Path('./airport_entry_fee.csv')
def file_exist(path):
    '''
    Docstring for file_exist
    check if file exist and return bool
    :param path: var with path from pathlib
    '''
    if path.exists():
        return True
    return False

def manager_authentication(manager_name, manager_pw, file_path):
    '''
    Docstring for manager_authentication
    compare between manager info and credentials.csv
    :param manager_name: get str name
    :param manager_pw: get str password
    :param file_path: get variable that contain check_csv function
    '''
    manager_info = [manager_name, manager_pw]
    flag = False
    for list in file_path:
        if manager_info == list:
            flag = True
    return flag


def read_airports_file(path):
        airports_list = []      
        with open(path, 'r') as f:
            airports = csv.DictReader(f)
            for row in airports:
                airports_list.append(dict(row))
        return airports_list

