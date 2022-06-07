import mysql
from flask import Flask, render_template, request

from test.dao.BookDao import BookDao
from test.entity.BookBean import BookBean

app = Flask(__name__)


@app.route('/BookModifyServlet/', methods=['POST'])
def book_modify():
    count = 0

    booktitle = request.form['booktitle']
    dao = BookDao()

    try:

        if booktitle != None:

            authorname = request.form["authorname"]

            book = BookBean()

            book.setBookTitle(booktitle)
            book.setAuthorName(authorname)

            count = dao.insert(book)
        else:
            ids = request.form['book']
            if ids == None:
                pass
            else:
                count = dao.delete(ids)
    except mysql.connector.Error:
        print('DB操作エラー')
    except ModuleNotFoundError:
        print('モジュールがみつかりません')

    return render_template('serch.py')


if __name__ == '__main__':
    app.run()