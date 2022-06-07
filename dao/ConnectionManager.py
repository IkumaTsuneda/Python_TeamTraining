import mysql.connector


class ConnectionManager:

    def getConnection(self):
        try:
            cnx = mysql.connector.connect(
                user='root',
                password='root',
                host='127.0.0.1',
                database='book_db'
            )
        except mysql.connector.Error:
            print('DBに接続できませんでした。')
        return cnx