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
    return engine

def call_query(engine, query):
    '''
    Calls a query from the SQLite database,
    turn it into a dataframe,
    and print the result
    :param query: SQL query
    :return: df dataframe
    '''
    # open engine connection
    con = engine.connect()

    # perform queries on selected tables
    rs = con.execute(query)

    # save results in a dataframe
    df = pd.DataFrame(rs.fetchall())

    # close connection
    con.close()

    print(df)