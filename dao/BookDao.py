import mysql

from test.dao.ConnectionManager import ConnectionManager


class BookDao:
    # 引数で本の名前と著者名を受け取りデータベースに接続し、あいまい検索を行い、
    # レコードの内容をタプル型の配列にした要素を持つ多次元データの結果を返す
    def select(self, param):
        try:
            connect = ConnectionManager()
            cnx = connect.getConnection()
            cursor = cnx.cursor()
            params = ("%" + param.get_booktitle() + "%", "%" + param.get_authorname() + "%")
            cursor.execute("SELECT * FROM m_book WHERE book_title LIKE %s AND author_name LIKE %s", params)

            # 結果をタプル型でまとめて返すメソッド
            booklist = cursor.fetchall()
        except mysql.connector.Error:

            print('DBに接続できませんでした。')

        else:

            cnx.close()

        return booklist

    def insert(self, book):
        connect = ConnectionManager()
        cnx = connect.getConnection()

        cursor = cnx.cursor()
        params = (book.get_booktitle(), book.get_authorname())
        cursor.execute("INSERT INTO m_book (book_title, author_name) VALUES(%s, %s)", params)

        # 更新件数を受け取る処理
        cursor.fetchall()
        count = cursor.rowcount
        cnx.commit()
        cursor.close()
        cnx.close()
        return count


