import db_connect


def main():
    result = db_connect.query('mysql', 'SELECT Host, User FROM user')
    for line in result:
        print(line)


if __name__ == '__main__':
    main()
