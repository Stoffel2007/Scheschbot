import pymysql


def query(query_string):
    try:
        # Connection herstellen
        connection = pymysql.connect(host='localhost',
                                     port=3306,
                                     user='root',
                                     passwd='',
                                     db='scheschbot')

        # Verbindungsart Cursor
        cursor = connection.cursor()
        cursor.execute(query_string)

        # Cursor und Connection schließen
        cursor.close()
        connection.close()

        return cursor
    except pymysql.err.OperationalError:
        print("Error connecting to the database")
        return False
