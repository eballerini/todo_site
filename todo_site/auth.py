from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User


class BackendAuthenticator:
    
    def authenticate(self, request, username=None, password=None):
        # self.list_users()
        print("request: {}".format(request))
        # TODO extract from request:
        # state
        # redirect_uri
        # client_id
        #
        # For implicit grant, include the state, access_token, and token_type in the URL fragment. The token_type should be Bearer.
        # e.g.
        # https://pitangui.amazon.com/spa/skill/account-linking-status.html?vendorId=AAAAAAAAAAAAAA#state=xyz
        # &access_token=2YotnFZFEjr1zCsicMWpAA&token_type=Bearer
        # 
        # if client = 'alexa123':
        # redirect to redirect_uri
        # else:
        # redirect to /todo
        user = None
        try:
            user = User.objects.get(username=username)
            print("found user {}".format(username))
            # uncomment this to check the password
            # pwd_valid = check_password(password, user.password)
            # print('password is valid: {}'.format(pwd_valid))
            # if not pwd_valid:
            #     user = None
            
        except User.DoesNotExist:
            print("user not found")
            return None
            
        # TODO fix this
        client_id = request.POST.get('client_id', '')
        print('client_id: {}'.format(client_id))
            
        return user
        
      
    def get_user(self, user_id):
        print("get_user")
        user = None
        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            print("user not found")
            
        return user
        
    def list_users(self):
        print('all users')
        users = User.objects.all()
        for u in users:
            print(u.__dict__)