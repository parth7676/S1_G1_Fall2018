from django.contrib.auth.hashers import check_password

from myapp.models import User


class CustomAuth(object):
    def authenticate(self, request, username=None, password=None):
        user = User.objects.filter(email=username).select_related('password').first()
        print(user.password.encryptedPassword)
        pwd_valid = check_password(password, user.password.encryptedPassword)
        if user and pwd_valid:
            return user
        else:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.filter(userID=user_id).first()
        except User.DoesNotExist:
            return None
