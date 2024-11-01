import firebase_admin
from firebase_admin import auth
from firebase_admin import credentials
import os
if not firebase_admin._apps:
    print('initializing')
    cred = credentials.Certificate("lastest.json")
    firebase_admin.initialize_app(cred, name='authentication_app')
    print(app.name)
