#!/usr/bin/env python

import os, httplib
from oauth import oauth
import json


config = json.load(open('config.json', 'r'))

CONSUMER_KEY = config['CONSUMER_KEY']
CONSUMER_SECRET = config['CONSUMER_SECRET']
SERVER = config['SERVER']
secret = config['secret']
token = config['token']

access_token = 'oauth_token_secret=%s&oauth_token=%s' % (secret, token)


def call(access_token, endpoint):

    signature_method = oauth.OAuthSignatureMethod_PLAINTEXT()
    connection = httplib.HTTPSConnection(SERVER)

    #build the access token from a string
    access_token = oauth.OAuthToken.from_string(access_token)
    consumer = oauth.OAuthConsumer(CONSUMER_KEY, CONSUMER_SECRET)
    oauth_request = oauth.OAuthRequest.from_consumer_and_token(consumer,
        token=access_token, http_url=endpoint)
    oauth_request.sign_request(signature_method, consumer, access_token)
    headers = oauth_request.to_header(realm='api.fitbit.com')
    connection.request('GET', endpoint, headers=headers)
    resp = connection.getresponse()
    json = resp.read()

    return json


if __name__ == '__main__':

    print call(access_token, endpoint='/1/user/-/body/log/weight/date/2012-09-01/30d.json')