import re
import itertools

from social_core.backends.oauth import BaseOAuth2
from crux.models import User


class FigshareBackend(BaseOAuth2):
    name = 'figshare'
    AUTHORIZATION_URL = 'https://figshare.com/account/applications/authorize'
    ACCESS_TOKEN_URL = 'https://api.figshare.com/v2/token'
    REFRESH_TOKEN_URL = 'https://api.figshare.com/v2/token'
    ACCESS_TOKEN_METHOD = 'POST'
    ID_KEY = 'id'

    def get_user_details(self, response):
        email = response.get('email')
        details = {
            'first_name': response.get('first_name'),
            'last_name': response.get('last_name'),
            'email': email,
        }
        if email:
            username = uname = re.sub('[^a-zA-Z0-9-_ \n]', '',
                                      email.split('@')[0])
            i = itertools.count(1)
            while (User.objects.filter(username=username).exists()):
                username = f'{uname}{next(i)}'
            details['username'] = username

        return details

    def user_data(self, access_token, *args, **kwargs):
        url = 'https://api.figshare.com/v2/account'
        resp = self.get_json(
            url, headers={'Authorization': f'token {access_token}'})
        return resp
