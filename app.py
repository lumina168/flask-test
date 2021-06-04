from flask import Flask, render_template,request,redirect,session
import sqlite3
app = Flask(__name__)

app.secret_key="sunabacoyatsushiro"

# flaskやるのにコレは必要おまじない①↑
# ===    ↓テスト   ==========================================================================

# /にURLで入力されたときなどにこちらが動く
@app.route('/', methods=["GET"])
def test_get():
    title = 'アンケート'

# /index.htmlのページで送信ボタンが押されたときなどにこちらが動く
@app.route('/', methods=["POST"])
def test_post(): 
    name = request.form.get("name")
    print(name)
    # dbファイルに接続
    conn = sqlite3.connect("flasktest.db")
    c = conn.cursor()
#     # SQL分でデータを取り出し
    c.execute("""select id from users where username =? """,(username))
    # dbに変更を書き込み
    user_id = c.fetchone()
# dbファイルとの接続を終了
    c.close()

    if user_id is None:
        return render_template("index.html")
    else:
        return render_template('/list',title=title)






# @app.route("/login")
# def login_get():
#     return render_template("login.html")

# @app.route('/login', methods=["POST"])
# def login_post(): 
#     username = request.form.get("username")
#     password = request.form.get("password")
# # # dbファイルに接続
#     conn = sqlite3.connect("flasktest.db")
#     c = conn.cursor()
# # # SQL分でデータを挿入
#     c.execute("""select id from users where username =? and password =?""", (username, password))
# # # dbに変更を書き込み
#     user_id = c.fetchone()
# # # dbファイルとの接続を終了
#     c.close()
# #                 ↓Noneで大文字にしないとエラーが出る
#     if user_id is None:
#         return render_template("login.html")
#     else:
#         return redirect("/list")    


# ＝＝＝＝＝   ↑テスト     ＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝


#①↓ここからそのままブラウザへ出力＃＃＃＃＃＃＃＃＃＃
# @app.route('/')
# def index():
#     title = 'アンケート'
#     return render_template('index.html',title=title)

@app.route('/hello')
def hello():
    return 'Hello, Worldだよ'
# ↑ここまでそのままブラウザへ出力
# ＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃

# コレが解らない↓usernameどこから引っ張るんだっけ＃＃＃＃＃＃＃
@app.route('/user/<username>')
def profile(username):
    return "ここは、" + username + "さんのプロフィールネームです"
# ＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃

# index.htmlに結びつかせる↓＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃
@app.route('/temptest')
def temptest():
    return render_template('index.html')
#                            ↑index.htmlに結びつかせる

@app.route('/extendtest')
def extendtest():
    return render_template('extendtest.html')
# ＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃

# ＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃
@app.route('/weather')
def weather():
# ↑これが被ったらエラー起こす。
    title = '今日の天気は'
    weather = "快晴"
    message = 'です'
    return render_template('weather.html', title=title, message=message, weather=weather)
#    ＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃↑どこと紐付けるか、、紐付けた先に出力titleにも反応

# ＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃
@app.route('/dbtest')
def dbtest():
# dbファイルに接続
    conn = sqlite3.connect("flasktest.db")
    c = conn.cursor()
# SQL分でデータを取り出し
    c.execute("""select name, age, address from users_test where id= 1""")
    user_info = c.fetchone()
# dbファイルとの接続を終了
    c.close()
# 取り出したデータの中身を確認
    print(user_info)
    return render_template('db.html', user_info=user_info)
    # エラー分はしっかり見る（エラー分が出てくるから）


@app.route('/dbkadai')
def dbkadai():
# dbファイルに接続
    conn = sqlite3.connect("flasktest.db")
    c = conn.cursor()
# SQL分でデータを取り出し
    c.execute("""select task from task where id= 1""")
    user_info = c.fetchone()
# dbファイルとの接続を終了
    c.close()
# 取り出したデータの中身を確認
    print(user_info)
    return render_template('db.kadai.html', user_info=user_info)
# ＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃


# 5/31始める=================================================================================

@app.route('/list')
def list():
    user_id=session["user_id"]
# dbファイルに接続
    conn = sqlite3.connect("flasktest.db")
    c = conn.cursor()
# SQL分でデータを取り出し
    c.execute("""select id, task from task""")
# 空のリストを作成だけする
    task_list = []
# fechallで全部取り出してfor文で①行ずつrowに渡す
    for row in c.fetchall():
# ①行ずつdictにしてtask_listに追加していく
# row[0]→１rou[1]→焼き肉を食べる
        task_list.append({"id":row[0],"task":row[1]})
# dbファイルとの接続を終了
    c.close()
# 取り出したデータの中身を確認
    print(task_list)
    return render_template('db..html', task_list=task_list,user_id=user_id)
#return入れたら関数止まる
# エラー分はしっかり見る（エラー分が出てくるから）

# =========================================================================================
# /addにURLで入力されたときなどにこちらが動く
@app.route('/add', methods=["GET"])
def add_get():
    return render_template("add.html")
# /addのページで送信ボタンが押されたときなどにこちらが動く
@app.route('/add', methods=["POST"])
def add_post(): 
    task = request.form.get("task")
    print(task)
# dbファイルに接続
    conn = sqlite3.connect("flasktest.db")
    c = conn.cursor()
# SQL分でデータを挿入↓データベースの中身
    c.execute("insert into task values(null, ?)",(task, ))
# dbに変更を書き込み
    conn.commit()
# dbファイルとの接続を終了
    c.close()
    return redirect ("/list")

# ==============================================================================
# 6/2のやつ
@app.route("/edit/<int:task_id>")
def edit_get(task_id):
    # dbから編集前の値を引いてくる
    # dbファイルに接続
    conn = sqlite3.connect("flasktest.db")
    c = conn.cursor()
# SQL分でデータを取り出し
    c.execute("select task from task where id = ?",(task_id,))
# 空のリストを作成だけする
    unedited_task= c.fetchone()[0]
# dbファイルとの接続を終了
    c.close()
    return render_template("edit.html",task_id=task_id,unedited_task=unedited_task)

@app.route('/edit', methods=["POST"])
def edit_post(): 
    task_id = request.form.get("task_id")
    task = request.form.get("task")
    print(task_id)
    print(task)
# # dbファイルに接続
    conn = sqlite3.connect("flasktest.db")
    c = conn.cursor()
# # SQL分でデータを挿入↓データベースの中身
    c.execute("update task set task = ? where id = ?",(task, task_id))
# # dbに変更を書き込み
    conn.commit()
# # dbファイルとの接続を終了
    c.close()
    return redirect ("/list")

@app.route("/delete/<int:task_id>")
def delete_get(task_id):
    # return render_template("delete.html")
# # dbファイルに接続
    conn = sqlite3.connect("flasktest.db")
    c = conn.cursor()
# # SQL分でデータを挿入↓データベースの中身
    c.execute("delete from task where id = ?",(task_id,))
# # dbに変更を書き込み
    conn.commit()
# # dbファイルとの接続を終了
    c.close()
    return redirect ("/list")


# @app.route('/delete', methods=["POST"])
# def delete_post(): 
#     task_id = request.form.get("task_id")
#     print(task_id)
# ＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝
@app.route("/regist")
def regist_get():
    return render_template("regist.html")

@app.route('/regist', methods=["POST"])
def regist_post(): 
    username = request.form.get("username")
    password = request.form.get("password")
# # dbファイルに接続
    conn = sqlite3.connect("flasktest.db")
    c = conn.cursor()
# # SQL分でデータを挿入
    c.execute("""insert into users values 
    (null, ?, ?)""", (username, password))
# # dbに変更を書き込み
    conn.commit()
# # dbファイルとの接続を終了
    c.close()
    return "登録が完了しました"
    
# ＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝


@app.route("/login")
def login_get():
    return render_template("login.html")

@app.route('/login', methods=["POST"])
def login_post(): 
    username = request.form.get("username")
    password = request.form.get("password")
# # dbファイルに接続
    conn = sqlite3.connect("flasktest.db")
    c = conn.cursor()
# # SQL分でデータを挿入
    c.execute("""select id from users where username =? and password =?""", (username, password))
# # dbに変更を書き込み
    user_id = c.fetchone()
# # dbファイルとの接続を終了
    c.close()
#                 ↓Noneで大文字にしないとエラーが出る
    if user_id is None:
        return render_template("login.html")
    else:
        session["user_id"]= user_id
        return redirect("/list")    

# =================================================================-
# flaskやるのにコレは必要↓おまじない②
if __name__ == "__main__":
    app.run(debug=True)
#   ↑これがないと変更した時リロードしてもページ変わらない


# エラー分はしっかり見る（エラー分が出てくるから）