from flask import Blueprint, jsonify
from utils import get_artist_name, get_artist_songs
from db_connection import save_search_response

routes = Blueprint('routes', __name__)


@routes.route('/')
def index():
    return 'It works!', 200


@routes.route('/search/<:artist>?<:cache>')
def search(artist, cache):

    try:
        songs = get_artist_songs(artist)
        name = get_artist_name(artist)

        response = {
                'top_10_songs': songs,
                'artist_name': name
            }

        save_search_response(response)

    except ConnectionError:
        return jsonify({
            'status': 200,
            'response': {
                'top_10_songs': songs,
                'artist_name': name
            }
        })
