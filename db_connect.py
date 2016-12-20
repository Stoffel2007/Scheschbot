import pymysql


def query(query_string):
    # Connection herstellen
    connection = pymysql.connect(host='localhost',
                                 port=3306,
                                 user='root',
                                 passwd='',
                                 db='scheschbot')

    query_string = 'SELECT * FROM users'
    # Verbindungsart Cursor
    cursor = connection.cursor()
    cursor.execute(query_string)

    # Cursor und Connection schließen
    cursor.close()
    connection.close()

    return cursor
