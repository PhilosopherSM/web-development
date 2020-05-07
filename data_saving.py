from flask import Flask, request, render_template


def register(username, psw):
    try:
        f = open('.\\data\\' + username, 'x')
        f.write(username + '\n' + psw)
        f.close()
        return True
    except FileExistsError:
        print('用户名重复')
        return False


def check_psw(username, psw):
    try:
        f = open('.\\data\\' + username, 'r')
        if f.readlines()[1] == psw:
            f.close()
            return True
        else:
            f.close()
            print('密码错误')
            return False

    except FileNotFoundError:
        print('没有此用户信息')
        return '404'


app = Flask(__name__)


@app.route('/')
def register_page():
    return render_template('registration.html')


@app.route('/hello', methods=['GET', 'POST'])
def hello_page():
    register(request.form['userName'], request.form['passWord'])
    return render_template('registered.html', username=request.form['userName'])


if __name__ == '__main__':
    app.run()
