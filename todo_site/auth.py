from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User

from django.http import HttpResponseRedirect

class BackendAuthenticator:
    
    def authenticate(self, request, username=None, password=None):
        print("[authenticate] request: {}".format(request))
        user = None
        try:
            user = User.objects.get(username=username, is_active=True)
            print("found user: {}".format(username))
            # uncomment this to check the password
            # pwd_valid = check_password(password, user.password)
            # print('password is valid: {}'.format(pwd_valid))
            # if not pwd_valid:
            #     user = None
            
        except User.DoesNotExist:
            print("user not found")
            return None
            
        client_id = request.GET.get('client_id', '')
        
        if client_id == 'alexa123':
            redirect_uri = request.GET.get('redirect_uri')
            state = request.GET.get('state')
            # http://localhost:8000/accounts/login/?client_id=alexa123&redirect_uri=/login_redirect_alexa&state=ok
            print('redirect_uri: {}'.format(redirect_uri))
            print('state: {}'.format(state))
            request.session['redirect_uri'] = redirect_uri
            request.session['state'] = state
            
        return user
        
      
    def get_user(self, user_id):
        user = None
        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            print("user not found")
            
        return user
