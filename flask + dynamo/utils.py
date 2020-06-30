import requests
from api_connection import genius_keys
import json

PRIMARY_URL_PATH = 'api.genius.com/'


def normalize_request(request):

    if request.status_code != 200:
        raise ConnectionError('Something went wrong durint the request')

    response = json.loads(request.text)
    if response['meta']['status'] != 200:
        raise ConnectionError(response['meta']['message'])

    return response['response']

##############################################################################


def get_artist_songs(_id):

    return_size = 10
    header = {'Authorization': 'Bearer ' + genius_keys['acess_token']}
    url = PRIMARY_URL_PATH + 'artists/{}/songs?per_page={}'.format(
        _id, return_size
    )

    req = requests.get(url, header=header)
    response = normalize_request(req)
    return response['response']['songs']


def get_artist_name(_id):

    header = {'Authorization': 'Bearer ' + genius_keys['acess_token']}
    url = PRIMARY_URL_PATH + 'artists/{}'.format(_id)

    req = requests.get(url, header=header)
    response = normalize_request(req)
    return response['artist']['name']
