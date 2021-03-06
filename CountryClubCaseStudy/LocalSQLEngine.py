from sqlalchemy import create_engine
import pandas as pd

def create_engine(db_file):
    '''
    creates connection to a SQLite database specified by db_file
    :param db_file: database file
    :return: engine or None
    '''
    engine = None
    try:
        engine = create_engine('sqlite:///sqlite_db_pythonsqlite.db')
    except Error as e:
        print(e)