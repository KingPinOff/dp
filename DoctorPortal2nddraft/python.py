import firebase_admin
from firebase_admin import auth
from firebase_admin import credentials
from firebase_admin import auth

if not firebase_admin._apps:
    print('initializing')
    cred = credentials.Certificate("lastest.json")
    app = firebase_admin.initialize_app(cred, name='authentication_app')
    print(app.name)