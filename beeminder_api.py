#!/usr/bin/env python

import json
import requests
from datetime import datetime


config = json.load(open('config.json', 'r'))
config = config['beeminder']

username = config['username']
auth_token = config['auth_token']
goal = 'test'


def get(endpoint):

    r = requests.get(endpoint, params = {'auth_token': auth_token})
    return json.loads(r.text)


def post(endpoint, payload):

    payload['auth_token'] = auth_token
    r = requests.post(endpoint, params = payload)

    return json.loads(r.text)



if __name__ == '__main__':

    url = 'https://www.beeminder.com/api/v1/users/%s/goals/%s/datapoints.json'
    url = url % (username, goal)
    payload = {
        "timestamp": 1325523600,
        "value": 130.1,
        }

    result = post(url, payload)
    print json.dumps(result, sort_keys=True, indent=4)
    result = get(url)
    print json.dumps(result, sort_keys=True, indent=4)