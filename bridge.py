#!/usr/bin/env python

import json

import beeminder_api
import fitbit_api


def fitbit_to_beeminder(point):

    new_point = {}

    new_point['value'] = round(point[u'weight'] * 2.20462, 2)
    new_point['timestamp'] = int(point[u'logId'] * 1e-3)
    new_point['comment'] = 'sent from fitbit'

    print new_point
    print beeminder_api.post(payload = new_point)



if __name__ == '__main__':


    current = max([d['timestamp'] for d in beeminder_api.weight()])
    current = current * 1000.0

    new_values = [d for d in fitbit_api.weight() if d[u'logId'] > current]

    for val in new_values:

        fitbit_to_beeminder(val)


