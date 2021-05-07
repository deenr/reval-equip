import configparser
import os


def get_database_path():
    config = configparser.ConfigParser()
    config.read(os.getcwd() + os.path.sep + 'reval-config.ini')
    db_name = config['DEFAULT']['db_f_name']

    return 'database/' + db_name


def get_files_directory():
    return 'database/files'
