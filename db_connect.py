import pymysql


def connect():
    # Connection herstellen
    conn = pymysql.connect(host='127.0.0.1',
                           port=3306,
                           user='root',
                           passwd='admin',
                           db='mysql')

    # eine bestimmte Verbindungsart
    cur = conn.cursor()

    # SQL-Query
    cur.execute('SELECT Host, User FROM user')

    # Ergebnis ausgeben
    for r in cur:
        print(r)

    # Cursor und Connection schließen
    cur.close()
    conn.close()
