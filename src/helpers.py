import json
import os


def get_dummy_tracks(catalog):
    """ In order to prevent real api calls"""

    # load json from files
    id = catalog[0]
    playlist_path = os.path.join(os.path.dirname(__file__), f'../data/playlists/{id}.json')
    with open(playlist_path, 'r') as f:
        tracks = json.load(f)
    
    return tracks


def list2prettyrow(l):
    # convert everything to str
    l = [str(i) for i in l]
    pretty = ' | '.join(['', *l,''])
    pretty = pretty.strip() # delete both leading and trailing spaces
    pretty += '\n'
    return pretty 