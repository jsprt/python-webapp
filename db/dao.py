import psycopg2
import sys
from db import PG_DB
from db import PG_PASS
from db import PG_USER
from db import PG_HOST


def connect(params):
    """ Connect to DB """
    try:
        return psycopg2.connect(**params)
    except:
        e = sys.exc_info()[0]
        raise Exception(f'Unable to connect to database. {e}')


def version(connection):
    """ Fetch version """
    cur = connection.cursor()

    cur.execute('SELECT version()')

    db_version = cur.fetchone()

    # close the communication with the PostgreSQL
    cur.close()

    return db_version[0]


def query():
    """ Query DB """
    conn = connect({'dbname': PG_DB,
                    'user': PG_USER,
                    'host': PG_HOST,
                    'password': PG_PASS})

    return version(conn)


if __name__ == '__main__':
    query()
