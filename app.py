from flask import Flask, session, render_template
from flask_restful import Api
from resources.login import *
from resources.function import*
from dotenv import load_dotenv
from datetime import date, datetime, time, timedelta
import pymongo,os,certifi

load_dotenv()

#初始化資料庫連線
client=pymongo.MongoClient("mongodb+srv://"+os.getenv("mongodb")+".rpebx.mongodb.net/myFirstDatabase?retryWrites=true&w=majority",tlsCAFile=certifi.where())
db=client.order_system_v2
users=db['users']
customer=db.customer
print('\x1b[6;30;42m' + '資料庫連線成功'.center(87) + '\x1b[0m')

app = Flask(__name__)
app.secret_key =os.getenv('secret_key')


# 登入檢查裝飾器
def login_required(func):
    def wrapper(*args, **kwargs):
        if 'username' in session:
            return func(*args, **kwargs)
        else:
            flash('請先登入')
            return redirect('/login')
    return wrapper

# 加載api
api = Api(app)
api.add_resource(LoginResource, '/login', resource_class_kwargs={'users': users})
api.add_resource(LogoutResource, '/logout')
api.add_resource(RegisterResource, '/register', resource_class_kwargs={'users': users})

@app.before_request
def before_request():
    session.permanent = True
    app.permanent_session_lifetime = timedelta(days=30)  # 設定 session 的有效期限

# 登入頁面
@app.route('/login')
def login():
    return render_template('login.html')

#Home_page
@app.route('/')
@login_required
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True,port=5500)
