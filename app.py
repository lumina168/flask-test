from flask import Flask, render_template
import sqlite3
app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return 'Hello, World'

@app.route('/user/<username>')
def profile(username):
    return "ここは、"+username+"さんのプロフィールネームです"


@app.route('/temptest')
def temptest():
    return render_template('index.html')

@app.route('/extendtest')
def extendtest():
    return render_template('extendtest.html')


@app.route('/weather')
def weather():
    # ↑これが被ったらエラー起こす。だから上をメッセージ用にして消した
    weather = "快晴"
    title = '今日の天気は'
    message = '快晴'
    return render_template('index.html', title=title, message=message, weather=weather)



@app.route('/dbtest')
def dbtest():
    # dbファイルに接続
    conn = sqlite3.connect("flasktest.db")
    c = conn.cursor()
    # SQL分でデータを取り出し
    c.execute("""select name, age, address from users where id= 1""")
    user_info = c.fetchone()
    # dbファイルとの接続を終了
    c.close()
    # 取り出したデータの中身を確認
    print(user_info)
    return render_template('db.html', user_info=user_info)
    # エラー分はしっかり見る（エラー分が出てくるから）

if __name__ == "__main__":
    app.run(debug=True)
            #   ↑これがないと変更した時リロードしてもページ変わらない
