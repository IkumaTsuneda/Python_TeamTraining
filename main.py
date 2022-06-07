import datetime
import cgitb

import mysql
from flask import Flask, render_template, request

from test.dao.BookDao import BookDao
from test.entity.BookBean import BookBean

app = Flask(__name__)


# 書籍検索画面
@app.route('/')
def search():
    # 書籍検索画面を表示
    return render_template('search.html')


@app.route('/BookManagerServlet', methods=['POST'])
def book_manager():
    booktitle = request.form['booktitle']
    authorname = request.form['authorname']
    param = BookBean()
    dao = BookDao()
    try:
        param.set_booktitle(booktitle)
        param.set_authorname(authorname)
        bookList = (list(dao.select(param)))
        
        if len(bookList) == 0:
            bookList = None


    except mysql.connector.Error:
        print('DB操作エラー')
    except ModuleNotFoundError:
        print('モジュールがみつかりません')

    return render_template('/search.html/', bookList=bookList)


# 書籍登録画面
@app.route('/create/')
def create():
    # 書籍登録画面を表示
    return render_template('create.html')


@app.route('/BookModifyServlet', methods=['POST'])
def book_modify():
    count = 0

    booktitle = request.form['booktitle']
    dao = BookDao()

    try:


            authorname = request.form["authorname"]

            book = BookBean()

            book.set_booktitle(booktitle)
            book.set_authorname(authorname)

            count = dao.insert(book)

    except mysql.connector.Error:
        print('DB操作エラー')
    except ModuleNotFoundError:
        print('モジュールがみつかりません')

    return render_template('search.html')


if __name__ == '__main__':
    app.run()
