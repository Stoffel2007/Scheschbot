import telegram
import pymysql


def main():
   print(1)

   # Also hier macht man die Connection
   conn = pymysql.connect(host='127.0.0.1',
                          port=3306,
                          user='root',
                          passwd=None,
                          db='mysql')

   # Irgendeine Art von Verbindung ?
   cur = conn.cursor()

   # Die eigentliche SQL Abfrage wie man sie in SQL schreiben würde
   # aus der "user" Tabelle werden alle Hosts und der dazu gehörige User abgefragt
   cur.execute("SELECT Host,User FROM user")

   # Ausgabe des Resultsets (Daten aus den Zeilen)
   for r in cur:
      print(r)

   # Komische Verbindung schließen
   cur.close()
   print(2)

   # Connection schließen
   conn.close()

if __name__ == '__main__':
    main()