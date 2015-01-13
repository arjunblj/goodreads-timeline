
import simplejson as json
import xmltodict

from rauth.service import OAuth1Service, OAuth1Session

from bookviz import app, models


class DataRequest(object):

    base_url = '' # Set on whatever classes this is mixed into.

    def __init__(self):
        self.goodreads = OAuth1Service(
            name='goodreads',
            consumer_key=app.config['GOODREADS_CONSUMER_KEY'],
            consumer_secret=app.config['GOODREADS_CONSUMER_SECRET'],
            request_token_url=self.base_url+'request_token',
            authorize_url=self.base_url+'authorize',
            access_token_url=self.base_url+'access_token',
            )

        self.request_token, self.request_token_secret = self.goodreads.get_request_token(
            header_auth=True)

    def _create_session(self):
        self.session = self.goodreads.get_auth_session(self.request_token,
            self.request_token_secret)

    def _request(self, url, params={}, type='GET', return_json=False):
        """Posts/gets requests to Goodreads, returns JSON if specifed.
        """

        if not hasattr(self, 'session'):
            self._create_session()

        if type == 'GET':
            response = self.session.get(url, data=params)
        elif type == 'POST':
            response = self.session.post(url, data=params)

        if return_json:
            response = json.loads(json.dumps(
                xmltodict.parse(response.content)))['GoodreadsResponse']

        return response



class GoodreadsOAuth(DataRequest):

    base_url = 'http://www.goodreads.com/oauth/'

    def get_auth_url(self):
        """Creates the url where someone authorizes their account to the app.
        """

        auth_url = self.goodreads.get_authorize_url(self.request_token)
        return auth_url

    def connect(self):

        auth_user_resp = self._request('https://www.goodreads.com/api/auth_user',
            return_json=True)

        # If the request for user auth info was successfully made...
        if auth_user_resp['Request']['authentication'] == 'true':
            user_data = auth_user_resp['user']
            user_model = models.User(name=user_data['name'],
                goodreads_id=user_data['@id'], profile_url=user_data['link'])
            user_model.save()

        ## Yeah, yeah, '@id' is right. Goodreads API is silly.
        user_id = auth_user_resp['user']['@id']
        params = dict(key=app.config['GOODREADS_CONSUMER_KEY'],
            id=user_id)
        user_data_resp = self._request('https://www.goodreads.com/user/show/' +
            user_id + '.xml', params=params, return_json=True)['user']

        user_model.img_url = user_data_resp['image_url']
        user_model.save()
