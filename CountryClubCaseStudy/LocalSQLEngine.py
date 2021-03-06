from sqlalchemy import create_engine
import pandas as pd

def create_sql_engine(db_file):
    '''
    creates connection to a SQLite database specified by db_file
    :param db_file: database file
    :return: engine or None
    '''
    engine = None
    try:
        engine = create_engine(db_file)
        print('connection established')
    except Error as e:
        print(e)
    return engine

def select_table(engine):
    '''
    Query all rows from the table
    :param conn: connection object
    :return: None
    '''
    # connect to engine
    con = engine.connect()

    # select table for query
    query = 'SELECT * FROM FACILITIES'

    # perform queries on selected tables
    rs = con.execute(query)

    # fetch results
    rows = rs.fetchall()

    # close connection
    con.close()

    for row in rows:
        print(row)

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