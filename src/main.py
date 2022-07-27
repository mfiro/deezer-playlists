import deezer
import os

from helpers import get_test_playlist
from pretty_playlist import make_pretty_md
from archive import get_catalog, save_as_json, save_as_pretty_table


def main():
    # get the catalog:
    catalog_path = os.path.join(os.path.dirname(__file__), '../data/catalog/catalog.txt')
    catalog = get_catalog(catalog_path)

    # initated the deezer client
    client = deezer.Client()

    # get playlist tracks and artists:
    for id in catalog:

        # get playlist
        print(f"Getting the playlist {id} ...")
        playlist = client.get_playlist(id)
        playlist = playlist.as_dict()

        # remove the share key from dict. It changes constantly and causes not useful diff 
        playlist.pop('share') 
        print(f"Playlist found! name: {playlist['title']}, {playlist['nb_tracks']} Tracks")

        # saving to playlist as json file. Dest: ../data/playlists/id.json
        save_path = os.path.join(os.path.dirname(__file__), f"../data/playlists/{playlist['id']}.json")
        save_as_json(playlist, save_path)

        # saving as a pretty table. ../data/playlists_pretty/id.md
        current_dir = os.path.dirname(__file__)
        save_path = os.path.join(current_dir, f"../data/playlists_pretty/{playlist['id']}.md")
        save_as_pretty_table(playlist, save_path)       


def dummy_main():
    """ In order to prevent real api calls"""
    
    # get the catalog:
    catalog_path = os.path.join(os.path.dirname(__file__), '../data/catalog/catalog.txt')
    catalog = get_catalog(catalog_path)

    # get some dummy data to start with
    playlist = get_test_playlist(catalog)

    # save the template
    template_path = os.path.join(os.path.dirname(__file__), f'../data/playlists_pretty/table_template.md')
    save_as_pretty_table(playlist, template_path)  
       

if __name__ == "__main__":
    dummy_mode = False

    if dummy_mode:
        dummy_main()
    else:
        main()