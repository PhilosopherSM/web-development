from flask import Flask, request, render_template


def register(username, pwd):
    try:
        f = open('.\\data\\' + username, mode='x')
        f.write(username + '\n' + pwd)
        f.close()
        return True
    except FileExistsError:
        print('用户名重复')
        return False


def check_psw(username, pwd):
    try:
        f = open('.\\data\\' + username, 'r')
        if f.readlines()[1] == pwd:
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


@app.route('/hello', methods=['POST'])
def hello_page():
    username = request.form.get('userName')
    pwd = request.form.get('passWord')

    if register(username, pwd) is True:
        return render_template('registered.html', username=username)
    else:
        return render_template('registration.html', msg='用户名重复')


if __name__ == '__main__':
    app.run(debug=True)
