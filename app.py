from flask import Flask, render_template
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


# @app.route('/temptest')
# def temptest():
#     return render_template('index.html')

@app.route('/extendtest')
def extendtest():
    return render_template('extendtest.html')


@app.route('/temptest')
def temptest():
    # ↑これが被ったらエラー起こす。だから上をメッセージ用にして消した
    title = 'indexページ'
    message = 'ここにはメッセージが入ります。ここにはメッセージが入ります。'
    return render_template('index.html', title=title, message=message)

if __name__ == "__main__":
    app.run(debug=True)
            #   ↑これがないと変更した時リロードしてもページ変わらない
