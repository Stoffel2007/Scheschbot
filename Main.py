import db_connect


def main():
    result = db_connect.query('SELECT * FROM users')
    for line in result:
        print(line)


if __name__ == '__main__':
    main()
