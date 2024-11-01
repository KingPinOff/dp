from django.contrib.auth.backends import ModelBackend
from firebase_admin import auth
import firebase_admin
from firebase_admin import auth
from firebase_admin import credentials
import os

class FirebaseBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None):
        if not firebase_admin._apps:
            print('initializing')
            cred = credentials.Certificate("lastest.json")
            firebase_admin.initialize_app(cred, name='authentication_app')
        try:
            user = auth.get_user_by_email(username)
            if user and user.uid:
                # Check if the user exists in your Django database
                try:
                    django_user = request.user.objects.get(firebase_uid=user.uid)
                    return django_user
                except request.user.DoesNotExist:
                    # Create a new Django user if they don't exist
                    django_user = request.user.objects.create_user(
                        username=username,
                        email=user.email,
                        firebase_uid=user.uid,
                    )
                    return django_user
        except auth.UserNotFoundError:
            return None