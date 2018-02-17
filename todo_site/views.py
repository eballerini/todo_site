from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from django.http import HttpResponseRedirect

DEFAULT_HOME_URL = '/todo/'

@login_required
def login_redirect_alexa(request):
    print('>>> login_redirect_alexa')
    return render(request, 'registration/login-redirect-alexa.html', {})
    
@login_required
def home(request):
    print('*** home ***')
    print("request: {}".format(request))
    # use redirect_uri if exists (alexa mode) or use default (default login)
    redirect_uri = request.session.pop('redirect_uri', DEFAULT_HOME_URL)
    state = request.session.pop('state', None)
    
    print("redirect_uri: {}".format(redirect_uri))
    print('state: {}'.format(state))
    if redirect_uri != DEFAULT_HOME_URL:
        # http://localhost:8000/accounts/login/?client_id=alexa123&redirect_uri=/login_redirect_alexa&state=ok
        # For implicit grant, include the state, access_token, and token_type in the URL fragment. The token_type should be Bearer.
        # e.g.
        # https://pitangui.amazon.com/spa/skill/account-linking-status.html?vendorId=AAAAAAAAAAAAAA#state=xyz
        # &access_token=2YotnFZFEjr1zCsicMWpAA&token_type=Bearer
        #
        access_token = get_access_token()
        redirect_uri = redirect_uri + '#state=' + state + '&token_type=Bearer&access_token=' + access_token
    
    print("final redirect_uri: {}".format(redirect_uri))
    return HttpResponseRedirect(redirect_uri)

def get_access_token():
    # TODO fix
    return 'abc'