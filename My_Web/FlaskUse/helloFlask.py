from flask import Flask, request, render_template, redirect, Response, session
from settings import config
from flask_sqlalchemy import SQLAlchemy

import os

app = Flask(__name__)
app.config.from_object(config['development'])
app.secret_key = os.urandom(25)

db = SQLAlchemy(app)

class Roles(db.Model):
    __tablename__ = 'Roles'
    rid = db.Column(db.Integer, primary_key=True)
    rname = db.Column(db.String(32))

    def __init__(self):
        self.rname = rname
    
    def __repr__(self):
        return 'Roles:[%s,%s]' %(self.rid, self.rname)





db.create_all()













@app.route('/')
def gotoIndex():
    return '你好，Flask！'


@app.route('/user/<username>')
def gotoHello(username):
    return '你好，%s！'% username


@app.route('/login', methods=['GET', 'POST'])
def gotoLogin():
    if request.method == 'POST':
        loginAccount = request.values.get('loginAccount', None)
        loginPassword = request.values.get('loginPassword', None)
        remember = request.values.get('remember', None)
        if loginAccount=='admin' and loginPassword=='123':
            session['account'] = 'admin'

            msg = '登陆成功'
            resp = Response('你好！', session.get('account'))
            resp = Response(render_template('login.html', msg=msg))
            
            if remember:
                resp.set_cookie('loginAccount', loginAccount)
        else:

            return render_template('login.html',msg = '用户名或密码错误')

        return resp
    else:
        loginAccount = request.cookies.get('loginAccount', None)
        if loginAccount:
            return render_template('login.html', loginAccount=loginAccount)
        else:
            return render_template('login.html')
        

@app.route('/user/method/')
def gotoPara():
    userid = int(request.args.get('userid'))
    return 'userid:%s' % userid




@app.route('/search', methods=['GET', 'POST'])
def gotoSreach():
    if request.method == 'POST':
        keyword = request.values.get('keywords', None)
        msg = '搜索关键字为：%s' % keyword
        resp = Response(render_template('search.html', msg=msg, msg1=msg))
        resp.set_cookie('keyword', keyword)
        return resp
    else:
        return render_template('search.html')







if __name__ == '__main__':
    app.run()
