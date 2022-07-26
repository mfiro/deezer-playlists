import json
import os


def get_test_playlist(catalog):
    """ In order to prevent real api calls"""

    # load json from files
    id = catalog[0]
    playlist_path = os.path.join(os.path.dirname(__file__), f'../data/playlists/{id}.json')
    with open(playlist_path, 'r') as f:
        playlist = json.load(f)
    
    return playlist


def list2prettyrow(l):
    # convert everything to str
    l = [str(i) for i in l]
    pretty = ' | '.join(['', *l,''])
    pretty = pretty.strip() # delete both leading and trailing spaces
    pretty += '\n'
    return pretty 

def seconds2hms(s):
    """Converts seconds to hh:mm:ss format
    if the hh=00 the result will be mm:ss"""
    
    hours, remainder = divmod(s, 3600)
    minutes, seconds = divmod(remainder, 60)
    if hours==0:
        return '{:02}:{:02}'.format(int(minutes), int(seconds))
    else:
        return '{:02}:{:02}:{:02}'.format(int(hours), int(minutes), int(seconds))


def create_url_markdown(url, link_text):
    """creates a url in markdown style for github"""
    return f'[{link_text}]({url})'