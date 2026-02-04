from pathlib import Path
def file_exist(path):
    '''
    Docstring for file_exist
    check if file exist and return bool
    :param path: var with path from pathlib
    '''
    if path.exists():
        return True
    return False

