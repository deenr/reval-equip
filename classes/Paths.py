import configparser
import os


def get_database_path():
    config = configparser.ConfigParser()
    config.read(os.getcwd() + os.path.sep + 'reval-config.ini')
    db_name = config['DEFAULT']['db_f_name']

    project_path = str(os.getcwd()).split('\\')
    project_path[-1] = 'reval-database'
    database_path = ''
    for p in project_path:
        database_path = database_path + p + '\\'
    # return database_path + db_name
    return 'database/' + db_name
