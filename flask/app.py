from flask import Flask,request,jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


# mulASAAGVHAI
app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:gandapuri@localhost/practise_db'
db = SQLAlchemy(app)

migrate= Migrate(app,db)



class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password=db.Column(db.String(50),nullable=False)


with app.app_context():
    db.create_all()
@app.route('/')
def home():
    return 'Hello World!!'



@app.route('/signup',methods=['POST'])
def signup():
    data=request.get_json()
    
    if check_email_no_exists(data['email']):

        response={'status':'success'}
        add_user(data)
        
    else:
        response={'status':'failed','error':'email already exists'}
        view_all_user()
    return jsonify(response)

@app.route("/login",methods=['GET'])
def login():
    data=request.get_json()
    print(data)
    if check_email_no_exists(data['email']):
        response={'status':'failed','error':'No email found'}
    elif not check_password(data):
        response={'status':'failed','error':'Password don\'t match'}
    else:
        response={'status':'success'}
    return jsonify(response)
        
def check_password(data):
    result=db.session.query(User).filter_by(email=data['email']).first()
    if result.password== data['password']:
        return True
    return False
def check_email_no_exists(data):
    result=db.session.query(User).filter_by(email=data).first()
    if result is None:
        return True
    return False

def add_user(data):
    new_user= User(name=data['name'],email=data['email'],password=data['password'])
    db.session.add(new_user)
    db.session.commit()

def view_all_user():
    users=db.session.query(User)
    print(type(users))
    for user in users:
        print(f"USer {user.id}: {user.email}:{user.password}")


if __name__=='__main__':
    app.run()