import pymysql


def query(db_name, query_string):
    # Connection herstellen
    connection = pymysql.connect(host='127.0.0.1',
                                 port=3306,
                                 user='root',
                                 passwd='',
                                 db=db_name)

    # Verbindungsart Cursor
    cursor = connection.cursor()
    cursor.execute(query_string)

    # Cursor und Connection schließen
    cursor.close()
    connection.close()

    return cursor
